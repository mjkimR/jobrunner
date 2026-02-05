# 프로젝트 요구사항 명세서: JobRunner

## 1. 프로젝트 개요 (Vision)

- **프로젝트 명:** JobRunner
- **목표:** 반복적인 개인 업무를 자동화하고, 궁극적으로 LLM 기반의 지능형 워크플로우 생성 및 실행이 가능한 **개인 자동화 플랫폼**을 구축한다.
- **핵심 컨셉:**
    - **(Phase 1) 룰 기반 자동화:** 사용자가 정의한 '룰(Rule)'을 스케줄에 따라 실행하고, 결과를 통지하는 실행 환경(Runtime)을 제공한다.
    - **(Phase 2) 태스크/이벤트 시스템:** 일회성 작업, 사람의 개입(승인/리뷰), 외부 시스템 연동 등을 포괄하는 이벤트 기반 태스크 관리 시스템을 구축한다.
    - **(Phase 3) 지능형 자동화:** LLM이 사용자의 자연어 요청을 해석하여 워크플로우를 동적으로 생성하고, 외부 AI 에이전트와 협업하는 시스템으로 발전시킨다.
- **예시 시나리오:**
    - (Phase 1) 매일 아침 특정 주제의 기사를 검색, LLM으로 요약하여 텔레그램으로 전송
    - (Phase 1) 특정 주식의 가격이 지정된 조건을 만족하면 알림 발송
    - (Phase 2) 승인 대기 목록에서 사용자가 텔레그램으로 '승인' 버튼을 누르면 후속 작업 실행
    - (Phase 3) "지난주 AI 관련 뉴스 요약해서 보고서 만들어줘"라는 요청을 LLM이 워크플로우로 변환 후 실행

- **프로젝트 시작 동기:**

    > [!NOTE]
    > 왜 오픈소스 에이전트 프레임워크 + LLM API 조합으로 시작하지 않고, 굳이 정형화된 플랫폼을 직접 구축하는가?

    | 관점 | 직접 구축의 이점 |
    |------|-----------------|
    | **비용 효율성** | CLI 기반 Human-in-the-Loop 방식으로 LLM API 호출 최소화. Gemini CLI 무료 사용량 적극 활용. |
    | **보안 및 통제력** | 내가 허락하지 않은 작업의 폭주 억제. 직접 만들었기에 한계를 알고, 블랙박스 실행보다 안심. |
    | **안정적 재사용** | 한 번 코드화한 작업은 LLM 비결정성 없이 안정적으로 반복 실행 가능. |
    | **커스터마이징** | 내가 만든 도구이므로 원하는 대로 확장 및 수정 가능. |
    | **세밀한 트리거링** | API 자동 호출이 아닌, 원하는 시점에 원하는 모델로 CLI를 통해 명시적 트리거 가능. |

    이 동기는 프로젝트 전반의 아키텍처 결정(Human-in-the-Loop, CLI 중심 워크플로우, 단계적 승인 등)에 일관되게 반영된다.

---

## 2. 용어 정의 (Glossary)

본 문서에서 사용하는 주요 용어를 명확히 정의한다.

| 용어 | 정의 | 비고 |
|---|---|---|
| **룰 (Rule)** | 조건, 액션, 실행 주기가 정의된 자동화 작업의 최소 단위. Phase 1의 핵심 개념. | DB에 저장 |
| **룰 스크립트 (Rule Script)** | 룰 실행 시 구동되는 Python 스크립트. | GitHub에서 관리 |
| **태스크 (Task)** | 실행 가능한 작업의 일반화된 단위. 룰, 일회성 작업, 승인 요청 등을 포괄. | Phase 2 이후 |
| **워크플로우 (Workflow)** | 여러 태스크가 순서/조건에 따라 연결된 실행 흐름. | Phase 2 이후 |
| **이벤트 (Event)** | 시스템 내외부에서 발생하는 트리거. 워크플로우 시작 조건이 됨. | Phase 2 이후 |
| **Artifact** | 룰/워크플로우 실행 결과로 생성되는 파일(보고서, 데이터 등). | Storage에 저장 |

---

## 3. 프로젝트 범위 (Scope)

### Phase 1: 룰 기반 자동화 (PoC)

> [!NOTE]
> Phase 1은 MVP(Minimum Viable Product)로, 핵심 아이디어 검증에 집중한다.

**In-Scope:**
- **룰(Rule) 관리:** 룰 생성, 조회, 수정, 삭제 (CRUD). 데이터베이스(Supabase)에 저장.
- **룰 스크립트 관리:** 사용자가 룰에 매칭되는 실행 스크립트를 직접 개발하여 GitHub 리포지토리에 저장/관리. 실행 환경에서는 호스트 머신의 Git 리포지토리 디렉토리를 Docker 컨테이너에 볼륨 마운트하여 사용.
- **룰 실행 환경:** FastAPI 기반 백엔드 서버, Docker 컨테이너화, 스케줄 기반 실행 (`next_run_at` polling).
- **알림:** 룰 실행 결과 및 조건 충족 시 텔레그램으로 알림 전송.
- **PoC 기능:** `yfinance`를 이용한 미국 주식 가격 모니터링 및 조건 알림.

**Out-of-Scope (Phase 1):**
- 전용 프론트엔드 UI (API와 텔레그램을 통해 상호작용)
- 실시간성 보장 (분/시간 단위 배치 기본)
- 복잡한 워크플로우 (단일 룰 실행만 지원)

---

### Phase 2: 태스크/이벤트 관리 시스템 (중기 목표)

**In-Scope:**
- **태스크/이벤트 모듈:** 일회성 작업, 사람의 개입(승인/리뷰), 외부 시스템 연동을 포괄하는 중앙 허브 구축.
- **Pub/Sub 아키텍처:** 서비스 간 결합도를 낮추기 위한 이벤트 주도 아키텍처 도입 (**초기: 로컬 Docker Redis 기반 메시지 브로커 활용**).
    - **전달/처리 보장(최소 계약):** 기본은 **at-least-once** 전달로 가정하며, 컨슈머는 `event_id`(UUID/ULID 등)를 기준으로 **멱등성(idempotency)** 을 보장해야 한다.
    - 컨슈머는 event_id를 processed table(또는 Redis set)로 dedupe 처리
- **워크플로우 엔진:** 복잡한 태스크 흐름, 상태 관리, 에러 처리를 위한 오케스트레이션 프레임워크 도입 (Dagster / Prefect / Temporal 검토).
- **사용자 상호작용 고도화:** 텔레그램 봇을 통한 양방향 대화형 인터랙션 (인라인 버튼, 승인/반려 처리 등).

---

### Phase 3: 지능형 자동화 (장기 목표)

**In-Scope:**
- **LLM as Planner:** 사용자의 자연어 요청을 LLM이 해석하여 정적 워크플로우 코드를 동적으로 생성.
- **RAG 기반 최적화:** 과거 성공 사례를 Vector DB에 저장, 유사 사례를 Few-shot example로 활용하여 워크플로우 생성 품질 향상.
- **외부 에이전트 연동:** OpenClaw 등 전문화된 에이전트 프레임워크와의 상호 보완적 연동.
- **CLI 기반 Human-in-the-Loop:** Gemini CLI를 활용한 비용 효율적 워크플로우 생성 및 사용자 검토/승인 프로세스.
- **간이 대시보드 UI:** 시스템 운영 상태를 한눈에 볼 수 있는 읽기 전용 웹 대시보드 (선택 사항).

## 4. 기능 요구사항 (Functional Requirements)

| ID | 기능명 | 설명 | 우선순위 |
|---|---|---|---|
| FR-01 | 룰 정의 | 사용자는 자동화하고 싶은 작업의 조건, 액션, 실행 주기 등을 포함한 룰을 생성할 수 있다. | Must |
| FR-02 | 룰 스크립트 생성 지원 | 사용자가 룰 스크립트를 생성하는 과정을 보조하기 위해, 플랫폼은 LLM 기반의 '룰 생성 스킬(Skill)'과 같은 개발 도구를 제공할 수 있다. | Should |
| FR-03 | 룰 실행 | 스케줄러가 DB에 저장된 룰 정보를 기반으로, GitHub에 저장된 해당 룰의 실행 스크립트를 가져와 실행한다. | Must |
| FR-04 | 결과 알림 (Telegram) | 룰 실행 결과 또는 지정된 조건 충족 시, 텔레그램 봇을 통해 사용자에게 메시지를 보낸다. | Must |
| FR-05 | 주가 데이터 조회 (PoC) | `yfinance` 라이브러리를 사용하여 특정 주식의 시세 데이터를 조회한다. | Must (for PoC) |
| FR-06 | 주가 조건 검사 (PoC) | 'FR-05'에서 얻은 데이터가 사용자가 룰에 설정한 조건(예: $500 이상)을 만족하는지 검사한다. | Must (for PoC) |

## 5. 시스템 아키텍처 (System Architecture)

### 5.1. 스케줄링 아키텍처

본 시스템의 룰 스케줄링은 Application 레벨에서 `next_run_at` 필드 기반 polling 방식으로 처리한다.

- **설계 원칙:**
    - **인프라 독립성:** PostgreSQL 특정 확장(pg_cron 등)에 의존하지 않아, 다양한 환경에서 동작 가능.
    - **로컬 환경 호환:** 로컬 Docker 환경에서도 외부 Webhook 수신 없이 완전히 동작.
    - **직관적 디버깅:** `next_run_at` 컬럼 조회만으로 다음 실행 시점 확인 가능.

- **실행 흐름:**
    1. **(External) 주기적 트리거:** 외부 스케줄러(OS cron, Windows Task Scheduler, 또는 앱 내부 루프)가 1분마다 FastAPI의 tick 엔드포인트를 호출한다.
    2. **(App) 실행 대상 룰 조회:** FastAPI는 `rules` 테이블에서 `WHERE next_run_at <= NOW() AND is_active = true` 조건으로 실행 대상 룰들을 조회한다.
    3. **(App) 룰 실행:** 조회된 각 룰에 대해 실행 스크립트를 가져와 실행하고, 콜백을 처리한다.
    4. **(App) 다음 실행 시간 계산:** 실행 완료 후, `schedule` (cron 표현식)을 파싱하여 다음 실행 시간을 계산하고, `next_run_at` 필드를 업데이트한다. (Python `croniter` 라이브러리 활용)

- **Tick 엔드포인트 예시:**
    ```
    POST /api/v1/tick
    → 실행 대상 룰 조회 및 실행
    → 각 룰의 next_run_at 업데이트
    ```

### 5.2. 데이터베이스 스키마

#### Table: `rules`
룰 자체의 정의를 저장합니다.

| Column | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `id` | `uuid` | Primary Key | `a1b2c3d4-...` |
| `name` | `text` | 룰의 이름 | `"Apple 주가 $200 돌파 알림"` |
| `schedule` | `text` | 실행 주기 (Cron 표현식) | `"*/5 * * * *"` (5분마다) |
| `is_active` | `boolean` | 룰 활성화 여부 | `true` |
| `payload` | `jsonb` | 실행 스크립트에 전달될 데이터 | `{ "ticker": "AAPL", "target": 200 }` |
| `execution_script_path`| `text` | 실행할 메인 스크립트 경로 (마운트된 볼륨 내 상대경로) | `"scripts/stock/check_price.py"` |
| `on_success` | `jsonb` | 성공 시 실행할 콜백 설정. PoC 진행하며 구조 확정 예정. | `{"type": "telegram", "config": {...}}` |
| `on_failure` | `jsonb` | 실패 시 실행할 콜백 설정. PoC 진행하며 구조 확정 예정. | `{"type": "log", "config": {...}}` |
| `next_run_at` | `timestampz`| 다음 실행 예정 시간. 스케줄러가 이 시간을 기준으로 실행 대상을 조회. **Not Null**. | `2024-10-26 10:05:00Z` |
| `created_at` | `timestampz` | 생성 시각 | `2024-10-26 10:00:00Z` |

#### Table: `rule_executions`
각 룰의 실행 이력과 결과물 위치를 저장합니다.

| Column | Type | Description |
| :--- | :--- | :--- |
| `id` | `uuid` | 실행 기록의 Primary Key |
| `rule_id` | `uuid` | 실행된 룰의 ID (FK to `rules.id`) |
| `status` | `text` | 실행 결과 (`running`, `success`, `failure`) |
| `executed_at` | `timestampz` | 실행 시작 시각 |
| `log_summary` | `text` | "5개 기사 요약 완료" 등 간단한 실행 로그 |
| `artifact_path` | `text` | **Supabase Storage에 저장된 결과물 파일의 경로** |

### 5.3. 결과물 저장소 (Artifact Storage)

- **기술:** **Supabase Storage**를 사용하여 룰 실행 결과물(파일, 보고서 등)을 저장한다.
- **장점:**
    - **통합 환경:** DB, 인증, 스토리지를 Supabase 플랫폼 내에서 모두 해결
    - **통합 보안:** DB의 RLS(Row Level Security)와 연계하여 파일 접근 권한을 세밀하게 제어 가능
    - **개발 단순성:** 단일 SDK 사용

## 6. 비기능 요구사항 (Non-Functional Requirements)

| ID | 구분 | 설명 |
|---|---|---|
| NFR-01 | 기술 스택 | - **Backend:** FastAPI (Python) <br> - **Database:** Supabase (PostgreSQL) <br> - **Scheduler (Phase 1):** Application-level polling (`next_run_at` 기반) <br> - **Message Broker (Phase 2):** Redis (local Docker) + FastStream (권장: Redis Streams + Consumer Group) <br> - **Cron Parsing:** `croniter` (Python) <br> - **Storage:** Supabase Storage <br> - **Rule Generation:** High-performance LLM (e.g., Gemini) <br> - **Rule Execution:** Cost-efficient or Local LLM <br> - **Data Source (PoC):** `yfinance` |
| NFR-02 | 인프라 | - 모든 애플리케이션은 **Docker 컨테이너**로 패키징 및 실행되어야 한다. <br> - DB는 호스팅된 Supabase를 사용하고, 백엔드 Docker 컨테이너는 로컬 머신에서 실행하는 것을 가정한다. <br> - **(Phase 2)** 이벤트 기반 태스크/이벤트 모듈을 위해 로컬 Docker로 Redis 브로커를 함께 구동한다. |
| NFR-03 | 소스코드 관리 | - **룰 (데이터):** Supabase DB에 저장 <br> - **룰 실행 스크립트 (코드):** 사용자가 관리하는 GitHub 리포지토리에 저장 및 버전 관리 |
| NFR-04 | 확장성 | 룰의 종류나 데이터 소스가 추가되더라도 유연하게 확장할 수 있는 구조를 지향한다. (Skill 화) |
| NFR-05 | 환경 분리 | - **룰 개발 환경:** 사용자가 룰 스크립트를 개발하는 환경. 플랫폼은 이 과정을 지원하기 위한 보조 도구(e.g. LLM Skill)를 제공. <br> - **룰 실행 환경:** FastAPI/Docker 기반으로, 원격 DB 및 Git 리포지토리의 룰과 스크립트를 가져와 실행하는 런타임. |

### 6.1. 데이터 보존 및 삭제 (Data Retention and Deletion)

- **Supabase Storage (결과물 파일):**
    - Supabase Storage는 자동 객체 수명 주기 관리(automatic object lifecycle management) 기능을 기본으로 제공하지 않는다.
    - 일정 기간이 지난 결과물 파일의 자동 삭제를 위해서는 별도의 스크립트(예: Supabase Edge Function 또는 FastAPI 백엔드에서 주기적으로 실행되는 스크립트)를 구현하여 Supabase Storage API의 `remove` 메서드를 호출해야 한다.
    - `storage.objects` 테이블에 적절한 RLS(Row Level Security) 정책이 설정되어 있어야 한다.
- **Supabase PostgreSQL (DB 레코드):**
    - 특정 기간(예: 30일)이 지난 `rule_executions` 테이블의 레코드와 같이 오래된 데이터를 주기적으로 삭제한다.
    - FastAPI 백엔드에서 주기적으로 실행되는 정리 태스크(예: 매일 1회 tick 시 오래된 레코드 삭제)를 통해 처리한다.
    - 또는 Supabase Edge Function을 활용하여 서버리스 방식으로 처리할 수도 있다.

## 7. 가정 및 제약사항 (Assumptions and Constraints)

- **`yfinance`의 한계 인지:** `yfinance`는 비공식 스크래핑 기반으로, 불안정하거나 IP가 차단될 수 있음을 인지한다. PoC 단계에서는 이를 감수하고 사용하되, 향후 안정적인 API(예: Alpha Vantage)로 전환을 고려한다.
- **로컬 실행 환경:** 초기 운영은 사용자가 개인 로컬 머신에서 Docker 컨테이너를 직접 실행하는 것을 가정한다. (예: 출근 후 Docker 실행)
- **GitHub 관리:** 룰 실행 스크립트가 저장될 GitHub 리포지토리는 사용자가 직접 생성하고 관리한다.

## 8. 향후 발전 방향 (Future Roadmap)

본 프로젝트의 핵심 기능이 안정화된 이후, 다음과 같은 기능 확장을 통해 고도화된 개인 자동화 플랫폼으로 발전시키는 것을 목표로 한다.

### 8.1. 태스크/이벤트 관리 시스템 구축

- **모듈 비전:** 정기적인 룰 실행을 넘어, 일회성 작업, 사람의 개입(승인/리뷰), 외부 AI 에이전트 연동 등을 포괄하는 시스템의 중앙 허브 역할을 수행하는 '태스크/이벤트 관리 모듈'을 구축한다.
- **서비스 간 통신 아키텍처:** 서비스 간 결합도를 낮추고 유연한 확장을 위해 **이벤트 주도 아키텍처**를 채택한다. 각 서비스(프로듀서)는 단순히 이벤트를 발행하고, 다른 서비스(컨슈머)는 이벤트를 구독하여 독립적으로 처리한다.
    - **Phase 2 초기:** 로컬 Docker 환경에서 **Redis를 메시지 브로커**로 사용하여 이벤트 Pub/Sub를 구현한다.
        - 권장: **Redis Streams + Consumer Group** 기반으로 백로그/재처리/수평 확장(여러 컨슈머)을 가능하게 설계한다.
        - **전달/처리 보장(최소 계약):** 기본은 **at-least-once** 전달로 가정하며, 컨슈머는 `event_id`를 기준으로 **멱등성(idempotency)** 을 보장해야 한다.
        - 구현 예: FastStream 기반 Producer/Consumer
    - **필요 시 확장:** 처리량/요구사항 증가 시 Kafka/RabbitMQ 등 전용 메시지 브로커를 검토한다.
    - **비고:** DB 테이블 폴링 기반 이벤트 큐 구현은 운영/구현 복잡도가 높아 초기 범위에서 제외한다.
