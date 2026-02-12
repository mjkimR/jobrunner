import { useQueryClient } from '@tanstack/react-query'
import { useTasksQuery } from '../api/queries/tasks'
import { useWorkspacesQuery } from '../api/queries/workspaces'
import { queryKeys } from '../api/queryKeys'
import { useUiStore } from '../stores/uiStore'
import { useParams, useNavigate } from 'react-router-dom'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { useEffect } from 'react'

export default function HomeView() {
  const queryClient = useQueryClient()
  const { workspaceId } = useParams<{ workspaceId: string }>();
  const navigate = useNavigate();
  const lastRefreshAt = useUiStore((s) => s.lastRefreshAt)
  const setLastRefreshAt = useUiStore((s) => s.setLastRefreshAt)

  const { data: workspacesData } = useWorkspacesQuery()
  const workspaces = workspacesData?.items ?? []

  // Redirect to default workspace if at root
  useEffect(() => {
    if (!workspaceId && workspaces.length > 0) {
        const defaultWorkspace = workspaces.find(w => w.is_default) ?? workspaces[0];
        if (defaultWorkspace) {
            navigate(`/workspaces/${defaultWorkspace.id}/tasks`, { replace: true })
        }
    }
  }, [workspaceId, workspaces, navigate])

  const tasksQuery = useTasksQuery(workspaceId!, { offset: 0, limit: 20 })

  const onRefresh = async () => {
    if (!workspaceId) return;
    await queryClient.invalidateQueries({ queryKey: queryKeys.tasks.list(workspaceId) })
    setLastRefreshAt(new Date())
  }

  if (!workspaceId) {
    return (
      <div className="flex items-center justify-center h-full">
          <Card className="w-full max-w-md text-center">
              <CardHeader>
                  <CardTitle>Welcome to JobRunner Hub</CardTitle>
                  <CardDescription>
                      Please select a workspace from the sidebar to get started.
                  </CardDescription>
              </CardHeader>
          </Card>
      </div>
    )
  }

  return (
    <div className="grid gap-4">
      <div className="flex items-center justify-between">
        <h1 className="text-3xl font-bold">Dashboard</h1>
        <div className="flex items-center gap-2">
          <Button onClick={onRefresh} type="button" variant="outline" size="sm">
            Refresh Tasks
          </Button>
          <p className="text-xs text-muted-foreground">
            Last refresh: {lastRefreshAt ? lastRefreshAt.toLocaleString() : '—'}
          </p>
        </div>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Task Summary</CardTitle>
          <CardDescription>A brief overview of tasks in this workspace.</CardDescription>
        </CardHeader>
        <CardContent>
          {tasksQuery.isLoading && <div>Loading…</div>}
          {tasksQuery.isError && (
            <div>Failed: {(tasksQuery.error as Error).message}</div>
          )}
          {tasksQuery.data && (
            <pre className="p-4 rounded-md bg-muted text-sm overflow-x-auto">
              {JSON.stringify(
                {
                  total_count: tasksQuery.data.total_count,
                  offset: tasksQuery.data.offset,
                  limit: tasksQuery.data.limit,
                  items_in_page: tasksQuery.data.items.length,
                },
                null,
                2,
              )}
            </pre>
          )}
        </CardContent>
      </Card>
    </div>
  )
}
