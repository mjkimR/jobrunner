# Hub Module - DB Schema Design

> [!NOTE]
> 이 문서는 `jr-hub` 모듈의 데이터베이스 스키마 설계를 정의합니다.
> 참고: [PROJECT_REQUIREMENTS.md](PROJECT_REQUIREMENTS.md), [MODULES.md](MODULES.md)

---

## 개요

Hub 모듈은 3가지 핵심 Feature로 구성됩니다:

| Feature | 역할 | 주요 엔티티 |
|---------|------|-------------|
| **Tasks** | Task Manager - 할일 관리, Host Agent의 영구 메모리 | Task, SubTask |
| **Agents** | Agent Manager - Worker LLM Agent 생명주기 관리 | Agent, AgentExecution |
| **Gateway** | Local Agent Gateway - 채팅 인터페이스, 라우팅 | Conversation, Message |

---

## 1. Tasks (Task Manager)

### 1.1. Task

Host Agent 또는 사용자가 관리하는 TODO 항목.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ tasks                                                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│ PK  id              UUID          NOT NULL                                  │
│     title           VARCHAR(255)  NOT NULL                                  │
│     description     TEXT          NULL                                      │
│     status          VARCHAR(50)   NOT NULL  DEFAULT 'pending'               │
│     priority        VARCHAR(20)   NOT NULL  DEFAULT 'normal'                │
│     urgency         VARCHAR(20)   NOT NULL  DEFAULT 'normal'                │
│     complexity      VARCHAR(20)   NOT NULL  DEFAULT 'simple'                │
│     queue           VARCHAR(100)  NOT NULL  DEFAULT 'default'               │
│ FK  parent_task_id  UUID          NULL      -> tasks.id                     │
│     source          VARCHAR(50)   NOT NULL  DEFAULT 'user'                  │
│     external_ref    VARCHAR(255)  NULL      -- GitHub Issue URL, etc.       │
│     due_date        TIMESTAMP     NULL                                      │
│     completed_at    TIMESTAMP     NULL                                      │
│     result_summary  TEXT          NULL                                      │
│     created_at      TIMESTAMP     NOT NULL  DEFAULT now()                   │
│     updated_at      TIMESTAMP     NOT NULL  DEFAULT now()                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

**컬럼 설명:**

| 컬럼 | 설명 | Enum 값 |
|------|------|---------|
| `status` | Task 진행 상태 | `pending`, `in_progress`, `review`, `done`, `cancelled` |
| `priority` | 우선순위 | `low`, `normal`, `high`, `critical` |
| `urgency` | 긴급도 (라우팅 결정에 사용) | `low`, `normal`, `high`, `critical` |
| `complexity` | 복잡도 (라우팅 결정에 사용) | `simple`, `moderate`, `complex` |
| `queue` | 처리 대상 큐 (Dagster sensor polling용) | `default`, `host-agent`, `local-agent`, `workflow` 등 |
| `source` | Task 생성 출처 | `user`, `host_agent`, `gateway`, `workflow`, `system` |
| `external_ref` | 외부 시스템 연동 참조 | GitHub Issue URL 등 |

**관계:**
- `parent_task_id`: Self-referencing FK로 Task → SubTask 분해 지원

**Queue 설명:**
- `host-agent`: Host Agent만 처리 가능 (복잡한 판단, 코드 생성 등)
- `local-agent`: Local LLM Agent가 처리 가능한 작업
- `workflow`: Dagster Job으로 처리할 수 있는 정형화된 작업
- `default`: 라우팅 결정 전 기본 큐

---

### 1.2. TaskTag

Task 분류를 위한 태그.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ task_tags                                                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│ PK  id              UUID          NOT NULL                                  │
│     name            VARCHAR(100)  NOT NULL  UNIQUE                          │
│     description     VARCHAR(255)  NULL                                      │
│     color           VARCHAR(7)    NULL      -- #RRGGBB                      │
│     created_at      TIMESTAMP     NOT NULL  DEFAULT now()                   │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ task_tag_associations (M:N Junction Table)                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│ FK  task_id         UUID          NOT NULL  -> tasks.id                     │
│ FK  tag_id          UUID          NOT NULL  -> task_tags.id                 │
│     PRIMARY KEY (task_id, tag_id)                                           │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 1.3. TaskHistory

Task 상태 변경 및 할당 이력. Agent 할당도 이력으로 관리하여 추적 가능.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ task_history                                                                │
├─────────────────────────────────────────────────────────────────────────────┤
│ PK  id              UUID          NOT NULL                                  │
│ FK  task_id         UUID          NOT NULL  -> tasks.id                     │
│     event_type      VARCHAR(50)   NOT NULL                                  │
│     previous_value  VARCHAR(100)  NULL                                      │
│     new_value       VARCHAR(100)  NOT NULL                                  │
│ FK  assigned_agent_id UUID        NULL      -> agents.id                    │
│     changed_by      VARCHAR(100)  NOT NULL                                  │
│     comment         TEXT          NULL                                      │
│     created_at      TIMESTAMP     NOT NULL  DEFAULT now()                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

**컬럼 설명:**

| 컬럼 | 설명 | Enum 값 |
|------|------|---------|  
| `event_type` | 이력 이벤트 유형 | `status_change`, `assignment`, `queue_change`, `priority_change` |
| `assigned_agent_id` | 할당된 Agent (event_type=assignment일 때) | - |

---

## 2. Agents (Agent Manager)

> [!NOTE]
> Hub는 Agent 설정(Configuration)만 관리하고, 실제 LLM 호출 및 실행은 Workflow Engine(Dagster)에서 처리합니다.
> - **Configured Agent**: Hub에서 Model + Capability로 설정, Workflow Engine에서 실행
> - **Graph Agent**: Workflow Engine에서 LangGraph Asset으로 직접 정의

### 2.1. AIModelRegistry

사용 가능한 AI 모델 목록. `catalog.yml`의 `models` 섹션과 호환.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ ai_model_registry                                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│ PK  id              UUID          NOT NULL                                  │
│     name            VARCHAR(100)  NOT NULL  UNIQUE                          │
│     provider        VARCHAR(50)   NOT NULL                                  │
│     model_name      VARCHAR(100)  NOT NULL                                  │
│     model_type      VARCHAR(50)   NOT NULL  DEFAULT 'llm'                   │
│     description     TEXT          NULL                                      │
│     capabilities    JSONB         NOT NULL  DEFAULT '[]'                    │
│     args            JSONB         NOT NULL  DEFAULT '{}'                    │
│     param_spec      JSONB         NULL      -- exclude/map 규칙             │
│     is_active       BOOLEAN       NOT NULL  DEFAULT true                    │
│     created_at      TIMESTAMP     NOT NULL  DEFAULT now()                   │
│     updated_at      TIMESTAMP     NOT NULL  DEFAULT now()                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

**컬럼 설명:**

| 컬럼 | 설명 | 예시 |
|------|------|------|
| `provider` | 모델 제공자 | `ollama`, `openai`, `openai-compatible`, `google` |
| `model_name` | 모델 식별자 | `gpt-4`, `gemini-2.5-flash`, `qwen2.5-coder:7b` |
| `model_type` | 모델 유형 | `llm`, `text-embedding`, `vision` |
| `args` | 연결 인자 | `{"api_key": "${OPENAI_API_KEY}", "base_url": "..."}` |
| `param_spec` | 파라미터 변환 규칙 | `{"exclude": ["temperature"], "map": {"max_tokens": "max_completion_tokens"}}` |
| `capabilities` | 모델 능력 태그 | `["code", "reasoning", "vision"]` |

---

### 2.2. AIModelAlias

모델 별칭. fallback 체인 지원. `catalog.yml`의 `aliases` 섹션과 호환.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ ai_model_aliases                                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│ PK  id              UUID          NOT NULL                                  │
│     name            VARCHAR(100)  NOT NULL  UNIQUE                          │
│     model_type      VARCHAR(50)   NOT NULL                                  │
│ FK  target_model_id UUID          NOT NULL  -> ai_model_registry.id         │
│     fallbacks       JSONB         NULL      -- ["alias1", "alias2"]         │
│     description     TEXT          NULL                                      │
│     is_active       BOOLEAN       NOT NULL  DEFAULT true                    │
│     created_at      TIMESTAMP     NOT NULL  DEFAULT now()                   │
│     updated_at      TIMESTAMP     NOT NULL  DEFAULT now()                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

**컬럼 설명:**

| 컬럼 | 설명 | 예시 |
|------|------|------|
| `name` | 별칭 이름 | `llm-default`, `llm-high-performance` |
| `model_type` | 모델 유형 | `llm`, `text-embedding` |
| `target_model_id` | 대상 모델 FK | ai_model_registry 참조 |
| `fallbacks` | fallback 별칭 목록 | `["llm-default"]` |

---

### 2.3. AIModelGroup

모델 그룹. `catalog.yml`의 `groups` 섹션과 호환.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ ai_model_groups                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ PK  id              UUID          NOT NULL                                  │
│     name            VARCHAR(100)  NOT NULL  UNIQUE                          │
│     model_type      VARCHAR(50)   NOT NULL                                  │
│     members         JSONB         NOT NULL  -- ["alias1", "alias2"]         │
│ FK  default_alias_id UUID         NULL      -> ai_model_aliases.id          │
│     description     TEXT          NULL                                      │
│     created_at      TIMESTAMP     NOT NULL  DEFAULT now()                   │
│     updated_at      TIMESTAMP     NOT NULL  DEFAULT now()                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

**컬럼 설명:**

| 컬럼 | 설명 | 예시 |
|------|------|------|
| `name` | 그룹 이름 | `llm-models`, `embedding-models` |
| `members` | 멤버 별칭 목록 | `["llm-default", "llm-high-performance"]` |
| `default_alias_id` | 기본 별칭 FK | ai_model_aliases 참조 |

---

### 2.4. ConfiguredAgent

Hub에서 설정으로 정의되는 Agent. Model + Skill/MCP 조합.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ configured_agents                                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│ PK  id              UUID          NOT NULL                                  │
│     name            VARCHAR(100)  NOT NULL  UNIQUE                          │
│     description     TEXT          NULL                                      │
│ FK  model_id        UUID          NOT NULL  -> ai_model_registry.id         │
│     system_prompt   TEXT          NULL                                      │
│     config          JSONB         NOT NULL  DEFAULT '{}'                    │
│     is_active       BOOLEAN       NOT NULL  DEFAULT true                    │
│     created_at      TIMESTAMP     NOT NULL  DEFAULT now()                   │
│     updated_at      TIMESTAMP     NOT NULL  DEFAULT now()                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

**컬럼 설명:**

| 컬럼 | 설명 | 예시 |
|------|------|------|
| `model_id` | 사용할 AI 모델 (FK) | ai_model_registry 참조 |
| `system_prompt` | 시스템 프롬프트 | "You are a code review assistant..." |
| `config` | 실행 설정 | `{"temperature": 0.7, "max_tokens": 4096}` |

---

### 2.5. ConfiguredAgentSkill / ConfiguredAgentMCP (M:N)

Configured Agent에 연결된 Skill 및 MCP.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ configured_agent_skills (M:N Junction Table)                                │
├─────────────────────────────────────────────────────────────────────────────┤
│ FK  agent_id        UUID          NOT NULL  -> configured_agents.id         │
│ FK  skill_id        UUID          NOT NULL  -> skill_registry.id            │
│     PRIMARY KEY (agent_id, skill_id)                                        │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ configured_agent_mcps (M:N Junction Table)                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│ FK  agent_id        UUID          NOT NULL  -> configured_agents.id         │
│ FK  mcp_id          UUID          NOT NULL  -> mcp_registry.id              │
│     PRIMARY KEY (agent_id, mcp_id)                                          │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 2.6. AgentExecution

Agent 실행 이력. Configured Agent 및 Graph Agent 모두의 실행을 추적.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ agent_executions                                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│ PK  id                  UUID          NOT NULL                              │
│     agent_type          VARCHAR(50)   NOT NULL                              │
│ FK  configured_agent_id UUID          NULL      -> configured_agents.id     │
│     graph_agent_name    VARCHAR(100)  NULL      -- LangGraph Asset 이름     │
│ FK  task_id             UUID          NULL      -> tasks.id                 │
│     execution_type      VARCHAR(50)   NOT NULL                              │
│     status              VARCHAR(50)   NOT NULL  DEFAULT 'pending'           │
│     input_data          JSONB         NULL                                  │
│     output_data         JSONB         NULL                                  │
│     error_message       TEXT          NULL                                  │
│     started_at          TIMESTAMP     NULL                                  │
│     completed_at        TIMESTAMP     NULL                                  │
│     token_usage         JSONB         NULL                                  │
│     dagster_run_id      VARCHAR(100)  NULL      -- Dagster Run ID 참조      │
│     created_at          TIMESTAMP     NOT NULL  DEFAULT now()               │
│     updated_at          TIMESTAMP     NOT NULL  DEFAULT now()               │
└─────────────────────────────────────────────────────────────────────────────┘
```

**컬럼 설명:**

| 컬럼 | 설명 | Enum 값 |
|------|------|---------|
| `agent_type` | Agent 유형 | `configured`, `graph` |
| `configured_agent_id` | Configured Agent FK (agent_type=configured일 때) | - |
| `graph_agent_name` | LangGraph Asset 이름 (agent_type=graph일 때) | `react_agent`, `plan_execute_agent` |
| `execution_type` | 실행 유형 | `task_processing`, `routing_decision`, `chat_response`, `workflow_step` |
| `status` | 실행 상태 | `pending`, `running`, `success`, `failed`, `cancelled`, `timeout` |
| `token_usage` | LLM 토큰 사용량 | `{"input_tokens": N, "output_tokens": N}` |
| `dagster_run_id` | Dagster 실행 ID | Workflow Engine 실행 추적용 |

---

### 2.7. SkillRegistry

Agent에 주입 가능한 Skill 카탈로그.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ skill_registry                                                              │
├─────────────────────────────────────────────────────────────────────────────┤
│ PK  id              UUID          NOT NULL                                  │
│     name            VARCHAR(100)  NOT NULL  UNIQUE                          │
│     description     TEXT          NULL                                      │
│     skill_path      VARCHAR(500)  NOT NULL  -- SKILL.md 파일 경로            │
│     version         VARCHAR(20)   NOT NULL  DEFAULT '1.0.0'                 │
│     is_active       BOOLEAN       NOT NULL  DEFAULT true                    │
│     created_at      TIMESTAMP     NOT NULL  DEFAULT now()                   │
│     updated_at      TIMESTAMP     NOT NULL  DEFAULT now()                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 2.8. MCPRegistry

Agent에 연결 가능한 MCP Server 목록.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ mcp_registry                                                                │
├─────────────────────────────────────────────────────────────────────────────┤
│ PK  id              UUID          NOT NULL                                  │
│     name            VARCHAR(100)  NOT NULL  UNIQUE                          │
│     description     TEXT          NULL                                      │
│     mcp_type        VARCHAR(50)   NOT NULL                                  │
│     connection_config JSONB       NOT NULL  DEFAULT '{}'                    │
│     is_active       BOOLEAN       NOT NULL  DEFAULT true                    │
│     created_at      TIMESTAMP     NOT NULL  DEFAULT now()                   │
│     updated_at      TIMESTAMP     NOT NULL  DEFAULT now()                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

**컬럼 설명:**

| 컬럼 | 설명 | Enum 값 |
|------|------|---------|
| `mcp_type` | MCP 서버 유형 | `dagster`, `github`, `filesystem`, `custom` |
| `connection_config` | 연결 설정 | `{"url": "...", "api_key_env": "..."}` |

---

## 3. Gateway (Local Agent Gateway)

### 3.1. Conversation

채팅 대화 세션.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ conversations                                                               │
├─────────────────────────────────────────────────────────────────────────────┤
│ PK  id              UUID          NOT NULL                                  │
│     title           VARCHAR(255)  NULL      -- 자동 생성 또는 사용자 설정    │
│     channel         VARCHAR(50)   NOT NULL  DEFAULT 'web'                   │
│     status          VARCHAR(50)   NOT NULL  DEFAULT 'active'                │
│     context         JSONB         NOT NULL  DEFAULT '{}'                    │
│     started_at      TIMESTAMP     NOT NULL  DEFAULT now()                   │
│     ended_at        TIMESTAMP     NULL                                      │
│     created_at      TIMESTAMP     NOT NULL  DEFAULT now()                   │
│     updated_at      TIMESTAMP     NOT NULL  DEFAULT now()                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

**컬럼 설명:**

| 컬럼 | 설명 | Enum 값 |
|------|------|---------|
| `channel` | 채팅 채널 | `web`, `telegram`, `slack`, `cli` |
| `status` | 대화 상태 | `active`, `archived`, `deleted` |
| `context` | 대화 컨텍스트 (사용자 설정, 기본 상태 등) | `{"user_preferences": {...}}` |

---

### 3.2. Message

대화 내 메시지.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ messages                                                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│ PK  id              UUID          NOT NULL                                  │
│ FK  conversation_id UUID          NOT NULL  -> conversations.id             │
│     role            VARCHAR(20)   NOT NULL                                  │
│     content         TEXT          NOT NULL                                  │
│     content_type    VARCHAR(50)   NOT NULL  DEFAULT 'text'                  │
│     metadata        JSONB         NOT NULL  DEFAULT '{}'                    │
│ FK  agent_execution_id UUID       NULL      -> agent_executions.id          │
│     created_at      TIMESTAMP     NOT NULL  DEFAULT now()                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

**컬럼 설명:**

| 컬럼 | 설명 | Enum 값 |
|------|------|---------|
| `role` | 메시지 발신자 | `user`, `assistant`, `system` |
| `content_type` | 컨텐츠 유형 | `text`, `markdown`, `json`, `image_url` |
| `metadata` | 추가 메타정보 | `{"model": "...", "tokens": {...}, "routing": {...}}` |

---

### 3.3. RoutingLog

Gateway의 라우팅 결정 이력.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ routing_logs                                                                │
├─────────────────────────────────────────────────────────────────────────────┤
│ PK  id              UUID          NOT NULL                                  │
│ FK  message_id      UUID          NOT NULL  -> messages.id                  │
│     routing_result  VARCHAR(50)   NOT NULL                                  │
│     confidence      FLOAT         NULL                                      │
│     reasoning       TEXT          NULL                                      │
│ FK  target_task_id  UUID          NULL      -> tasks.id                     │
│ FK  target_agent_id UUID          NULL      -> agents.id                    │
│     created_at      TIMESTAMP     NOT NULL  DEFAULT now()                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

**컬럼 설명:**

| 컬럼 | 설명 | Enum 값 |
|------|------|---------|
| `routing_result` | 라우팅 결과 | `self_handled`, `local_agent`, `task_deferred`, `cloud_agent` |
| `confidence` | 라우팅 결정 신뢰도 (0.0 ~ 1.0) | - |

---

## 인덱스 설계

### Tasks
```sql
CREATE INDEX idx_tasks_status ON tasks(status);
CREATE INDEX idx_tasks_queue ON tasks(queue);
CREATE INDEX idx_tasks_status_queue ON tasks(status, queue);  -- Dagster sensor polling용
CREATE INDEX idx_tasks_priority ON tasks(priority);
CREATE INDEX idx_tasks_urgency ON tasks(urgency);
CREATE INDEX idx_tasks_parent ON tasks(parent_task_id);
CREATE INDEX idx_tasks_created ON tasks(created_at DESC);

CREATE INDEX idx_task_history_task ON task_history(task_id);
CREATE INDEX idx_task_history_agent ON task_history(assigned_agent_id);
CREATE INDEX idx_task_history_event_type ON task_history(event_type);
```

### Agents
```sql
CREATE INDEX idx_ai_models_provider ON ai_model_registry(provider);
CREATE INDEX idx_ai_models_type ON ai_model_registry(model_type);
CREATE INDEX idx_ai_models_active ON ai_model_registry(is_active);

CREATE INDEX idx_ai_aliases_type ON ai_model_aliases(model_type);
CREATE INDEX idx_ai_aliases_target ON ai_model_aliases(target_model_id);
CREATE INDEX idx_ai_aliases_active ON ai_model_aliases(is_active);

CREATE INDEX idx_ai_groups_type ON ai_model_groups(model_type);
CREATE INDEX idx_ai_groups_default ON ai_model_groups(default_alias_id);

CREATE INDEX idx_configured_agents_model ON configured_agents(model_id);
CREATE INDEX idx_configured_agents_active ON configured_agents(is_active);

CREATE INDEX idx_agent_executions_type ON agent_executions(agent_type);
CREATE INDEX idx_agent_executions_configured ON agent_executions(configured_agent_id);
CREATE INDEX idx_agent_executions_task ON agent_executions(task_id);
CREATE INDEX idx_agent_executions_status ON agent_executions(status);
CREATE INDEX idx_agent_executions_created ON agent_executions(created_at DESC);
CREATE INDEX idx_agent_executions_dagster ON agent_executions(dagster_run_id);
```

### Gateway
```sql
CREATE INDEX idx_conversations_status ON conversations(status);
CREATE INDEX idx_conversations_created ON conversations(created_at DESC);
CREATE INDEX idx_messages_conversation ON messages(conversation_id);
CREATE INDEX idx_messages_created ON messages(created_at DESC);
CREATE INDEX idx_routing_logs_message ON routing_logs(message_id);
```

---

## 확장 고려사항

### Phase 2+ 확장 시 추가 고려 테이블

1. **UserPreferences** - 사용자별 설정 (멀티테넌시 지원 시)
2. **GraphAgentRegistry** - LangGraph Agent 메타데이터 (Workflow Engine에서 정의된 Asset 목록)
3. **AgentExecutionSteps** - Graph Agent의 단계별 실행 이력 (LangGraph checkpoint 연동)

---

## Changelog

| 날짜 | 버전 | 변경 내용 |
|------|------|----------|
| 2026-02-08 | v0.1.0 | 초기 스키마 설계 |
| 2026-02-08 | v0.1.1 | `queue` 필드 추가, `assigned_agent_id`를 `task_history`로 이동 |
| 2026-02-08 | v0.2.0 | Agent 아키텍처 개편: `ai_model_registry`, `configured_agents` 추가, Configured/Graph Agent 분리 |
| 2026-02-08 | v0.2.1 | AI 카탈로그 호환: `ai_model_aliases`, `ai_model_groups` 추가, `model_type`, `args`, `param_spec` 필드 추가 |

