import { useQuery } from '@tanstack/react-query';
import { ConversationService } from '../../generated/api/services/ConversationService';
import { queryKeys } from '../queryKeys';

export const useConversationsQuery = (workspaceId: string, params: { offset?: number; limit?: number } = {}) => {
  return useQuery({
    queryKey: queryKeys.conversations.list(workspaceId, params),
    queryFn: () => ConversationService.getConversationsApiV1WorkspacesWorkspaceIdConversationsGet(
        workspaceId,
        params.offset,
        params.limit,
    ),
    enabled: !!workspaceId,
  });
};

export const useConversationQuery = (workspaceId: string, id: string, enabled = true) => {
  return useQuery({
    queryKey: queryKeys.conversations.detail(workspaceId, id),
    queryFn: () => ConversationService.getConversationApiV1WorkspacesWorkspaceIdConversationsConversationIdGet(workspaceId, id),
    enabled: !!workspaceId && !!id && enabled,
  });
};
