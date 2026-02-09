
import { useState } from 'react';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { TaskService } from '@/generated/api/services/TaskService';
import { DataTable } from '@/components/ui/data-table';
import { getColumns } from './columns';
import { Button } from '@/components/ui/button';
import type { TaskRead } from '@/generated/api/models/TaskRead';
import TaskForm from './TaskForm';
import { Dialog, DialogContent, DialogTrigger, DialogHeader, DialogTitle } from '@/components/ui/dialog';
import { Plus } from 'lucide-react';

export default function TaskList() {
    const [pagination, setPagination] = useState({ pageIndex: 0, pageSize: 10 });
    const [selectedTask, setSelectedTask] = useState<TaskRead | null>(null);
    const [isDialogOpen, setIsDialogOpen] = useState(false);
    const queryClient = useQueryClient();

    const { data } = useQuery({
        queryKey: ['tasks', pagination.pageIndex, pagination.pageSize],
        queryFn: () => TaskService.getTasksApiV1TasksGet(pagination.pageIndex * pagination.pageSize, pagination.pageSize),
    });

    const deleteMutation = useMutation({
        mutationFn: (taskId: string) => TaskService.deleteTaskApiV1TasksTaskIdDelete(taskId),
        onSuccess: () => {
            queryClient.invalidateQueries({ queryKey: ['tasks'] });
        },
    });

    const handleEdit = (task: TaskRead) => {
        setSelectedTask(task);
        setIsDialogOpen(true);
    };

    const handleDelete = async (task: TaskRead) => {
        if (confirm('Are you sure you want to delete this task?')) {
            deleteMutation.mutate(task.id);
        }
    };

    const handleOpenChange = (open: boolean) => {
        setIsDialogOpen(open);
        if (!open) setSelectedTask(null);
    };

    const columns = getColumns({ onEdit: handleEdit, onDelete: handleDelete });

    return (
        <div className="space-y-4">
            <div className="flex justify-between items-center">
                <h2 className="text-3xl font-bold tracking-tight">Tasks</h2>
                <Dialog open={isDialogOpen} onOpenChange={handleOpenChange}>
                    <DialogTrigger asChild>
                        <Button onClick={() => setSelectedTask(null)}>
                            <Plus className="mr-2 h-4 w-4" /> Create Task
                        </Button>
                    </DialogTrigger>
                    <DialogContent className="max-w-2xl max-h-[90vh] overflow-y-auto">
                        <DialogHeader>
                            <DialogTitle>{selectedTask ? 'Edit Task' : 'Create Task'}</DialogTitle>
                        </DialogHeader>
                        <TaskForm
                            task={selectedTask}
                            onSuccess={() => {
                                setIsDialogOpen(false);
                                queryClient.invalidateQueries({ queryKey: ['tasks'] });
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
