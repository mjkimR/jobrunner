
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
import type { TaskTagRead } from '@/generated/api/models/TaskTagRead';
import type { TaskTagCreate } from '@/generated/api/models/TaskTagCreate';
import type { TaskTagUpdate } from '@/generated/api/models/TaskTagUpdate';
import { TaskTagService } from '@/generated/api/services/TaskTagService';
import { useMutation } from '@tanstack/react-query';
import { useEffect } from 'react';

const tagSchema = z.object({
    name: z.string().min(1, 'Name is required'),
    description: z.string().optional(),
    color: z.string().optional(),
});

interface TaskTagFormProps {
    tag?: TaskTagRead | null;
    onSuccess: () => void;
}

export default function TaskTagForm({ tag, onSuccess }: TaskTagFormProps) {
    const form = useForm<z.infer<typeof tagSchema>>({
        resolver: zodResolver(tagSchema),
        defaultValues: {
            name: '',
            description: '',
            color: '#000000',
        },
    });

    useEffect(() => {
        if (tag) {
            form.reset({
                name: tag.name,
                description: tag.description || '',
                color: tag.color || '#000000',
            });
        } else {
            form.reset({
                name: '',
                description: '',
                color: '#000000',
            });
        }
    }, [tag, form]);

    const createMutation = useMutation({
        mutationFn: (data: TaskTagCreate) => TaskTagService.createTaskTagApiV1TaskTagsPost(data),
        onSuccess: () => onSuccess(),
    });

    const updateMutation = useMutation({
        mutationFn: (data: TaskTagUpdate) => TaskTagService.updateTaskTagApiV1TaskTagsTaskTagIdPut(tag!.id, data),
        onSuccess: () => onSuccess(),
    });

    function onSubmit(values: z.infer<typeof tagSchema>) {
        if (tag) {
            updateMutation.mutate(values as TaskTagUpdate);
        } else {
            createMutation.mutate(values as TaskTagCreate);
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
                                <Input placeholder="Tag name" {...field} />
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
                                <Input placeholder="Tag description" {...field} />
                            </FormControl>
                            <FormMessage />
                        </FormItem>
                    )}
                />
                <FormField
                    control={form.control}
                    name="color"
                    render={({ field }) => (
                        <FormItem>
                            <FormLabel>Color</FormLabel>
                            <FormControl>
                                <div className="flex items-center gap-2">
                                    <Input type="color" className="w-12 p-1 h-10" {...field} />
                                    <Input placeholder="#RRGGBB" {...field} />
                                </div>
                            </FormControl>
                            <FormMessage />
                        </FormItem>
                    )}
                />

                <Button type="submit">
                    {tag ? 'Update Tag' : 'Create Tag'}
                </Button>
            </form>
        </Form>
    );
}
