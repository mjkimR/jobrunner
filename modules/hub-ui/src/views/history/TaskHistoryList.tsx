
import { useState } from 'react';
import { useTaskHistoryListQuery, useDeleteTaskHistoryMutation } from '@/api/queries/taskHistory';
import { DataTable } from '@/components/ui/data-table';
import { getHistoryColumns } from './columns';
import type { TaskHistoryRead } from '@/generated/api/models/TaskHistoryRead';
import { useParams } from 'react-router-dom';

export default function TaskHistoryList() {
    const { workspaceId } = useParams<{ workspaceId: string }>();
    const [pagination, setPagination] = useState({ pageIndex: 0, pageSize: 10 });
    
    const { data, isLoading } = useTaskHistoryListQuery(workspaceId!, {
        offset: pagination.pageIndex * pagination.pageSize,
        limit: pagination.pageSize,
    });

    const deleteMutation = useDeleteTaskHistoryMutation(workspaceId!);

    const handleDelete = async (history: TaskHistoryRead) => {
        if (confirm('Are you sure you want to delete this history record?')) {
            deleteMutation.mutate(history.id);
        }
    };
    
    const columns = getHistoryColumns({ onDelete: handleDelete });
    const pageCount = data ? Math.ceil((data.total_count ?? 0) / pagination.pageSize) : 0;
    
    if (!workspaceId) {
        return <div>Invalid workspace.</div>
    }

    return (
        <div className="space-y-4">
            <div className="flex justify-between items-center">
                <h2 className="text-3xl font-bold tracking-tight">Task Histories</h2>
            </div>

            <DataTable
                columns={columns}
                data={data?.items || []}
                pageCount={pageCount}
                pagination={pagination}
                onPaginationChange={setPagination}
                isLoading={isLoading}
            />
        </div>
    );
}
