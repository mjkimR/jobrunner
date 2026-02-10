
import type { ColumnDef } from "@tanstack/react-table"
import type { ConfiguredAgentRead } from "../../generated/api/models/ConfiguredAgentRead"
import { MoreHorizontal } from "lucide-react"
import { Button } from "@/components/ui/button"
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuLabel,
    DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import { Badge } from "@/components/ui/badge"

export type AgentColumnProps = {
    // Add actions here if needed
}


export const getColumns = (): ColumnDef<ConfiguredAgentRead>[] => [
    {
        accessorKey: "name",
        header: "Name",
        cell: ({ row }) => <div className="font-medium">{row.getValue("name")}</div>,
    },
    {
        accessorKey: "model_name",
        header: "Model",
        cell: ({ row }) => <Badge variant="secondary">{row.getValue("model_name")}</Badge>,
    },
    {
        accessorKey: "description",
        header: "Description",
        cell: ({ row }) => <div className="truncate max-w-[300px]" title={row.getValue("description")}>{row.getValue("description")}</div>,
    },
    {
        accessorKey: "is_active",
        header: "Active",
        cell: ({ row }) => {
            const isActive = row.getValue("is_active");
            return <Badge variant={isActive ? "default" : "secondary"}>{isActive ? "Active" : "Inactive"}</Badge>
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
            const agent = row.original

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
                        <DropdownMenuItem onClick={() => navigator.clipboard.writeText(agent.id)}>
                            Copy ID
                        </DropdownMenuItem>
                    </DropdownMenuContent>
                </DropdownMenu>
            )
        },
    },
]
