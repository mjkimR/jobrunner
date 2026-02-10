import type { ColumnDef } from "@tanstack/react-table"
import type { WorkspaceRead } from "@/generated/api"
import { MoreHorizontal, CheckCircle2, Circle } from "lucide-react"
import { Button } from "@/components/ui/button"
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuLabel,
    DropdownMenuSeparator,
    DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import { Badge } from "@/components/ui/badge"

export type WorkspaceColumnProps = {
    onEdit: (workspace: WorkspaceRead) => void;
    onDelete: (workspace: WorkspaceRead) => void;
}

export const getWorkspaceColumns = ({ onEdit, onDelete }: WorkspaceColumnProps): ColumnDef<WorkspaceRead>[] => [
    {
        accessorKey: "name",
        header: "Name",
        cell: ({ row }) => {
            return (
                <div className="flex flex-col">
                    <span className="font-medium">{row.original.name}</span>
                    <span className="text-xs text-muted-foreground font-mono">{row.original.alias}</span>
                </div>
            )
        }
    },
    {
        accessorKey: "description",
        header: "Description",
        cell: ({ row }) => <span className="text-muted-foreground text-sm">{row.original.description}</span>
    },
    {
        accessorKey: "is_default",
        header: "Default",
        cell: ({ row }) => {
            const isDefault = row.getValue("is_default");
            return (
                <Badge variant={isDefault ? "default" : "outline"} className="capitalize">
                    {isDefault ? <CheckCircle2 className="mr-1 h-3 w-3" /> : <Circle className="mr-1 h-3 w-3" />}
                    {isDefault ? "Yes" : "No"}
                </Badge>
            )
        }
    },
    {
        accessorKey: "created_at",
        header: "Created At",
        cell: ({ row }) => {
            return new Date(row.getValue("created_at")).toLocaleString()
        }
    },
    {
        id: "actions",
        cell: ({ row }) => {
            const workspace = row.original

            return (
                <DropdownMenu>
                    <DropdownMenuTrigger asChild>
                        <Button variant="ghost" className="h-8 w-8 p-0">
                            <span className="sr-only">Open menu</span>
                            <MoreHorizontal className="h-4 w-4" />
                        </Button>
                    </DropdownMenuTrigger>
                    <DropdownMenuContent align="end">
                        <DropdownMenuLabel>Actions</DropdownMenuLabel>
                        <DropdownMenuItem onClick={() => navigator.clipboard.writeText(workspace.id)}>
                            Copy ID
                        </DropdownMenuItem>
                        <DropdownMenuSeparator />
                        <DropdownMenuItem onClick={() => onEdit(workspace)}>Edit</DropdownMenuItem>
                        <DropdownMenuItem onClick={() => onDelete(workspace)} className="text-destructive focus:text-destructive">
                            Delete
                        </DropdownMenuItem>
                    </DropdownMenuContent>
                </DropdownMenu>
            )
        },
    },
]
