"""
JobRunner Dagster Definitions

이 파일은 Dagster의 진입점입니다.
src/jobs 디렉토리의 모든 Asset을 자동으로 로드합니다.
"""

import importlib
import sys
from pathlib import Path

from dagster import Definitions, load_assets_from_modules


def _load_job_modules():
    """jobs 디렉토리에서 모든 Python 모듈을 동적으로 로드합니다."""
    jobs_dir = Path(__file__).parent / "jobs"
    modules = []

    # Ensure src is in path
    src_path = str(Path(__file__).parent)
    if src_path not in sys.path:
        sys.path.insert(0, src_path)

    for py_file in jobs_dir.glob("*.py"):
        if py_file.name.startswith("_"):
            continue

        module_name = f"jobs.{py_file.stem}"
        try:
            module = importlib.import_module(module_name)
            modules.append(module)
        except Exception as e:
            print(f"Warning: Failed to load {module_name}: {e}")

    return modules


# jobs 디렉토리에서 모든 asset 로드
job_modules = _load_job_modules()
all_assets = load_assets_from_modules(job_modules) if job_modules else []

defs = Definitions(
    assets=all_assets,
)
