import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { TaskHistorieService, type TaskHistoryCreate, type TaskHistoryUpdate } from '@/generated/api'
import { queryKeys } from '../queryKeys'

export function useTaskHistoryListQuery(workspaceId: string, params: { offset?: number; limit?: number } = {}) {
    const { offset, limit } = params

    return useQuery({
        queryKey: queryKeys.taskHistory.list(workspaceId, { offset, limit }),
        queryFn: () => TaskHistorieService.getTaskHistoriesApiV1WorkspaceWorkspaceIdTaskHistoriesGet(workspaceId, offset, limit ?? 100),
        enabled: !!workspaceId,
    })
}

export function useCreateTaskHistoryMutation(workspaceId: string) {
    const queryClient = useQueryClient()
    return useMutation({
        mutationFn: (data: TaskHistoryCreate) => TaskHistorieService.createTaskHistoryApiV1WorkspaceWorkspaceIdTaskHistoriesPost(workspaceId, data),
        onSuccess: () => {
            queryClient.invalidateQueries({ queryKey: queryKeys.taskHistory.list(workspaceId) })
        },
    })
}

export function useUpdateTaskHistoryMutation(workspaceId: string, historyId: string) {
    const queryClient = useQueryClient()
    return useMutation({
        mutationFn: (data: TaskHistoryUpdate) => TaskHistorieService.updateTaskHistoryApiV1WorkspaceWorkspaceIdTaskHistoriesTaskHistoryIdPut(workspaceId, historyId, data),
        onSuccess: () => {
            queryClient.invalidateQueries({ queryKey: queryKeys.taskHistory.list(workspaceId) })
        },
    })
}


export function useDeleteTaskHistoryMutation(workspaceId: string) {
    const queryClient = useQueryClient()
    return useMutation({
        mutationFn: (historyId: string) =>
            TaskHistorieService.deleteTaskHistoryApiV1WorkspaceWorkspaceIdTaskHistoriesTaskHistoryIdDelete(workspaceId, historyId),
        onSuccess: () => {
            queryClient.invalidateQueries({ queryKey: queryKeys.taskHistory.list(workspaceId) })
        },
    })
}
