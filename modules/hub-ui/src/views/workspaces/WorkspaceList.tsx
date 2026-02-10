import { useState } from 'react';
import { useQueryClient } from '@tanstack/react-query';
import { useWorkspacesQuery, useDeleteWorkspaceMutation } from '@/api/queries/workspaces';
import { DataTable } from '@/components/ui/data-table';
import { getWorkspaceColumns } from './columns';
import { Button } from '@/components/ui/button';
import type { WorkspaceRead } from '@/generated/api';
import WorkspaceForm from './WorkspaceForm';
import { Dialog, DialogContent, DialogTrigger, DialogHeader, DialogTitle } from '@/components/ui/dialog';
import { Plus } from 'lucide-react';
import { queryKeys } from '@/api/queryKeys';

export default function WorkspaceList() {
    const [pagination, setPagination] = useState({ pageIndex: 0, pageSize: 10 });
    const [selectedWorkspace, setSelectedWorkspace] = useState<WorkspaceRead | null>(null);
    const [isDialogOpen, setIsDialogOpen] = useState(false);
    const queryClient = useQueryClient();

    const { data, isLoading } = useWorkspacesQuery({
        offset: pagination.pageIndex * pagination.pageSize,
        limit: pagination.pageSize,
    });

    const deleteMutation = useDeleteWorkspaceMutation();

    const handleEdit = (workspace: WorkspaceRead) => {
        setSelectedWorkspace(workspace);
        setIsDialogOpen(true);
    };

    const handleDelete = async (workspace: WorkspaceRead) => {
        if (confirm('Are you sure you want to delete this workspace? This action cannot be undone.')) {
            deleteMutation.mutate(workspace.id);
        }
    };

    const handleFormSuccess = () => {
        setIsDialogOpen(false);
        queryClient.invalidateQueries({ queryKey: queryKeys.workspaces.all });
    };
    
    const handleOpenChange = (open: boolean) => {
        setIsDialogOpen(open);
        if (!open) setSelectedWorkspace(null);
    };

    const columns = getWorkspaceColumns({ onEdit: handleEdit, onDelete: handleDelete });
    const pageCount = data ? Math.ceil((data.total_count ?? 0) / pagination.pageSize) : 0;

    return (
        <div className="space-y-6">
            <div className="flex justify-between items-center">
                <div>
                    <h2 className="text-2xl font-bold tracking-tight">Workspaces</h2>
                    <p className="text-muted-foreground">
                        Manage all workspaces in the system.
                    </p>
                </div>
                <Dialog open={isDialogOpen} onOpenChange={handleOpenChange}>
                    <DialogTrigger asChild>
                        <Button onClick={() => setSelectedWorkspace(null)}>
                            <Plus className="mr-2 h-4 w-4" /> Create Workspace
                        </Button>
                    </DialogTrigger>
                    <DialogContent className="max-w-md">
                        <DialogHeader>
                            <DialogTitle>{selectedWorkspace ? 'Edit Workspace' : 'Create Workspace'}</DialogTitle>
                        </DialogHeader>
                        <WorkspaceForm
                            workspace={selectedWorkspace}
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
