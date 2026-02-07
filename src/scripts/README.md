# Rule Scripts Directory

이 디렉토리는 JobRunner에서 실행되는 룰 스크립트들을 저장합니다.

## 스크립트 작성 규약

### 데코레이터 패턴 (권장)

모든 룰 스크립트는 `@rule` 데코레이터를 사용하여 **async 함수**로 작성합니다:

```python
from scripts.registry import rule

@rule("my_rule", description="설명", tags=["category"])
async def my_rule(payload: dict) -> dict:
    """
    Args:
        payload: Rule에 정의된 payload (DB에서 전달)
    
    Returns:
        dict: 실행 결과
            - success: bool (필수)
            - message: str (선택)
            - data: any (선택)
    """
    # 비동기 작업 가능
    result = await some_async_operation()
    return {"success": True, "message": "완료"}
```

### 예제: Hello World

```python
# scripts/hello_world/main.py
from scripts.registry import rule

@rule("hello_world", description="Simple greeting", tags=["example"])
async def hello_world(payload: dict) -> dict:
    name = payload.get("name", "World")
    return {
        "success": True,
        "message": f"Hello, {name}!"
    }
```

## 디렉토리 구조

```
scripts/
├── __init__.py            # 패키지 초기화 (자동 등록)
├── registry.py            # RuleRegistry 및 @rule 데코레이터
├── hello_world/           # 예제 스크립트
│   ├── __init__.py
│   └── main.py
├── stock/                 # 주식 관련 (Phase 1 PoC 예정)
│   └── check_price.py
└── utils/                 # 공용 유틸리티
    └── __init__.py
```

## 새 룰 추가하기

1. 새 디렉토리 또는 파일 생성
2. `@rule("rule_name")` 데코레이터로 async 함수 정의
3. `scripts/__init__.py`에 import 추가

## DB 설정

Rule 생성 시 `execution_script_path`에 룰 이름을 지정:

```json
{
  "name": "Hello World",
  "schedule": "*/5 * * * *",
  "execution_script_path": "hello_world",
  "payload": {"name": "JobRunner"}
}
```

## Registry API

```python
from scripts.registry import rule_registry

# 등록된 룰 조회
handler = rule_registry.get("hello_world")
result = await handler({"name": "Test"})

# 모든 룰 목록
all_rules = rule_registry.list_rules()

# 메타데이터 포함 조회
definition = rule_registry.get_definition("hello_world")
print(definition.description, definition.tags)
```
