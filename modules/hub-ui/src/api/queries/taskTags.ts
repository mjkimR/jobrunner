import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { TaskTagService } from '@/generated/api'
import { queryKeys } from '../queryKeys'
import type { TaskTagCreate } from '@/generated/api/models/TaskTagCreate'
import type { TaskTagUpdate } from '@/generated/api/models/TaskTagUpdate'

export function useTaskTagsQuery(params: { offset?: number; limit?: number } = {}) {
    const { offset, limit } = params

    return useQuery({
        queryKey: queryKeys.taskTags.list({ offset, limit }),
        queryFn: () => TaskTagService.getTaskTagsApiV1TaskTagsGet(offset, limit ?? 100),
    })
}

export function useCreateTaskTagMutation() {
    const queryClient = useQueryClient()
    return useMutation({
        mutationFn: (data: TaskTagCreate) => TaskTagService.createTaskTagApiV1TaskTagsPost(data),
        onSuccess: () => {
            queryClient.invalidateQueries({ queryKey: queryKeys.taskTags.all })
        },
    })
}

export function useUpdateTaskTagMutation(tagId: string) {
    const queryClient = useQueryClient()
    return useMutation({
        mutationFn: (data: TaskTagUpdate) =>
            TaskTagService.updateTaskTagApiV1TaskTagsTaskTagIdPut(tagId, data),
        onSuccess: () => {
            queryClient.invalidateQueries({ queryKey: queryKeys.taskTags.all })
        },
    })
}

export function useDeleteTaskTagMutation() {
    const queryClient = useQueryClient()
    return useMutation({
        mutationFn: (tagId: string) => TaskTagService.deleteTaskTagApiV1TaskTagsTaskTagIdDelete(tagId),
        onSuccess: () => {
            queryClient.invalidateQueries({ queryKey: queryKeys.taskTags.all })
        },
    })
}
