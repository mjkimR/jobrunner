import { useQuery } from '@tanstack/react-query';
import { ChatMessageService } from '../../generated/api/services/ChatMessageService';
import { queryKeys } from '../queryKeys';

export const useChatMessagesQuery = (conversationId: string, params: { offset?: number; limit?: number } = {}) => {
  return useQuery({
    queryKey: queryKeys.chatMessages.list(conversationId, params),
    queryFn: () => ChatMessageService.getChatMessagesApiV1ChatMessagesGet(
        params.offset,
        params.limit,
    ),
    enabled: !!conversationId,
  });
};
