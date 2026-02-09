import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { TaskHistorieService } from '@/generated/api'
import { queryKeys } from '../queryKeys'

export function useTaskHistoryListQuery(params: { offset?: number; limit?: number } = {}) {
    const { offset, limit } = params

    return useQuery({
        queryKey: queryKeys.taskHistory.list({ offset, limit }),
        queryFn: () => TaskHistorieService.getTaskHistoriesApiV1TaskHistoriesGet(offset, limit ?? 100),
    })
}

export function useDeleteTaskHistoryMutation() {
    const queryClient = useQueryClient()
    return useMutation({
        mutationFn: (historyId: string) =>
            TaskHistorieService.deleteTaskHistoryApiV1TaskHistoriesTaskHistoryIdDelete(historyId),
        onSuccess: () => {
            queryClient.invalidateQueries({ queryKey: queryKeys.taskHistory.all })
        },
    })
}
