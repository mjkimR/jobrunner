import { useWorkspacesQuery } from "@/api/queries/workspaces"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { useUiStore } from "@/stores/uiStore"
import { useEffect } from "react"
import { useLocation, useNavigate, useParams } from "react-router-dom"
import { cn } from "@/lib/utils"

export function WorkspaceSelector({ className }: { className?: string }) {
    const { data: workspacesData } = useWorkspacesQuery()
    const activeWorkspaceId = useUiStore((s) => s.activeWorkspaceId)
    const setActiveWorkspaceId = useUiStore((s) => s.setActiveWorkspaceId)
    const navigate = useNavigate()
    const location = useLocation()
    const params = useParams()

    const workspaces = workspacesData?.items ?? []
    const currentWorkspaceId = params.workspaceId

    // Set active workspace from URL params
    useEffect(() => {
        if (currentWorkspaceId && currentWorkspaceId !== activeWorkspaceId) {
            setActiveWorkspaceId(currentWorkspaceId)
        }
    }, [currentWorkspaceId, activeWorkspaceId, setActiveWorkspaceId])

    const handleWorkspaceChange = (newWorkspaceId: string) => {
        if (currentWorkspaceId) {
            // Replace the workspaceId in the current path and navigate
            const newPath = location.pathname.replace(`/workspaces/${currentWorkspaceId}`, `/workspaces/${newWorkspaceId}`);
            navigate(newPath)
        } else {
            // If in global view, navigate to the selected workspace's tasks view
            navigate(`/workspaces/${newWorkspaceId}/tasks`)
        }
    }

    if (workspaces.length === 0) {
        return <div className="text-sm p-2 text-center">No workspaces.</div>
    }

    return (
        <Select onValueChange={handleWorkspaceChange} value={activeWorkspaceId ?? ''}>
            <SelectTrigger className={cn("w-full", className)}>
                <SelectValue placeholder="Select a workspace..." />
            </SelectTrigger>
            <SelectContent>
                {workspaces.map((workspace) => (
                    <SelectItem key={workspace.id} value={workspace.id}>
                        {workspace.name}
                    </SelectItem>
                ))}
            </SelectContent>
        </Select>
    )
}
