import { create } from 'zustand'

type UiState = {
  lastRefreshAt: Date | null
  setLastRefreshAt: (at: Date) => void
  activeWorkspaceId: string | null
  setActiveWorkspaceId: (id: string | null) => void
}

export const useUiStore = create<UiState>((set) => ({
  lastRefreshAt: null,
  setLastRefreshAt: (at) => set({ lastRefreshAt: at }),
  activeWorkspaceId: null,
  setActiveWorkspaceId: (id) => set({ activeWorkspaceId: id }),
}))
