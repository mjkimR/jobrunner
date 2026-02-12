import { useQuery } from '@tanstack/react-query';
import { ChatMessageService } from '../../generated/api/services/ChatMessageService';
import { queryKeys } from '../queryKeys';

export const useChatMessagesQuery = (workspaceId: string, conversationId: string, params: { offset?: number; limit?: number } = {}) => {
  return useQuery({
    queryKey: queryKeys.chatMessages.list(workspaceId, conversationId, params),
    queryFn: () => ChatMessageService.getChatMessagesApiV1WorkspacesWorkspaceIdConversationsConversationIdChatMessagesGet(
        workspaceId,
        conversationId,
        params.offset,
        params.limit,
    ),
    enabled: !!workspaceId && !!conversationId,
  });
};
