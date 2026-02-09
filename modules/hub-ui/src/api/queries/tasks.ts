import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { TaskService } from '@/generated/api'
import { queryKeys } from '../queryKeys'

export function useTasksQuery(params: { offset?: number; limit?: number } = {}) {
  const { offset, limit } = params

  return useQuery({
    queryKey: queryKeys.tasks.list({ offset, limit }),
    queryFn: () => TaskService.getTasksApiV1TasksGet(offset, limit ?? 100),
  })
}

export function useDeleteTaskMutation() {
  const queryClient = useQueryClient()
  return useMutation({
    mutationFn: (taskId: string) => TaskService.deleteTaskApiV1TasksTaskIdDelete(taskId),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: queryKeys.tasks.all })
    },
  })
}
