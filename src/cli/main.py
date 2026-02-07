"""
jr CLI - Host Agent용 JobRunner 제어 인터페이스

주요 명령:
- jr plan: 자연어 → Dagster 코드 생성
- jr run: Job 수동 실행
- jr status: 시스템 상태 확인
"""

from pathlib import Path

import click

JOBS_DIR = Path(__file__).parent.parent / "jobs"
TEMPLATES_DIR = Path(__file__).parent.parent / "templates"


@click.group()
@click.version_option(version="0.1.0", prog_name="jr")
def cli():
    """JobRunner CLI - Host Agent용 시스템 제어 도구"""
    pass


@cli.command()
@click.argument("job_name")
@click.option("--description", "-d", help="Job에 대한 자연어 설명")
@click.option("--schedule", "-s", help="Cron 스케줄 표현식 (예: '0 9 * * *')")
@click.option(
    "--template", "-t", default="asset", help="사용할 템플릿 (asset, sensor, schedule)"
)
def plan(job_name: str, description: str | None, schedule: str | None, template: str):
    """
    새로운 Job 코드를 생성합니다.

    예시:
        jr plan daily_stock_alert -d "매일 아침 9시 주가 알림" -s "0 9 * * *"
    """
    click.echo(f"📋 Planning job: {job_name}")

    if description:
        click.echo(f"   Description: {description}")
    if schedule:
        click.echo(f"   Schedule: {schedule}")

    # 템플릿 기반 코드 생성
    job_file = JOBS_DIR / f"{job_name}.py"

    if job_file.exists():
        click.echo(f"⚠️  Job file already exists: {job_file}")
        if not click.confirm("Overwrite?"):
            return

    code = _generate_job_code(job_name, description, schedule, template)

    click.echo("\n" + "=" * 60)
    click.echo("Generated Code:")
    click.echo("=" * 60)
    click.secho(code, fg="cyan")
    click.echo("=" * 60 + "\n")

    if click.confirm("이 코드를 저장하시겠습니까?"):
        JOBS_DIR.mkdir(parents=True, exist_ok=True)
        job_file.write_text(code, encoding="utf-8")
        click.secho(f"✅ Saved: {job_file}", fg="green")
    else:
        click.echo("❌ Cancelled")


@cli.command()
@click.argument("job_name")
@click.option("--dry-run", is_flag=True, help="실제 실행 없이 시뮬레이션")
def run(job_name: str, dry_run: bool):
    """
    Job을 수동으로 실행합니다.

    예시:
        jr run daily_stock_alert
        jr run my_job --dry-run
    """
    job_file = JOBS_DIR / f"{job_name}.py"

    if not job_file.exists():
        click.secho(f"❌ Job not found: {job_name}", fg="red")
        click.echo(f"   Expected path: {job_file}")
        return

    if dry_run:
        click.echo(f"🔍 [DRY RUN] Would execute: {job_name}")
        return

    click.echo(f"🚀 Triggering asset materialization: {job_name}")

    from cli.dagster_client import get_client

    client = get_client()

    # 서버 상태 확인
    health = client.health_check()
    if health["status"] != "healthy":
        click.secho(
            f"❌ Dagster server unreachable: {health.get('error', 'unknown')}", fg="red"
        )
        click.echo(f"   URL: {health['url']}")
        return

    # Asset Materialize 요청
    result = client.materialize_asset(job_name)

    if "error" in result:
        click.secho(f"❌ Failed: {result['error']}", fg="red")
    elif "data" in result:
        launch_result = result["data"].get("launchPipelineExecution", {})
        if launch_result.get("__typename") == "LaunchRunSuccess":
            run_info = launch_result.get("run", {})
            click.secho(
                f"✅ Run launched: {run_info.get('runId', 'unknown')}", fg="green"
            )
            click.echo(f"   Status: {run_info.get('status', 'unknown')}")
        else:
            click.secho(f"⚠️  Launch result: {launch_result}", fg="yellow")
    else:
        click.secho("✅ Request sent to Dagster", fg="green")


@cli.command()
@click.option("--jobs", "-j", is_flag=True, help="등록된 Job 목록 표시")
def status(jobs: bool):
    """
    시스템 상태를 확인합니다.

    예시:
        jr status
        jr status --jobs
    """
    from cli.dagster_client import get_client

    click.echo("📊 JobRunner Status")
    click.echo("-" * 40)

    # Dagster 연결 상태
    client = get_client()
    health = client.health_check()
    if health["status"] == "healthy":
        click.secho(f"✅ Dagster: Connected ({health['url']})", fg="green")
    else:
        click.secho(
            f"❌ Dagster: {health['status']} - {health.get('error', 'unknown')}",
            fg="red",
        )

    # Job 목록
    if jobs or True:  # 기본으로 jobs 표시
        click.echo("\n📁 Registered Jobs:")
        if JOBS_DIR.exists():
            job_files = list(JOBS_DIR.glob("*.py"))
            if job_files:
                for f in job_files:
                    if f.name != "__init__.py":
                        click.echo(f"   • {f.stem}")
            else:
                click.echo("   (no jobs registered)")
        else:
            click.echo("   (jobs directory not found)")


@cli.command("list")
def list_jobs():
    """등록된 모든 Job을 나열합니다."""
    if not JOBS_DIR.exists():
        click.echo("No jobs directory found.")
        return

    job_files = [f for f in JOBS_DIR.glob("*.py") if f.name != "__init__.py"]

    if not job_files:
        click.echo("No jobs registered yet.")
        return

    click.echo(f"📋 Registered Jobs ({len(job_files)}):")
    for f in sorted(job_files):
        click.echo(f"   • {f.stem}")


def _generate_job_code(
    job_name: str, description: str | None, schedule: str | None, template: str
) -> str:
    """템플릿 기반으로 Dagster Job 코드를 생성합니다."""

    desc = description or f"{job_name} job"

    if template == "asset":
        code = f'''"""
{desc}
"""

from dagster import asset, AssetExecutionContext


@asset(
    description="{desc}",
    group_name="jobs",
)
def {job_name}(context: AssetExecutionContext):
    """
    {desc}
    
    TODO: 실제 로직 구현
    """
    context.log.info("Starting {job_name}")
    
    # TODO: 작업 로직 구현
    result = {{"status": "success"}}
    
    context.log.info(f"Completed {job_name}: {{result}}")
    return result
'''
    elif template == "schedule" and schedule:
        code = f'''"""
{desc}
"""

from dagster import asset, AssetExecutionContext, ScheduleDefinition


@asset(
    description="{desc}",
    group_name="scheduled_jobs",
)
def {job_name}(context: AssetExecutionContext):
    """
    {desc}
    
    Schedule: {schedule}
    """
    context.log.info("Starting {job_name}")
    
    # TODO: 작업 로직 구현
    result = {{"status": "success"}}
    
    context.log.info(f"Completed {job_name}: {{result}}")
    return result


{job_name}_schedule = ScheduleDefinition(
    job=None,  # TODO: define_asset_job 연결
    cron_schedule="{schedule}",
    name="{job_name}_schedule",
)
'''
    else:
        code = f'''"""
{desc}
"""

from dagster import asset, AssetExecutionContext


@asset(
    description="{desc}",
    group_name="jobs",
)
def {job_name}(context: AssetExecutionContext):
    """
    {desc}
    """
    context.log.info("Starting {job_name}")
    
    # TODO: 작업 로직 구현
    
    return {{"status": "success"}}
'''

    return code


if __name__ == "__main__":
    cli()
