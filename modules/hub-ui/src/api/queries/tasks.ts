import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { TaskService } from '@/generated/api'
import { queryKeys } from '../queryKeys'
import type { TaskCreate } from '@/generated/api/models/TaskCreate'
import type { TaskUpdate } from '@/generated/api/models/TaskUpdate'

export function useTasksQuery(workspaceId: string, params: { offset?: number; limit?: number } = {}) {
  const { offset, limit } = params

  return useQuery({
    queryKey: queryKeys.tasks.list(workspaceId, { offset, limit }),
    queryFn: () => TaskService.getTasksApiV1WorkspacesWorkspaceIdTasksGet(workspaceId, offset, limit ?? 100),
    enabled: !!workspaceId,
  })
}

export function useCreateTaskMutation(workspaceId: string) {
    const queryClient = useQueryClient()
    return useMutation({
        mutationFn: (data: TaskCreate) => TaskService.createTaskApiV1WorkspacesWorkspaceIdTasksPost(workspaceId, data),
        onSuccess: () => {
            queryClient.invalidateQueries({ queryKey: queryKeys.tasks.list(workspaceId) })
        },
    })
}

export function useUpdateTaskMutation(workspaceId: string) {
    const queryClient = useQueryClient()
    return useMutation({
        mutationFn: ({ taskId, data }: { taskId: string; data: TaskUpdate }) =>
            TaskService.updateTaskApiV1WorkspacesWorkspaceIdTasksTaskIdPut(workspaceId, taskId, data),
        onSuccess: (data) => {
            queryClient.invalidateQueries({ queryKey: queryKeys.tasks.list(workspaceId) })
            queryClient.invalidateQueries({ queryKey: queryKeys.tasks.detail(workspaceId, data.id) })
        },
    })
}

export function useDeleteTaskMutation(workspaceId: string) {
  const queryClient = useQueryClient()
  return useMutation({
    mutationFn: (taskId: string) => TaskService.deleteTaskApiV1WorkspacesWorkspaceIdTasksTaskIdDelete(workspaceId, taskId),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: queryKeys.tasks.list(workspaceId) })
    },
  })
}
