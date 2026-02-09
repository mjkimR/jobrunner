import { useQueryClient } from '@tanstack/react-query'
import { useTasksQuery } from '../api/queries/tasks'
import { queryKeys } from '../api/queryKeys'
import { useUiStore } from '../stores/uiStore'

export default function HomeView() {
  const queryClient = useQueryClient()
  const lastRefreshAt = useUiStore((s) => s.lastRefreshAt)
  const setLastRefreshAt = useUiStore((s) => s.setLastRefreshAt)

  const tasksQuery = useTasksQuery({ offset: 0, limit: 20 })

  const onRefresh = async () => {
    await queryClient.invalidateQueries({ queryKey: queryKeys.tasks.all })
    setLastRefreshAt(new Date())
  }

  return (
    <section style={{ display: 'grid', gap: 12, maxWidth: 960 }}>
      <h1 style={{ margin: 0 }}>Home</h1>

      <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
        <button onClick={onRefresh} type="button">
          Refresh
        </button>
        <small>
          last refresh: {lastRefreshAt ? lastRefreshAt.toLocaleString() : '—'}
        </small>
      </div>

      <div
        style={{
          padding: 12,
          border: '1px solid #ddd',
          borderRadius: 8,
          background: '#fff',
          color: '#111',
        }}
      >
        {tasksQuery.isLoading && <div>Loading…</div>}
        {tasksQuery.isError && (
          <div>Failed: {(tasksQuery.error as Error).message}</div>
        )}
        {tasksQuery.data && (
          <pre style={{ margin: 0 }}>
            {JSON.stringify(
              {
                total_count: tasksQuery.data.total_count,
                offset: tasksQuery.data.offset,
                limit: tasksQuery.data.limit,
                first: tasksQuery.data.first,
                last: tasksQuery.data.last,
                items: tasksQuery.data.items,
              },
              null,
              2,
            )}
          </pre>
        )}
      </div>

      <small style={{ opacity: 0.7 }}>
        서버 상태(Task 목록)는 TanStack Query(+ OpenAPI codegen client), UI 전역 상태(lastRefreshAt)는 Zustand.
      </small>
    </section>
  )
}
