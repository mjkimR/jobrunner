import { useQuery } from '@tanstack/react-query';
import { RoutingLogService } from '../../generated/api/services/RoutingLogService';
import { queryKeys } from '../queryKeys';

export const useRoutingLogsQuery = (params: { offset?: number; limit?: number } = {}) => {
  return useQuery({
    queryKey: queryKeys.routingLogs.list(params),
    queryFn: () => RoutingLogService.getRoutingLogsApiV1RoutingLogsGet(
        params.offset,
        params.limit,
    ),
  });
};
