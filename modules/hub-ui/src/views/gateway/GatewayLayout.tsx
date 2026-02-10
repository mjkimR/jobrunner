
import { Outlet, NavLink, useParams } from 'react-router-dom';
import { cn } from '@/lib/utils';
import { buttonVariants } from '@/components/ui/button';

export default function GatewayLayout() {
    const { workspaceId } = useParams<{ workspaceId: string }>();

    return (
        <div className="space-y-6 flex flex-col h-full">
            <div className="flex flex-col space-y-2">
                <h1 className="text-3xl font-bold tracking-tight">Gateway</h1>
                <p className="text-muted-foreground">
                    Monitor conversations and inspect routing logs.
                </p>
            </div>
            
            <div className="flex space-x-2 border-b pb-2">
                 <NavLink
                    to={`/workspaces/${workspaceId}/gateway/conversations`}
                    className={({ isActive }) =>
                        cn(
                            buttonVariants({ variant: isActive ? "default" : "ghost", size: "sm" }),
                            "justify-start"
                        )
                    }
                >
                    Conversations
                </NavLink>
                <NavLink
                    to={`/workspaces/${workspaceId}/gateway/logs`}
                    className={({ isActive }) =>
                        cn(
                            buttonVariants({ variant: isActive ? "default" : "ghost", size: "sm" }),
                            "justify-start"
                        )
                    }
                >
                    Routing Logs
                </NavLink>
            </div>

            <div className="flex-1 min-h-0 overflow-auto">
                <Outlet />
            </div>
        </div>
    );
}
