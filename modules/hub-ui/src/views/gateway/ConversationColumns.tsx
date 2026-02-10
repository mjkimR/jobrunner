
import type { ColumnDef } from "@tanstack/react-table"
import type { ConversationRead } from "../../generated/api/models/ConversationRead"
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
import { Link } from "react-router-dom"

export const getColumns = (workspaceId: string): ColumnDef<ConversationRead>[] => [
    {
        accessorKey: "title",
        header: "Title",
        cell: ({ row }) => {
            const conversation = row.original;
            return (
                <Link 
                    to={`/workspaces/${workspaceId}/gateway/conversations/${conversation.id}`}
                    className="font-medium hover:underline"
                >
                    {conversation.title || "Untitled Conversation"}
                </Link>
            );
        },
    },
    {
        accessorKey: "channel",
        header: "Channel",
        cell: ({ row }) => <Badge variant="outline">{row.getValue("channel")}</Badge>,
    },
    {
        accessorKey: "status",
        header: "Status",
        cell: ({ row }) => {
            return <Badge variant="secondary">{row.getValue("status")}</Badge>
        }
    },
    {
        accessorKey: "started_at",
        header: "Started At",
        cell: ({ row }) => {
            return new Date(row.getValue("started_at")).toLocaleString()
        }
    },
    {
        id: "actions",
        cell: ({ row }) => {
            const conversation = row.original

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
                        <DropdownMenuItem asChild>
                            <Link to={`/workspaces/${workspaceId}/gateway/conversations/${conversation.id}`}>
                                View Details
                            </Link>
                        </DropdownMenuItem>
                        <DropdownMenuItem onClick={() => navigator.clipboard.writeText(conversation.id)}>
                            Copy ID
                        </DropdownMenuItem>
                    </DropdownMenuContent>
                </DropdownMenu>
            )
        },
    },
]
