import { useQuery } from '@tanstack/react-query';
import { ConversationService } from '../../generated/api/services/ConversationService';
import { queryKeys } from '../queryKeys';

export const useConversationsQuery = (params: { offset?: number; limit?: number } = {}) => {
  return useQuery({
    queryKey: queryKeys.conversations.list(params),
    queryFn: () => ConversationService.getConversationsApiV1ConversationsGet(
        params.offset,
        params.limit,
    ),
  });
};

export const useConversationQuery = (id: string, enabled = true) => {
  return useQuery({
    queryKey: queryKeys.conversations.detail(id),
    queryFn: () => ConversationService.getConversationApiV1ConversationsConversationIdGet(id),
    enabled: !!id && enabled,
  });
};
