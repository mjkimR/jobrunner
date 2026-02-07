"""
Dagster Client - Dagster GraphQL API 연동

jr CLI에서 Dagster와 통신하기 위한 클라이언트.
"""

import os

import httpx


class DagsterClient:
    """Dagster GraphQL API 클라이언트"""

    def __init__(self, host: str | None = None, port: int | None = None):
        self.host = host or os.getenv("DAGSTER_WEBSERVER_HOST", "localhost")
        self.port = port or int(os.getenv("DAGSTER_WEBSERVER_PORT", "3000"))
        self.base_url = f"http://{self.host}:{self.port}"
        self.graphql_url = f"{self.base_url}/graphql"

    def health_check(self) -> dict:
        """Dagster 서버 상태 확인"""
        try:
            response = httpx.get(f"{self.base_url}/server_info", timeout=5.0)
            response.raise_for_status()
            return {"status": "healthy", "url": self.base_url}
        except httpx.RequestError as e:
            return {"status": "unreachable", "error": str(e), "url": self.base_url}
        except httpx.HTTPStatusError as e:
            return {"status": "error", "error": str(e), "url": self.base_url}

    def get_assets(self) -> dict:
        """등록된 모든 Asset 목록 조회"""
        query = """
        query AssetsQuery {
            assetsOrError {
                ... on AssetConnection {
                    nodes {
                        key {
                            path
                        }
                    }
                }
            }
        }
        """
        return self._execute_query(query)

    def materialize_asset(self, asset_key: str) -> dict:
        """Asset을 materialize (실행)"""
        query = """
        mutation MaterializeAsset($assetKeys: [AssetKeyInput!]!) {
            launchPipelineExecution(
                executionParams: {
                    selector: {
                        repositoryLocationName: "__repository__"
                        repositoryName: "__repository__"
                        assetSelection: $assetKeys
                    }
                    mode: "default"
                }
            ) {
                __typename
                ... on LaunchRunSuccess {
                    run {
                        runId
                        status
                    }
                }
                ... on PythonError {
                    message
                    stack
                }
                ... on RunConfigValidationInvalid {
                    errors {
                        message
                    }
                }
            }
        }
        """
        variables = {"assetKeys": [{"path": [asset_key]}]}
        return self._execute_query(query, variables)

    def get_runs(self, limit: int = 10) -> dict:
        """최근 실행 이력 조회"""
        query = """
        query RunsQuery($limit: Int!) {
            runsOrError(limit: $limit) {
                ... on Runs {
                    results {
                        runId
                        status
                        startTime
                        endTime
                        jobName
                    }
                }
            }
        }
        """
        return self._execute_query(query, {"limit": limit})

    def _execute_query(self, query: str, variables: dict | None = None) -> dict:
        """GraphQL 쿼리 실행"""
        try:
            payload: dict[str, str | dict] = {"query": query}
            if variables:
                payload["variables"] = variables

            response = httpx.post(
                self.graphql_url,
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=30.0,
            )
            response.raise_for_status()
            return response.json()
        except httpx.RequestError as e:
            return {"error": f"Request failed: {e}"}
        except httpx.HTTPStatusError as e:
            return {"error": f"HTTP error: {e}"}


# Singleton instance
_client: DagsterClient | None = None


def get_client() -> DagsterClient:
    """DagsterClient 싱글톤 인스턴스 반환"""
    global _client
    if _client is None:
        _client = DagsterClient()
    return _client
