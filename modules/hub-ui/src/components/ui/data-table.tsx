
import type { ColumnDef } from "@tanstack/react-table"
import {
    flexRender,
    getCoreRowModel,
    useReactTable,
    getPaginationRowModel,
} from "@tanstack/react-table"

import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from "@/components/ui/table"
import { Button } from "@/components/ui/button"

interface DataTableProps<TData, TValue> {
    columns: ColumnDef<TData, TValue>[]
    data: TData[]
    pageCount?: number
    pagination?: {
        pageIndex: number
        pageSize: number
    }
    onPaginationChange?: (pagination: { pageIndex: number; pageSize: number }) => void
}

export function DataTable<TData, TValue>({
    columns,
    data,
    pageCount,
    pagination,
    onPaginationChange,
}: DataTableProps<TData, TValue>) {
    const table = useReactTable({
        data,
        columns,
        getCoreRowModel: getCoreRowModel(),
        getPaginationRowModel: getPaginationRowModel(),
        manualPagination: !!pageCount,
        pageCount: pageCount ?? -1,
        state: {
            pagination: pagination,
        },
        onPaginationChange: (updater) => {
            if (typeof updater === 'function' && pagination) {
                const next = updater({
                    pageIndex: pagination.pageIndex,
                    pageSize: pagination.pageSize,
                });
                onPaginationChange?.(next);
            } else if (typeof updater !== 'function' && onPaginationChange) {
                // This case is tricky with strict types but simplified for now
                // casting updater as any since we expect it to be the new state if not function
                onPaginationChange(updater as any);
            }
        }
    })

    return (
        <div>
            <div className="rounded-md border">
                <Table>
                    <TableHeader>
                        {table.getHeaderGroups().map((headerGroup) => (
                            <TableRow key={headerGroup.id}>
                                {headerGroup.headers.map((header) => {
                                    return (
                                        <TableHead key={header.id}>
                                            {header.isPlaceholder
                                                ? null
                                                : flexRender(
                                                    header.column.columnDef.header,
                                                    header.getContext()
                                                )}
                                        </TableHead>
                                    )
                                })}
                            </TableRow>
                        ))}
                    </TableHeader>
                    <TableBody>
                        {table.getRowModel().rows?.length ? (
                            table.getRowModel().rows.map((row) => (
                                <TableRow
                                    key={row.id}
                                    data-state={row.getIsSelected() && "selected"}
                                >
                                    {row.getVisibleCells().map((cell) => (
                                        <TableCell key={cell.id}>
                                            {flexRender(cell.column.columnDef.cell, cell.getContext())}
                                        </TableCell>
                                    ))}
                                </TableRow>
                            ))
                        ) : (
                            <TableRow>
                                <TableCell colSpan={columns.length} className="h-24 text-center">
                                    No results.
                                </TableCell>
                            </TableRow>
                        )}
                    </TableBody>
                </Table>
            </div>
            <div className="flex items-center justify-end space-x-2 py-4">
                <Button
                    variant="outline"
                    size="sm"
                    onClick={() => {
                        if (onPaginationChange && pagination) {
                            onPaginationChange({ ...pagination, pageIndex: pagination.pageIndex - 1 })
                        } else {
                            table.previousPage()
                        }
                    }}
                    disabled={pagination ? pagination.pageIndex === 0 : !table.getCanPreviousPage()}
                >
                    Previous
                </Button>
                <Button
                    variant="outline"
                    size="sm"
                    onClick={() => {
                        if (onPaginationChange && pagination) {
                            onPaginationChange({ ...pagination, pageIndex: pagination.pageIndex + 1 })
                        } else {
                            table.nextPage()
                        }
                    }}
                    disabled={pagination && pageCount ? pagination.pageIndex >= pageCount - 1 : !table.getCanNextPage()}
                >
                    Next
                </Button>
            </div>
        </div>
    )
}
