
import type { ColumnDef } from "@tanstack/react-table"
import type { TaskHistoryRead } from "../../generated/api/models/TaskHistoryRead"
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
import { Badge } from "@/components/ui/badge"

export type TaskHistoryColumnProps = {
    onEdit: (history: TaskHistoryRead) => void;
    onDelete: (history: TaskHistoryRead) => void;
}

export const getHistoryColumns = ({ onEdit, onDelete }: TaskHistoryColumnProps): ColumnDef<TaskHistoryRead>[] => [
    {
        accessorKey: "task_id",
        header: "Task ID",
        cell: ({ row }) => <span className="font-mono text-xs">{row.getValue("task_id")}</span>
    },
    {
        accessorKey: "event_type",
        header: "Event",
        cell: ({ row }) => <Badge variant="outline">{row.getValue("event_type")}</Badge>
    },
    {
        accessorKey: "changed_by",
        header: "Changed By",
    },
    {
        header: "Change",
        cell: ({ row }) => {
            const prev = row.original.previous_value;
            const curr = row.original.new_value;
            return (
                <div className="text-sm">
                    {prev && <div className="text-muted-foreground line-through">{prev}</div>}
                    <div>{curr}</div>
                </div>
            )
        }
    },
    {
        accessorKey: "created_at",
        header: "Time",
        cell: ({ row }) => {
            return new Date(row.getValue("created_at")).toLocaleString()
        }
    },
    {
        id: "actions",
        cell: ({ row }) => {
            const history = row.original

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
                        <DropdownMenuItem onClick={() => navigator.clipboard.writeText(history.id)}>
                            Copy ID
                        </DropdownMenuItem>
                        <DropdownMenuSeparator />
                        <DropdownMenuItem onClick={() => onEdit(history)}>Edit</DropdownMenuItem>
                        <DropdownMenuItem onClick={() => onDelete(history)} className="text-destructive">
                            Delete
                        </DropdownMenuItem>
                    </DropdownMenuContent>
                </DropdownMenu>
            )
        },
    },
]
