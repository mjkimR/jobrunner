---
description: jr CLI 사용법 - JobRunner 시스템 제어 도구
---

# jr CLI SKILL

Host Agent가 JobRunner 시스템을 제어할 때 사용하는 CLI 도구입니다.

## 설치 확인

```bash
jr --version
```

## 주요 명령어

### 1. Job 생성 (plan)

자연어 설명을 기반으로 Dagster Job 코드를 생성합니다.

```bash
# 기본 사용
jr plan <job_name> -d "설명"

# 스케줄 포함
jr plan daily_stock_alert -d "매일 아침 9시 주가 알림" -s "0 9 * * *"

# 템플릿 지정
jr plan my_job -d "설명" -t asset     # 기본 Asset
jr plan my_job -d "설명" -t schedule  # 스케줄 포함
```

**workflow:**
1. `jr plan` 실행 → 코드 생성
2. 생성된 코드 리뷰
3. 승인 시 `src/jobs/` 디렉토리에 저장
4. Dagster가 자동으로 새 Job 감지

### 2. Job 실행 (run)

등록된 Job을 수동으로 실행합니다.

```bash
# Job 실행
jr run <job_name>

# 실행 시뮬레이션 (dry-run)
jr run <job_name> --dry-run
```

### 3. 상태 확인 (status)

시스템과 등록된 Job 상태를 확인합니다.

```bash
jr status
jr status --jobs
```

### 4. Job 목록 (list)

등록된 모든 Job을 나열합니다.

```bash
jr list
```

## 디렉토리 구조

```
src/
├── jobs/           # 생성된 Job 코드 저장
├── templates/      # 코드 생성 템플릿
├── cli/            # jr CLI 구현체
└── definitions.py  # Dagster 진입점
```

## 일반적인 워크플로우

1. **새 Job 생성**
   ```bash
   jr plan daily_report -d "매일 아침 데일리 리포트 생성" -s "0 8 * * *"
   ```

2. **코드 리뷰 및 승인** (CLI에서 Y/N 선택)

3. **Job 확인**
   ```bash
   jr list
   jr status
   ```

4. **필요시 수동 실행**
   ```bash
   jr run daily_report
   ```
