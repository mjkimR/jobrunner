export const queryKeys = {
  health: ['health'] as const,
  tasks: {
    all: ['tasks'] as const,
    list: (params: { offset?: number; limit?: number } = {}) =>
      ['tasks', 'list', params] as const,
    detail: (id: string) => ['tasks', 'detail', id] as const,
  },
}
