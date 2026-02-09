import { QueryClient } from '@tanstack/react-query'

export function createQueryClient() {
  return new QueryClient({
    defaultOptions: {
      queries: {
        // 기본값은 팀/서비스 성격에 따라 조정하면 됩니다.
        // 너무 짧으면 불필요한 재요청이 늘고, 너무 길면 신선도가 떨어질 수 있어요.
        staleTime: 30_000,
        gcTime: 5 * 60_000,
        retry: 1,
        refetchOnWindowFocus: false,
      },
    },
  })
}
