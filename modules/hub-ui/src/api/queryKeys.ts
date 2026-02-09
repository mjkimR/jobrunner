export const queryKeys = {
  health: ['health'] as const,
  tasks: {
    all: ['tasks'] as const,
    list: (params: { offset?: number; limit?: number } = {}) =>
      ['tasks', 'list', params] as const,
    detail: (id: string) => ['tasks', 'detail', id] as const,
  },
  taskTags: {
    all: ['taskTags'] as const,
    list: (params: { offset?: number; limit?: number } = {}) =>
      ['taskTags', 'list', params] as const,
    detail: (id: string) => ['taskTags', 'detail', id] as const,
  },
  taskHistory: {
    all: ['taskHistory'] as const,
    list: (params: { offset?: number; limit?: number } = {}) =>
      ['taskHistory', 'list', params] as const,
    detail: (id: string) => ['taskHistory', 'detail', id] as const,
  },
}
