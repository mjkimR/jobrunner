import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import * as z from 'zod';
import { Button } from '@/components/ui/button';
import {
    Form,
    FormControl,
    FormDescription,
    FormField,
    FormItem,
    FormLabel,
    FormMessage,
} from '@/components/ui/form';
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/textarea';
import type { WorkspaceRead } from '@/generated/api/models/WorkspaceRead';
import type { WorkspaceCreate } from '@/generated/api/models/WorkspaceCreate';
import type { WorkspaceUpdate } from '@/generated/api/models/WorkspaceUpdate';
import { useCreateWorkspaceMutation, useUpdateWorkspaceMutation } from '@/api/queries/workspaces';
import { useEffect } from 'react';
import { Checkbox } from '@/components/ui/checkbox';

const workspaceSchema = z.object({
    name: z.string().min(1, 'Name is required'),
    alias: z.string().min(1, 'Alias is required'),
    description: z.string().optional(),
    is_default: z.boolean().optional(),
});

interface WorkspaceFormProps {
    workspace?: WorkspaceRead | null;
    onSuccess: () => void;
}

export default function WorkspaceForm({ workspace, onSuccess }: WorkspaceFormProps) {
    const form = useForm<z.infer<typeof workspaceSchema>>({
        resolver: zodResolver(workspaceSchema),
        defaultValues: {
            name: '',
            alias: '',
            description: '',
            is_default: false,
        },
    });

    useEffect(() => {
        if (workspace) {
            form.reset({
                name: workspace.name,
                alias: workspace.alias,
                description: workspace.description || '',
                is_default: workspace.is_default,
            });
        } else {
            form.reset({
                name: '',
                alias: '',
                description: '',
                is_default: false,
            });
        }
    }, [workspace, form]);

    const createMutation = useCreateWorkspaceMutation();
    const updateMutation = useUpdateWorkspaceMutation(workspace?.id ?? '');

    function onSubmit(values: z.infer<typeof workspaceSchema>) {
        if (workspace) {
            updateMutation.mutate(values as WorkspaceUpdate, {
                onSuccess,
            });
        } else {
            createMutation.mutate(values as WorkspaceCreate, {
                onSuccess,
            });
        }
    }

    return (
        <Form {...form}>
            <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
                <FormField
                    control={form.control}
                    name="name"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Name</FormLabel>
                            <FormControl>
                                <Input placeholder="My Main Project" {...field} />
                            </FormControl>
                            <FormDescription>A human-readable name for the workspace.</FormDescription>
                            <FormMessage />
                        </FormItem>
                    )}
                />
                <FormField
                    control={form.control}
                    name="alias"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Alias</FormLabel>
                            <FormControl>
                                <Input placeholder="main-project" {...field} />
                            </FormControl>
                            <FormDescription>A unique, URL-friendly identifier.</FormDescription>
                            <FormMessage />
                        </FormItem>
                    )}
                />
                <FormField
                    control={form.control}
                    name="description"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Description</FormLabel>
                            <FormControl>
                                <Textarea placeholder="What this workspace is for." {...field} />
                            </FormControl>
                            <FormMessage />
                        </FormItem>
                    )}
                />
                <FormField
                    control={form.control}
                    name="is_default"
                    render={({ field }) => (
                        <FormItem className="flex flex-row items-start space-x-3 space-y-0 rounded-md border p-4">
                            <FormControl>
                                <Checkbox
                                    checked={field.value}
                                    onCheckedChange={field.onChange}
                                />
                            </FormControl>
                            <div className="space-y-1 leading-none">
                                <FormLabel>
                                    Default Workspace
                                </FormLabel>
                                <FormDescription>
                                    Make this the default workspace for new sessions.
                                </FormDescription>
                            </div>
                        </FormItem>
                    )}
                />


                <Button type="submit" disabled={createMutation.isPending || updateMutation.isPending}>
                    {workspace ? 'Update Workspace' : 'Create Workspace'}
                </Button>
            </form>
        </Form>
    );
}
