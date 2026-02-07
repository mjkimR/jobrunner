"""Hello World 룰 스크립트 예제

가장 간단한 형태의 async 룰 스크립트입니다.
@rule() 데코레이터 사용 시 함수명이 자동으로 룰 이름이 됩니다.
"""

from scripts.registry import ExecutionContext, rule


@rule(tags=["example"])  # name='hello_world' (from __name__)
async def hello_world(
    payload: dict,
    context: ExecutionContext | None = None,
) -> dict:
    """Hello World 룰 실행

    Args:
        payload: Rule에 정의된 데이터
            - name: 인사할 대상 이름 (기본값: "World")
        context: 실행 컨텍스트 (chain 실행 시 이전 결과 포함)

    Returns:
        dict: 실행 결과
            - success: 성공 여부
            - message: 결과 메시지
    """
    name = payload.get("name", "World")
    message = f"Hello, {name}!"

    # Context 사용 예시 (chain에서 이전 결과 접근)
    if context and context.prev_results:
        prev_data = context.get_prev_result("fetch_data")
        if prev_data:
            message += f" (from chain, prev data: {prev_data})"

    print(f"[HelloWorld] {message}")

    return {
        "success": True,
        "message": message,
    }
