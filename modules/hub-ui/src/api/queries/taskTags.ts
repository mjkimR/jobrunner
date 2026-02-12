import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { TaskTagService } from '@/generated/api'
import { queryKeys } from '../queryKeys'
import type { TaskTagCreate } from '@/generated/api/models/TaskTagCreate'
import type { TaskTagUpdate } from '@/generated/api/models/TaskTagUpdate'

export const useTaskTagsQuery = (workspaceId: string, params: { offset?: number; limit?: number } = {}) => {
  return useQuery({
    queryKey: queryKeys.taskTags.list(workspaceId, params),
    queryFn: () => TaskTagService.getTaskTagsApiV1WorkspacesWorkspaceIdTaskTagsGet(
        workspaceId,
        params.offset,
        params.limit,
    ),
    enabled: !!workspaceId,
  });
};

export const useCreateTaskTagMutation = (workspaceId: string) => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (data: TaskTagCreate) => TaskTagService.createTaskTagApiV1WorkspacesWorkspaceIdTaskTagsPost(workspaceId, data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: queryKeys.taskTags.list(workspaceId) });
    },
  });
};

export const useUpdateTaskTagMutation = (workspaceId: string) => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: ({ tagId, data }: { tagId: string; data: TaskTagUpdate }) =>
      TaskTagService.updateTaskTagApiV1WorkspacesWorkspaceIdTaskTagsTaskTagIdPut(workspaceId, tagId, data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: queryKeys.taskTags.list(workspaceId) });
    },
  });
};

export const useDeleteTaskTagMutation = (workspaceId: string) => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (tagId: string) => TaskTagService.deleteTaskTagApiV1WorkspacesWorkspaceIdTaskTagsTaskTagIdDelete(workspaceId, tagId),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: queryKeys.taskTags.list(workspaceId) });
    },
  });
};
