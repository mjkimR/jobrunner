
import { useParams } from 'react-router-dom';
import { useChatMessagesQuery } from '@/api/queries/useChatMessagesQuery';
import type { ChatMessageRead } from '@/generated/api/models/ChatMessageRead';
import { useConversationQuery } from '@/api/queries/useConversationsQuery';
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { cn } from '@/lib/utils';

export default function ConversationDetail() {
    const { conversationId } = useParams<{ conversationId: string }>();
    
    // Fetch conversation details
    const { data: conversation, isLoading: isConversationLoading } = useConversationQuery(conversationId!);

    // Fetch messages
    const { data: messagesData, isLoading: isMessagesLoading } = useChatMessagesQuery(conversationId!, {
        limit: 100 // Fetch a reasonable amount of history
    });

    if (isConversationLoading || isMessagesLoading) {
        return <div>Loading...</div>;
    }

    if (!conversation) {
        return <div>Conversation not found.</div>;
    }

    const messages = messagesData?.items || [];

    return (
        <div className="space-y-4 h-full flex flex-col">
            <Card>
                <CardHeader>
                    <div className="flex justify-between items-start">
                        <div>
                            <CardTitle>{conversation.title || 'Untitled Conversation'}</CardTitle>
                            <CardDescription>ID: {conversation.id}</CardDescription>
                        </div>
                        <Badge variant={conversation.status === 'active' ? 'default' : 'secondary'}>
                            {conversation.status}
                        </Badge>
                    </div>
                </CardHeader>
            </Card>

            <Card className="flex-1 flex flex-col min-h-0">
                <CardHeader className="pb-2">
                    <CardTitle className="text-lg">Chat History</CardTitle>
                </CardHeader>
                <CardContent className="flex-1 overflow-hidden p-0">
                    <div className="h-[600px] overflow-y-auto p-4 space-y-4">
                        {messages.length === 0 ? (
                            <div className="text-center text-muted-foreground p-4">No messages yet.</div>
                        ) : (
                                messages.map((msg: ChatMessageRead) => (
                                <div
                                    key={msg.id}
                                    className={cn(
                                        "flex w-max max-w-[80%] flex-col gap-2 rounded-lg px-3 py-2 text-sm",
                                        msg.role === "user"
                                            ? "ml-auto bg-primary text-primary-foreground"
                                            : "bg-muted"
                                    )}
                                >
                                    <div className="font-semibold text-xs opacity-70 mb-0.5 capitalize">
                                        {msg.role}
                                    </div>
                                    <div className="whitespace-pre-wrap leading-relaxed">
                                        {msg.content}
                                    </div>
                                    <div className="text-[10px] opacity-70 self-end mt-1">
                                        {new Date(msg.created_at).toLocaleTimeString()}
                                    </div>
                                </div>
                            ))
                        )}
                    </div>
                </CardContent>
            </Card>
        </div>
    );
}
