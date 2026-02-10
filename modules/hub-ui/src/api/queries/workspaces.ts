import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { WorkspacesService } from '@/generated/api'
import { queryKeys } from '../queryKeys'
import type { WorkspaceCreate } from '@/generated/api/models/WorkspaceCreate'
import type { WorkspaceUpdate } from '@/generated/api/models/WorkspaceUpdate'

export function useWorkspacesQuery(params: { offset?: number; limit?: number } = {}) {
    const { offset, limit } = params

    return useQuery({
        queryKey: queryKeys.workspaces.list({ offset, limit }),
        queryFn: () => WorkspacesService.getWorkspacesApiV1WorkspacesGet(offset, limit ?? 100),
    })
}

export function useCreateWorkspaceMutation() {
    const queryClient = useQueryClient()
    return useMutation({
        mutationFn: (data: WorkspaceCreate) => WorkspacesService.createWorkspaceApiV1WorkspacesPost(data),
        onSuccess: () => {
            queryClient.invalidateQueries({ queryKey: queryKeys.workspaces.all })
        },
    })
}

export function useUpdateWorkspaceMutation(workspaceId: string) {
    const queryClient = useQueryClient()
    return useMutation({
        mutationFn: (data: WorkspaceUpdate) =>
            WorkspacesService.updateWorkspaceApiV1WorkspacesWorkspaceIdPut(workspaceId, data),
        onSuccess: (_data, variables) => {
            queryClient.invalidateQueries({ queryKey: queryKeys.workspaces.all })
            queryClient.invalidateQueries({ queryKey: queryKeys.workspaces.detail(workspaceId) })
        },
    })
}

export function useDeleteWorkspaceMutation() {
    const queryClient = useQueryClient()
    return useMutation({
        mutationFn: (workspaceId: string) => WorkspacesService.deleteWorkspaceApiV1WorkspacesWorkspaceIdDelete(workspaceId),
        onSuccess: () => {
            queryClient.invalidateQueries({ queryKey: queryKeys.workspaces.all })
        },
    })
}
