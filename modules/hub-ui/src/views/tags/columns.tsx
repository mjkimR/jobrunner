
import type { ColumnDef } from "@tanstack/react-table"
import type { TaskTagRead } from "../../generated/api/models/TaskTagRead"
import { MoreHorizontal } from "lucide-react"
import { Button } from "@/components/ui/button"
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuLabel,
    DropdownMenuSeparator,
    DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"

export type TaskTagColumnProps = {
    onEdit: (tag: TaskTagRead) => void;
    onDelete: (tag: TaskTagRead) => void;
}

export const getTagColumns = ({ onEdit, onDelete }: TaskTagColumnProps): ColumnDef<TaskTagRead>[] => [
    {
        accessorKey: "name",
        header: "Name",
        cell: ({ row }) => {
            const color = row.original.color || '#888888';
            return (
                <div className="flex items-center gap-2">
                    <div className="w-3 h-3 rounded-full" style={{ backgroundColor: color }} />
                    <span>{row.getValue("name")}</span>
                </div>
            )
        }
    },
    {
        accessorKey: "description",
        header: "Description",
    },
    {
        accessorKey: "color",
        header: "Color",
        cell: ({ row }) => (
            <div className="flex items-center gap-2">
                <span className="font-mono text-xs">{row.getValue("color")}</span>
            </div>
        )
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
            const tag = row.original

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
                        <DropdownMenuItem onClick={() => navigator.clipboard.writeText(tag.id)}>
                            Copy ID
                        </DropdownMenuItem>
                        <DropdownMenuSeparator />
                        <DropdownMenuItem onClick={() => onEdit(tag)}>Edit</DropdownMenuItem>
                        <DropdownMenuItem onClick={() => onDelete(tag)} className="text-destructive">
                            Delete
                        </DropdownMenuItem>
                    </DropdownMenuContent>
                </DropdownMenu>
            )
        },
    },
]
