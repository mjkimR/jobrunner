
import { useState } from 'react';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { TaskHistorieService } from '@/generated/api/services/TaskHistorieService';
import { DataTable } from '@/components/ui/data-table';
import { getHistoryColumns } from './columns';
import { Button } from '@/components/ui/button';
import type { TaskHistoryRead } from '@/generated/api/models/TaskHistoryRead';
import TaskHistoryForm from './TaskHistoryForm';
import { Dialog, DialogContent, DialogTrigger, DialogHeader, DialogTitle } from '@/components/ui/dialog';
import { Plus } from 'lucide-react';

export default function TaskHistoryList() {
    const [pagination, setPagination] = useState({ pageIndex: 0, pageSize: 10 });
    const [selectedHistory, setSelectedHistory] = useState<TaskHistoryRead | null>(null);
    const [isDialogOpen, setIsDialogOpen] = useState(false);
    const queryClient = useQueryClient();

    const { data } = useQuery({
        queryKey: ['task_histories', pagination.pageIndex, pagination.pageSize],
        queryFn: () => TaskHistorieService.getTaskHistoriesApiV1TaskHistoriesGet(pagination.pageIndex * pagination.pageSize, pagination.pageSize),
    });

    const deleteMutation = useMutation({
        mutationFn: (historyId: string) => TaskHistorieService.deleteTaskHistoryApiV1TaskHistoriesTaskHistoryIdDelete(historyId),
        onSuccess: () => {
            queryClient.invalidateQueries({ queryKey: ['task_histories'] });
        },
    });

    const handleEdit = (history: TaskHistoryRead) => {
        setSelectedHistory(history);
        setIsDialogOpen(true);
    };

    const handleDelete = async (history: TaskHistoryRead) => {
        if (confirm('Are you sure you want to delete this history record?')) {
            deleteMutation.mutate(history.id);
        }
    };

    const handleOpenChange = (open: boolean) => {
        setIsDialogOpen(open);
        if (!open) setSelectedHistory(null);
    };

    const columns = getHistoryColumns({ onEdit: handleEdit, onDelete: handleDelete });

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
                            history={selectedHistory}
                            onSuccess={() => {
                                setIsDialogOpen(false);
                                queryClient.invalidateQueries({ queryKey: ['task_histories'] });
                            }}
                        />
                    </DialogContent>
                </Dialog>
            </div>

            <DataTable
                columns={columns}
                data={data?.items || []}
                pageCount={data ? Math.ceil((data.total_count ?? 0) / pagination.pageSize) : -1}
                pagination={pagination}
                onPaginationChange={setPagination}
            />
        </div>
    );
}
