
import { useState } from 'react';
import { useQueryClient } from '@tanstack/react-query';
import { useTaskHistoryListQuery, useDeleteTaskHistoryMutation } from '@/api/queries/taskHistory';
import { DataTable } from '@/components/ui/data-table';
import { getHistoryColumns } from './columns';
import { Button } from '@/components/ui/button';
import type { TaskHistoryRead } from '@/generated/api/models/TaskHistoryRead';
import TaskHistoryForm from './TaskHistoryForm';
import { Dialog, DialogContent, DialogTrigger, DialogHeader, DialogTitle } from '@/components/ui/dialog';
import { Plus } from 'lucide-react';
import { queryKeys } from '@/api/queryKeys';
import { useParams } from 'react-router-dom';

export default function TaskHistoryList() {
    const { workspaceId } = useParams<{ workspaceId: string }>();
    const [pagination, setPagination] = useState({ pageIndex: 0, pageSize: 10 });
    const [selectedHistory, setSelectedHistory] = useState<TaskHistoryRead | null>(null);
    const [isDialogOpen, setIsDialogOpen] = useState(false);
    const queryClient = useQueryClient();

    const { data, isLoading } = useTaskHistoryListQuery(workspaceId!, {
        offset: pagination.pageIndex * pagination.pageSize,
        limit: pagination.pageSize,
    });

    const deleteMutation = useDeleteTaskHistoryMutation(workspaceId!);

    const handleEdit = (history: TaskHistoryRead) => {
        setSelectedHistory(history);
        setIsDialogOpen(true);
    };

    const handleDelete = async (history: TaskHistoryRead) => {
        if (confirm('Are you sure you want to delete this history record?')) {
            deleteMutation.mutate(history.id);
        }
    };
    
    const handleFormSuccess = () => {
        setIsDialogOpen(false);
        queryClient.invalidateQueries({ queryKey: queryKeys.taskHistory.list(workspaceId!) });
    };

    const handleOpenChange = (open: boolean) => {
        setIsDialogOpen(open);
        if (!open) setSelectedHistory(null);
    };

    const columns = getHistoryColumns({ onEdit: handleEdit, onDelete: handleDelete });
    const pageCount = data ? Math.ceil((data.total_count ?? 0) / pagination.pageSize) : 0;
    
    if (!workspaceId) {
        return <div>Invalid workspace.</div>
    }

    return (
        <div className="space-y-4">
            <div className="flex justify-between items-center">
                <h2 className="text-3xl font-bold tracking-tight">Task Histories</h2>
                <Dialog open={isDialogOpen} onOpenChange={handleOpenChange}>
                    <DialogTrigger asChild>
                        <Button onClick={() => setSelectedHistory(null)}>
                            <Plus className="mr-2 h-4 w-4" /> Create History
                        </Button>
                    </DialogTrigger>
                    <DialogContent>
                        <DialogHeader>
                            <DialogTitle>{selectedHistory ? 'Edit History' : 'Create History'}</DialogTitle>
                        </DialogHeader>
                        <TaskHistoryForm
                            workspaceId={workspaceId}
                            history={selectedHistory}
                            onSuccess={handleFormSuccess}
                        />
                    </DialogContent>
                </Dialog>
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
