
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
} from '@/components/ui/form';
import { Input } from '@/components/ui/input';
import type { TaskHistoryRead } from '@/generated/api/models/TaskHistoryRead';
import type { TaskHistoryCreate } from '@/generated/api/models/TaskHistoryCreate';
import type { TaskHistoryUpdate } from '@/generated/api/models/TaskHistoryUpdate';
import { TaskHistorieService } from '@/generated/api/services/TaskHistorieService';
import { useMutation } from '@tanstack/react-query';
import { useEffect } from 'react';

const historySchema = z.object({
    task_id: z.string().min(1, 'Task ID is required'),
    event_type: z.string().min(1, 'Event Type is required'),
    new_value: z.string().min(1, 'New Value is required'),
    previous_value: z.string().optional(),
    comment: z.string().optional(),
    changed_by: z.string().min(1, 'Changed By is required'),
});

interface TaskHistoryFormProps {
    history?: TaskHistoryRead | null;
    onSuccess: () => void;
}

export default function TaskHistoryForm({ history, onSuccess }: TaskHistoryFormProps) {
    const form = useForm<z.infer<typeof historySchema>>({
        resolver: zodResolver(historySchema),
        defaultValues: {
            task_id: '',
            event_type: 'UPDATE',
            new_value: '',
            previous_value: '',
            comment: '',
            changed_by: 'system',
        },
    });

    useEffect(() => {
        if (history) {
            form.reset({
                task_id: history.task_id,
                event_type: history.event_type,
                new_value: history.new_value,
                previous_value: history.previous_value || '',
                comment: history.comment || '',
                changed_by: history.changed_by,
            });
        } else {
            form.reset({
                task_id: '',
                event_type: 'UPDATE',
                new_value: '',
                previous_value: '',
                comment: '',
                changed_by: 'system',
            });
        }
    }, [history, form]);

    const createMutation = useMutation({
        mutationFn: (data: TaskHistoryCreate) => TaskHistorieService.createTaskHistoryApiV1TaskHistoriesPost(data),
        onSuccess: () => onSuccess(),
    });

    const updateMutation = useMutation({
        mutationFn: (data: TaskHistoryUpdate) => TaskHistorieService.updateTaskHistoryApiV1TaskHistoriesTaskHistoryIdPut(history!.id, data),
        onSuccess: () => onSuccess(),
    });

    function onSubmit(values: z.infer<typeof historySchema>) {
        if (history) {
            updateMutation.mutate(values as TaskHistoryUpdate);
        } else {
            createMutation.mutate(values as TaskHistoryCreate);
        }
    }

    return (
        <Form {...form}>
            <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
                <FormField
                    control={form.control}
                    name="task_id"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Task ID</FormLabel>
                            <FormControl>
                                <Input placeholder="Task ID" {...field} />
                            </FormControl>
                            <FormMessage />
                        </FormItem>
                    )}
                />
                <div className="grid grid-cols-2 gap-4">
                    <FormField
                        control={form.control}
                        name="event_type"
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel>Event Type</FormLabel>
                                <FormControl>
                                    <Input placeholder="Event Type" {...field} />
                                </FormControl>
                                <FormMessage />
                            </FormItem>
                        )}
                    />
                    <FormField
                        control={form.control}
                        name="changed_by"
                        render={({ field }) => (
                            <FormItem>
                                <FormLabel>Changed By</FormLabel>
                                <FormControl>
                                    <Input placeholder="Changed By" {...field} />
                                </FormControl>
                                <FormMessage />
                            </FormItem>
                        )}
                    />
                </div>

                <FormField
                    control={form.control}
                    name="previous_value"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Previous Value</FormLabel>
                            <FormControl>
                                <Input placeholder="Previous Value" {...field} />
                            </FormControl>
                            <FormMessage />
                        </FormItem>
                    )}
                />

                <FormField
                    control={form.control}
                    name="new_value"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>New Value</FormLabel>
                            <FormControl>
                                <Input placeholder="New Value" {...field} />
                            </FormControl>
                            <FormMessage />
                        </FormItem>
                    )}
                />

                <FormField
                    control={form.control}
                    name="comment"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Comment</FormLabel>
                            <FormControl>
                                <Input placeholder="Comment" {...field} />
                            </FormControl>
                            <FormMessage />
                        </FormItem>
                    )}
                />

                <Button type="submit">
                    {history ? 'Update History' : 'Create History'}
                </Button>
            </form>
        </Form>
    );
}
