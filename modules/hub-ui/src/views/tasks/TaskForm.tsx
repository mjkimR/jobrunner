
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import * as z from 'zod';
import { Button } from '@/components/ui/button';
import {
    Form,
    FormControl,
    FormField,
    FormItem,
    FormLabel,
    FormMessage,
    FormDescription,
} from '@/components/ui/form';
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/textarea';
import {
    Select,
    SelectContent,
    SelectItem,
    SelectTrigger,
    SelectValue,
} from '@/components/ui/select';
import type { TaskRead } from '@/generated/api/models/TaskRead';
import type { TaskCreate } from '@/generated/api/models/TaskCreate';
import type { TaskUpdate } from '@/generated/api/models/TaskUpdate';
import { useCreateTaskMutation, useUpdateTaskMutation } from '@/api/queries/tasks';
import { useEffect } from 'react';

const taskSchema = z.object({
    title: z.string().min(1, 'Title is required'),
    description: z.string().optional(),
    status: z.string().min(1, 'Status is required'),
    priority: z.string().min(1, 'Priority is required'),
    urgency: z.string().min(1, 'Urgency is required'),
    complexity: z.string().min(1, 'Complexity is required'),
    queue: z.string().min(1, 'Queue is required'),
    tags: z.string().optional(),
});

interface TaskFormProps {
    workspaceId: string;
    task?: TaskRead | null;
    onSuccess: () => void;
}

export default function TaskForm({ workspaceId, task, onSuccess }: TaskFormProps) {
    const form = useForm<z.infer<typeof taskSchema>>({
        resolver: zodResolver(taskSchema),
        defaultValues: {
            title: '',
            description: '',
            status: 'pending',
            priority: 'normal',
            urgency: 'normal',
            complexity: 'moderate',
            queue: 'default',
            tags: '',
        },
    });

    useEffect(() => {
        if (task) {
            form.reset({
                title: task.title,
                description: task.description || '',
                status: task.status,
                priority: task.priority,
                urgency: task.urgency,
                complexity: task.complexity,
                queue: task.queue,
                tags: task.tags?.map(t => t.name).join(', ') || '',
            });
        } else {
            form.reset({
                title: '',
                description: '',
                status: 'pending',
                priority: 'normal',
                urgency: 'normal',
                complexity: 'moderate',
                queue: 'default',
                tags: '',
            });
        }
    }, [task, form]);

    const createMutation = useCreateTaskMutation(workspaceId);
    const updateMutation = useUpdateTaskMutation(workspaceId);

    function onSubmit(values: z.infer<typeof taskSchema>) {
        const tagsList = values.tags 
            ? values.tags.split(',').map(t => t.trim()).filter(Boolean)
            : [];

        if (task) {
            updateMutation.mutate({ 
                taskId: task.id, 
                data: { ...values, tags: tagsList } as TaskUpdate 
            }, {
                onSuccess: onSuccess,
            });
        } else {
            createMutation.mutate({ ...values, tags: tagsList } as TaskCreate, {
                onSuccess: onSuccess,
            });
        }
    }

    return (
        <Form {...form}>
            <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
                <FormField
                    control={form.control}
                    name="title"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Title</FormLabel>
                            <FormControl>
                                <Input placeholder="Task title" {...field} />
                            </FormControl>
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
                                <Textarea placeholder="Task description" {...field} />
                            </FormControl>
                            <FormMessage />
                        </FormItem>
                    )}
                />
                
                <FormField
                    control={form.control}
                    name="tags"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Tags</FormLabel>
                            <FormControl>
                                <Input placeholder="Type tags separated by commas... (e.g. bug, frontend)" {...field} />
                            </FormControl>
                            <FormDescription>
                                Separate multiple tags with commas.
                            </FormDescription>
                            <FormMessage />
                        </FormItem>
                    )}
                />

                <div className="grid grid-cols-2 gap-4">
                    <FormField
                        control={form.control}
                        name="status"
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel>Status</FormLabel>
                                <Select onValueChange={field.onChange} defaultValue={field.value} value={field.value}>
                                    <FormControl>
                                        <SelectTrigger>
                                            <SelectValue placeholder="Select status" />
                                        </SelectTrigger>
                                    </FormControl>
                                    <SelectContent>
                                        <SelectItem value="pending">Pending</SelectItem>
                                        <SelectItem value="in_progress">In Progress</SelectItem>
                                        <SelectItem value="review">Review</SelectItem>
                                        <SelectItem value="done">Done</SelectItem>
                                        <SelectItem value="cancelled">Cancelled</SelectItem>
                                    </SelectContent>
                                </Select>
                                <FormMessage />
                            </FormItem>
                        )}
                    />
                    <FormField
                        control={form.control}
                        name="priority"
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel>Priority</FormLabel>
                                <Select onValueChange={field.onChange} defaultValue={field.value} value={field.value}>
                                    <FormControl>
                                        <SelectTrigger>
                                            <SelectValue placeholder="Select priority" />
                                        </SelectTrigger>
                                    </FormControl>
                                    <SelectContent>
                                        <SelectItem value="low">Low</SelectItem>
                                        <SelectItem value="normal">Normal</SelectItem>
                                        <SelectItem value="high">High</SelectItem>
                                        <SelectItem value="critical">Critical</SelectItem>
                                    </SelectContent>
                                </Select>
                                <FormMessage />
                            </FormItem>
                        )}
                    />
                </div>

                <div className="grid grid-cols-2 gap-4">
                    <FormField
                        control={form.control}
                        name="urgency"
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel>Urgency</FormLabel>
                                <Select onValueChange={field.onChange} defaultValue={field.value} value={field.value}>
                                    <FormControl>
                                        <SelectTrigger>
                                            <SelectValue placeholder="Select urgency" />
                                        </SelectTrigger>
                                    </FormControl>
                                    <SelectContent>
                                        <SelectItem value="low">Low</SelectItem>
                                        <SelectItem value="normal">Normal</SelectItem>
                                        <SelectItem value="high">High</SelectItem>
                                        <SelectItem value="critical">Critical</SelectItem>
                                    </SelectContent>
                                </Select>
                                <FormMessage />
                            </FormItem>
                        )}
                    />
                    <FormField
                        control={form.control}
                        name="complexity"
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel>Complexity</FormLabel>
                                <Select onValueChange={field.onChange} defaultValue={field.value} value={field.value}>
                                    <FormControl>
                                        <SelectTrigger>
                                            <SelectValue placeholder="Select complexity" />
                                        </SelectTrigger>
                                    </FormControl>
                                    <SelectContent>
                                        <SelectItem value="simple">Simple</SelectItem>
                                        <SelectItem value="moderate">Moderate</SelectItem>
                                        <SelectItem value="complex">Complex</SelectItem>
                                    </SelectContent>
                                </Select>
                                <FormMessage />
                            </FormItem>
                        )}
                    />
                </div>

                <FormField
                    control={form.control}
                    name="queue"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Queue</FormLabel>
                            <Select onValueChange={field.onChange} defaultValue={field.value} value={field.value}>
                                <FormControl>
                                        <SelectTrigger>
                                            <SelectValue placeholder="Select queue" />
                                        </SelectTrigger>
                                </FormControl>
                                <SelectContent>
                                    <SelectItem value="default">Default</SelectItem>
                                    <SelectItem value="host-agent">Host Agent</SelectItem>
                                    <SelectItem value="local-agent">Local Agent</SelectItem>
                                    <SelectItem value="workflow">Workflow</SelectItem>
                                </SelectContent>
                            </Select>
                            <FormMessage />
                        </FormItem>
                    )}
                />

                <Button type="submit">
                    {task ? 'Update Task' : 'Create Task'}
                </Button>
            </form>
        </Form>
    );
}
