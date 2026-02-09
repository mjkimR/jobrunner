# Hub UI 개발 가이드 및 주의사항

이 문서는 `hub-ui` 모듈 개발 시 발생했던 이슈들과 해결 방법을 정리하여, 향후 개발 시 참조하기 위해 작성되었습니다.

## 1. OpenAPI Generator 관련 주의사항

### 서비스(Service) 클래스 명명 규칙 확인
OpenAPI Generator가 생성하는 서비스 클래스의 이름이 예상과 다를 수 있습니다.
- **예시**: `Tasks` 태그가 있는 API라도 `TasksService`가 아니라 `TaskService`로 생성될 수 있습니다. (단수/복수 혼동 주의)
- **해결**: `src/generated/api/services` 폴더를 직접 확인하여 정확한 클래스명을 import 해야 합니다.

### 페이지네이션 모델 속성 (`total` vs `total_count`)
생성된 페이지네이션 응답 모델(`PaginatedList_...`)의 속성명이 직관과 다를 수 있습니다.
- **이슈**: 보통 `total`로 예상하고 코드를 작성하기 쉬우나, 실제 생성된 모델은 `total_count` 필드를 가지고 있었습니다.
- **해결**: `src/generated/api/models/PaginatedList_*.ts` 파일을 열어 정확한 속성명을 확인하고 사용하세요. (예: `data.total_count`)

## 2. TypeScript 및 빌드 설정 주의사항

### Type-Only Imports (`verbatimModuleSyntax`)
`tsconfig.json` (또는 `tsconfig.app.json`)에 `verbatimModuleSyntax: true`가 설정되어 있어, 타입이나 인터페이스를 import 할 때는 반드시 `import type` 구문을 사용해야 합니다.
- **잘못된 예**: `import { ColumnDef } from "@tanstack/react-table"`
- **올바른 예**: `import type { ColumnDef } from "@tanstack/react-table"`
- **증상**: IDE에서는 에러가 없더라도 `npm run build` 시 에러가 발생할 수 있습니다. (예: `TS1484`)

### 미사용 변수 (Unused Variables)
프로젝트의 린트 및 빌드 설정이 엄격하여, 사용하지 않는 import 구문이나 변수가 남아있으면 빌드가 실패합니다.
- **예시**: `useToast` 훅을 import 했으나 코드 내에서 호출하지 않은 경우.
- **해결**: 사용하지 않는 코드는 과감히 삭제하거나 필요 시 주석 처리해야 합니다.

## 3. 폴더 구조 및 네이밍
- **Views**: 각 기능별 페이지는 `src/views/[feature]/` 아래에 구성했습니다. (예: `tasks`, `tags`, `history`)
- **Components**: 재사용 가능한 UI 컴포넌트는 `src/components/ui` (shadcn) 또는 `src/components` (커스텀)에 위치합니다.
- **API**: API 관련 쿼리/뮤테이션 훅은 `src/api/queries/`에 위치합니다.

## 4. API 연동 표준 (TanStack Query)

제너레이트된 API 서비스를 직접 컴포넌트에서 호출하지 않고, `src/api` 폴더에 래핑하여 사용합니다.

### 쿼리 키 중앙 관리 (`src/api/queryKeys.ts`)
- 모든 React Query의 키는 `queryKeys` 객체를 통해 관리합니다. 하드코딩된 문자열 배열 사용을 지양합니다.
- 예: `queryKey: queryKeys.tasks.list({ offset, limit })`

### 커스텀 훅 사용 (`src/api/queries/*.ts`)
- 제너레이트된 서비스(`TaskService` 등)는 `src/api/queries` 하위의 커스텀 훅(`useTasksQuery` 등)으로 한 번 감싸서 사용합니다.
- 뮤테이션(`Mutation`) 역시 커스텀 훅으로 정의하여 사용합니다.
- 이를 통해 캐시 무효화(`invalidateQueries`) 로직을 중앙에서 관리하고, 컴포넌트 코드를 간결하게 유지합니다.
