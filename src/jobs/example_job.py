"""
Example Job - 시스템 동작 확인용 샘플

이 파일은 jr CLI와 Dagster 연동을 테스트하기 위한 예제입니다.
"""

from dagster import AssetExecutionContext, asset


@asset(
    description="Hello World 테스트 Asset",
    group_name="examples",
)
def hello_world(context: AssetExecutionContext):
    """
    간단한 Hello World Asset.
    시스템이 정상 동작하는지 확인할 때 사용합니다.
    """
    context.log.info("Hello from JobRunner!")

    result = {
        "status": "success",
        "message": "JobRunner is working correctly!",
    }

    context.log.info(f"Result: {result}")
    return result
