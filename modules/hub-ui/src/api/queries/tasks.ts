import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { TaskService } from '@/generated/api'
import { queryKeys } from '../queryKeys'
import type { TaskCreate } from '@/generated/api/models/TaskCreate'
import type { TaskUpdate } from '@/generated/api/models/TaskUpdate'

export function useTasksQuery(workspaceId: string, params: { offset?: number; limit?: number } = {}) {
  const { offset, limit } = params

  return useQuery({
    queryKey: queryKeys.tasks.list(workspaceId, { offset, limit }),
    queryFn: () => TaskService.getTasksApiV1WorkspaceWorkspaceIdTasksGet(workspaceId, offset, limit ?? 100),
    enabled: !!workspaceId,
  })
}

export function useCreateTaskMutation(workspaceId: string) {
    const queryClient = useQueryClient()
    return useMutation({
        mutationFn: (data: TaskCreate) => TaskService.createTaskApiV1WorkspaceWorkspaceIdTasksPost(workspaceId, data),
        onSuccess: () => {
            queryClient.invalidateQueries({ queryKey: queryKeys.tasks.list(workspaceId) })
        },
    })
}

export function useUpdateTaskMutation(workspaceId: string, taskId: string) {
    const queryClient = useQueryClient()
    return useMutation({
        mutationFn: (data: TaskUpdate) => TaskService.updateTaskApiV1WorkspaceWorkspaceIdTasksTaskIdPut(workspaceId, taskId, data),
        onSuccess: () => {
            queryClient.invalidateQueries({ queryKey: queryKeys.tasks.list(workspaceId) })
            queryClient.invalidateQueries({ queryKey: queryKeys.tasks.detail(workspaceId, taskId) })
        },
    })
}

export function useDeleteTaskMutation(workspaceId: string) {
  const queryClient = useQueryClient()
  return useMutation({
    mutationFn: (taskId: string) => TaskService.deleteTaskApiV1WorkspaceWorkspaceIdTasksTaskIdDelete(workspaceId, taskId),
    onSuccess: (_data, _taskId) => {
      queryClient.invalidateQueries({ queryKey: queryKeys.tasks.list(workspaceId) })
    },
  })
}
