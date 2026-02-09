# hub-ui

Vite + React + TypeScript UI.

- Routing: `react-router-dom`
- Server state: TanStack Query
- UI/global state: Zustand (필요할 때만)
- API client: FastAPI OpenAPI → `openapi-typescript-codegen`로 생성

## 전제

- Node.js 22.12+ 권장 (Vite 7 요구사항)
- FastAPI 백엔드 실행 중 (기본: `http://localhost:8389`)

## 빠른 시작

```bash
cd modules/hub-ui
npm install
npm run dev
```

## 백엔드 URL 설정

환경변수 `VITE_API_BASE_URL`을 사용합니다.

```bash
cd modules/hub-ui
cp .env.example .env
```

`.env` 예시:

```dotenv
VITE_API_BASE_URL=http://localhost:8389
```

## OpenAPI client 생성

아래 명령은 OpenAPI 스펙을 다운로드한 다음 `src/generated/api`에 클라이언트를 생성합니다.

```bash
cd modules/hub-ui
npm run gen:api
```

## 생성한 client가 실제로 잘 붙었는지 확인(스모크 테스트)

1) FastAPI를 8389 포트로 실행
2) UI 실행

```bash
cd modules/hub-ui
npm run dev
```

3) Vite가 출력하는 URL(보통 `http://localhost:5173`)로 접속

Home 화면에서 `GET /api/v1/tasks` 응답 JSON이 표시되면 성공입니다.

- `Refresh` 버튼: TanStack Query 캐시 invalidate → refetch
- React Query Devtools: 포함되어 있습니다(화면 하단에 토글)

## 트러블슈팅

### CORS 에러

브라우저 콘솔에 CORS 에러가 뜨면 FastAPI CORS 설정에서 Vite dev origin을 허용하세요.

- `http://localhost:5173`