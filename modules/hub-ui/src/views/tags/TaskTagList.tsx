
import { useState } from 'react';
import { useQueryClient } from '@tanstack/react-query';
import { useTaskTagsQuery, useDeleteTaskTagMutation } from '@/api/queries/taskTags';
import { DataTable } from '@/components/ui/data-table';
import { getTagColumns } from './columns';
import { Button } from '@/components/ui/button';
import type { TaskTagRead } from '@/generated/api/models/TaskTagRead';
import TaskTagForm from './TaskTagForm';
import { Dialog, DialogContent, DialogTrigger, DialogHeader, DialogTitle } from '@/components/ui/dialog';
import { Plus } from 'lucide-react';
import { queryKeys } from '@/api/queryKeys';

export default function TaskTagList() {
    const [pagination, setPagination] = useState({ pageIndex: 0, pageSize: 10 });
    const [selectedTag, setSelectedTag] = useState<TaskTagRead | null>(null);
    const [isDialogOpen, setIsDialogOpen] = useState(false);
    const queryClient = useQueryClient();

    const { data } = useTaskTagsQuery({
        offset: pagination.pageIndex * pagination.pageSize,
        limit: pagination.pageSize,
    });

    const deleteMutation = useDeleteTaskTagMutation();

    const handleEdit = (tag: TaskTagRead) => {
        setSelectedTag(tag);
        setIsDialogOpen(true);
    };

    const handleDelete = async (tag: TaskTagRead) => {
        if (confirm('Are you sure you want to delete this tag?')) {
            deleteMutation.mutate(tag.id);
        }
    };

    const handleOpenChange = (open: boolean) => {
        setIsDialogOpen(open);
        if (!open) setSelectedTag(null);
    };

    const columns = getTagColumns({ onEdit: handleEdit, onDelete: handleDelete });

    return (
        <div className="space-y-4">
            <div className="flex justify-between items-center">
                <h2 className="text-3xl font-bold tracking-tight">Task Tags</h2>
                <Dialog open={isDialogOpen} onOpenChange={handleOpenChange}>
                    <DialogTrigger asChild>
                        <Button onClick={() => setSelectedTag(null)}>
                            <Plus className="mr-2 h-4 w-4" /> Create Tag
                        </Button>
                    </DialogTrigger>
                    <DialogContent>
                        <DialogHeader>
                            <DialogTitle>{selectedTag ? 'Edit Tag' : 'Create Tag'}</DialogTitle>
                        </DialogHeader>
                        <TaskTagForm
                            tag={selectedTag}
                            onSuccess={() => {
                                setIsDialogOpen(false);
                                queryClient.invalidateQueries({ queryKey: queryKeys.taskTags.all });
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
