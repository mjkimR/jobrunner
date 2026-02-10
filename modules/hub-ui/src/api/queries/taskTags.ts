import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { TaskTagService } from '@/generated/api'
import { queryKeys } from '../queryKeys'
import type { TaskTagCreate } from '@/generated/api/models/TaskTagCreate'
import type { TaskTagUpdate } from '@/generated/api/models/TaskTagUpdate'

export function useTaskTagsQuery(workspaceId: string, params: { offset?: number; limit?: number } = {}) {
    const { offset, limit } = params

    return useQuery({
        queryKey: queryKeys.taskTags.list(workspaceId, { offset, limit }),
        queryFn: () => TaskTagService.getTaskTagsApiV1WorkspaceWorkspaceIdTaskTagsGet(workspaceId, offset, limit ?? 100),
        enabled: !!workspaceId,
    })
}

export function useCreateTaskTagMutation(workspaceId: string) {
    const queryClient = useQueryClient()
    return useMutation({
        mutationFn: (data: TaskTagCreate) => TaskTagService.createTaskTagApiV1WorkspaceWorkspaceIdTaskTagsPost(workspaceId, data),
        onSuccess: () => {
            queryClient.invalidateQueries({ queryKey: queryKeys.taskTags.list(workspaceId) })
        },
    })
}

export function useUpdateTaskTagMutation(workspaceId: string, tagId: string) {
    const queryClient = useQueryClient()
    return useMutation({
        mutationFn: (data: TaskTagUpdate) =>
            TaskTagService.updateTaskTagApiV1WorkspaceWorkspaceIdTaskTagsTaskTagIdPut(workspaceId, tagId, data),
        onSuccess: () => {
            queryClient.invalidateQueries({ queryKey: queryKeys.taskTags.list(workspaceId) })
        },
    })
}

export function useDeleteTaskTagMutation(workspaceId: string) {
    const queryClient = useQueryClient()
    return useMutation({
        mutationFn: (tagId: string) => TaskTagService.deleteTaskTagApiV1WorkspaceWorkspaceIdTaskTagsTaskTagIdDelete(workspaceId, tagId),
        onSuccess: () => {
            queryClient.invalidateQueries({ queryKey: queryKeys.taskTags.list(workspaceId) })
        },
    })
}
