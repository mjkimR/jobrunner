export const queryKeys = {
  health: ['health'] as const,
  workspaces: {
    all: ['workspaces'] as const,
    list: (params: { offset?: number; limit?: number } = {}) =>
      ['workspaces', 'list', params] as const,
    detail: (id: string) => ['workspaces', 'detail', id] as const,
  },
  tasks: {
    all: ['tasks'] as const,
    list: (workspaceId: string, params: { offset?: number; limit?: number } = {}) =>
      ['workspaces', workspaceId, 'tasks', 'list', params] as const,
    detail: (workspaceId: string, id: string) => ['workspaces', workspaceId, 'tasks', 'detail', id] as const,
  },
  taskTags: {
    all: ['taskTags'] as const,
    list: (workspaceId: string, params: { offset?: number; limit?: number } = {}) =>
      ['workspaces', workspaceId, 'taskTags', 'list', params] as const,
    detail: (workspaceId: string, id: string) => ['workspaces', workspaceId, 'taskTags', 'detail', id] as const,
  },
  taskHistory: {
    all: ['taskHistory'] as const,
    list: (workspaceId: string, params: { offset?: number; limit?: number } = {}) =>
      ['workspaces', workspaceId, 'taskHistory', 'list', params] as const,
    detail: (workspaceId: string, id: string) => ['workspaces', workspaceId, 'taskHistory', 'detail', id] as const,
  },
  configuredAgents: {
    all: ['configuredAgents'] as const,
    list: (params: { offset?: number; limit?: number } = {}) =>
      ['configuredAgents', 'list', params] as const,
    detail: (id: string) => ['configuredAgents', 'detail', id] as const,
  },
  conversations: {
    all: ['conversations'] as const,
    list: (workspaceId: string, params: { offset?: number; limit?: number } = {}) =>
      ['workspaces', workspaceId, 'conversations', 'list', params] as const,
    detail: (workspaceId: string, id: string) => ['workspaces', workspaceId, 'conversations', 'detail', id] as const,
  },
  chatMessages: {
    all: ['chatMessages'] as const,
    list: (workspaceId: string, conversationId: string, params: { offset?: number; limit?: number } = {}) =>
      ['workspaces', workspaceId, 'conversations', conversationId, 'chatMessages', 'list', params] as const,
  },
  routingLogs: {
    all: ['routingLogs'] as const,
    list: (params: { offset?: number; limit?: number } = {}) =>
      ['routingLogs', 'list', params] as const,
  },
}
