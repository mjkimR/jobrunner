import { create } from 'zustand'

type UiState = {
  lastRefreshAt: Date | null
  setLastRefreshAt: (at: Date) => void
}

export const useUiStore = create<UiState>((set) => ({
  lastRefreshAt: null,
  setLastRefreshAt: (at) => set({ lastRefreshAt: at }),
}))
