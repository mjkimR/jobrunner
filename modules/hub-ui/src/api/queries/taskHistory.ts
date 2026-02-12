import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { TaskHistoriesService } from '@/generated/api'
import { queryKeys } from '../queryKeys'

export function useTaskHistoryListQuery(workspaceId: string, params: { offset?: number; limit?: number } = {}) {
    const { offset, limit } = params

    return useQuery({
        queryKey: queryKeys.taskHistory.list(workspaceId, { offset, limit }),
        queryFn: () => TaskHistoriesService.getTaskHistoriesApiV1WorkspacesWorkspaceIdTaskHistoriesGet(workspaceId, offset, limit ?? 100),
        enabled: !!workspaceId,
    })
}




export function useDeleteTaskHistoryMutation(workspaceId: string) {
    const queryClient = useQueryClient()
    return useMutation({
        mutationFn: (historyId: string) =>
            TaskHistoriesService.deleteTaskHistoryApiV1WorkspacesWorkspaceIdTaskHistoriesTaskHistoryIdDelete(workspaceId, historyId),
        onSuccess: () => {
            queryClient.invalidateQueries({ queryKey: queryKeys.taskHistory.list(workspaceId) })
        },
    })
}
