# hub-ui

JobRunner Hub의 프론트엔드 UI 모듈입니다.

## 기술 스택 (Tech Stack)

이 프로젝트는 다음의 주요 기술들을 사용합니다:

- **Framework**: [React](https://react.dev/) (v19)
- **Language**: [TypeScript](https://www.typescriptlang.org/)
- **Build Tool**: [Vite](https://vitejs.dev/)
- **State Management**: [Zustand](https://github.com/pmndrs/zustand)
- **Routing**: [React Router](https://reactrouter.com/) (v7)
- **Data Fetching**: [TanStack Query](https://tanstack.com/query/latest) (React Query)
- **Styling**: [Tailwind CSS](https://tailwindcss.com/) (v4)
- **UI Components**: [shadcn/ui](https://ui.shadcn.com/) (UI Component Library)
- **API Client**: [openapi-typescript-codegen](https://github.com/ferdikoomen/openapi-typescript-codegen) (OpenAPI 기반 클라이언트 생성)

## 디렉토리 구조 (Directory Structure)

```
hub-ui/src/
├── api/                 # 커스텀 API 유틸리티 및 훅
├── app/                 # 앱 전역 설정 및 프로바이더
├── assets/              # 정적 에셋 (이미지, 폰트 등)
├── components/          # 공통 UI 컴포넌트
│   └── ui/              # shadcn/ui 컴포넌트 모음
├── config/              # 앱 설정 (상수, 환경변수 래퍼 등)
├── generated/           # 자동 생성된 코드
│   └── api/             # OpenAPI 기반 API 클라이언트
├── lib/                 # 외부 라이브러리 설정 및 유틸리티 (utils.ts 등)
├── stores/              # 전역 상태 관리 (Zustand)
├── utils/               # 일반 유틸리티 함수
├── views/               # 페이지/뷰 컴포넌트 (라우트 단위)
├── App.tsx              # 메인 앱 컴포넌트 및 라우팅 설정
└── main.tsx             # 앱 진입점 (Entry Point)
```

## 시작하기 (Getting Started)

### 의존성 설치 (Install Dependencies)

```bash
npm install
```

### 개발 서버 실행 (Run Development Server)

```bash
npm run dev
```

### API 클라이언트 생성 (Generate API Client)

백엔드 서버(JobRunner Hub)가 실행 중이어야 합니다 (`http://localhost:8389` 또는 `VITE_API_BASE_URL` 환경변수 참조).

```bash
npm run gen:api
```

### 빌드 (Build)

```bash
npm run build
```

### 린트 (Lint)

```bash
npm run lint
```

## 프로젝트 설정 (Project Settings)

- **Alias**: `@`는 `src` 디렉토리를 가리킵니다. (설정: `vite.config.ts`, `tsconfig.app.json`)
- **Tailwind CSS**: v4 버전이 적용되어 있으며, `vite.config.ts` 및 CSS 파일에서 설정됩니다.