
import type { ColumnDef } from "@tanstack/react-table"
import type { RoutingLogRead } from "../../generated/api/models/RoutingLogRead"
import { Badge } from "@/components/ui/badge"

export const getColumns = (): ColumnDef<RoutingLogRead>[] => [
    {
        accessorKey: "created_at",
        header: "Timestamp",
        cell: ({ row }) => {
            return new Date(row.getValue("created_at")).toLocaleString()
        }
    },
    {
        accessorKey: "routing_result",
        header: "Result",
        cell: ({ row }) => <Badge variant="outline">{row.getValue("routing_result")}</Badge>,
    },
    {
        accessorKey: "confidence",
        header: "Confidence",
        cell: ({ row }) => {
            const confidence = row.getValue("confidence") as number | null;
            return confidence ? confidence.toFixed(2) : '-';
        }
    },
    {
        accessorKey: "target_agent_id",
        header: "Target Agent",
        cell: ({ row }) => {
            const agentId = row.getValue("target_agent_id") as string | null;
            return agentId ? <code className="text-xs bg-muted px-1 rounded">{agentId}</code> : '-';
        }
    },
    {
        accessorKey: "reasoning",
        header: "Reasoning",
        cell: ({ row }) => <div className="truncate max-w-[300px]" title={row.getValue("reasoning")}>{row.getValue("reasoning")}</div>,
    },
]
