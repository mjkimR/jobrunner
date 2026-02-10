import { useQuery } from '@tanstack/react-query';
import { ConfiguredAgentService } from '../../generated/api/services/ConfiguredAgentService';
import { queryKeys } from '../queryKeys';

export const useConfiguredAgentsQuery = (params: { offset?: number; limit?: number } = {}) => {
  return useQuery({
    queryKey: queryKeys.configuredAgents.list(params),
    queryFn: () => ConfiguredAgentService.getConfiguredAgentsApiV1ConfiguredAgentsGet(
        params.offset,
        params.limit,
    ),
  });
};

export const useConfiguredAgentQuery = (id: string, enabled = true) => {
  return useQuery({
    queryKey: queryKeys.configuredAgents.detail(id),
    queryFn: () => ConfiguredAgentService.getConfiguredAgentApiV1ConfiguredAgentsConfiguredAgentIdGet(id),
    enabled: !!id && enabled,
  });
};
