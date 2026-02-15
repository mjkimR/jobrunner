import os

from prefect import flow, task

# 로컬 서버(Docker)의 API 주소 설정
# docker-compose에서 4200 포트를 열어두었으므로 localhost:4200 사용
os.environ["PREFECT_API_URL"] = "http://127.0.0.1:4200/api"


@task(log_prints=True)
def print_platform_info():
    import platform

    print(f"Running on {platform.system()} {platform.release()}")


@flow(name="local-test-flow", log_prints=True)
def test_flow():
    print("Precet workflow is starting!")
    print_platform_info()
    print("Workflow completed successfully.")


if __name__ == "__main__":
    test_flow()
