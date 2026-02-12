
import { Outlet, Link, useLocation, useParams } from 'react-router-dom';
import { cn } from '@/lib/utils';
import { Button } from '@/components/ui/button';
import {
    History,
    Menu,
    Bot,
    Briefcase,
    MessageSquare,
    StickyNote,
    Tag,
} from 'lucide-react';
import { useState } from 'react';
import { Sheet, SheetContent, SheetTrigger } from '@/components/ui/sheet';
import { WorkspaceSelector } from '@/components/WorkspaceSelector';
import { Separator } from '@/components/ui/separator';
import { useUiStore } from '@/stores/uiStore';

interface SidebarProps extends React.HTMLAttributes<HTMLDivElement> { }

export function Sidebar({ className }: SidebarProps) {
    const location = useLocation();
    const { workspaceId: paramWorkspaceId } = useParams<{ workspaceId: string }>();
    const activeWorkspaceId = useUiStore((s) => s.activeWorkspaceId);
    const pathname = location.pathname;

    const workspaceId = paramWorkspaceId || activeWorkspaceId;

    const workspaceItems = [
        { name: 'Gateway', href: `/workspaces/${workspaceId}/gateway`, icon: MessageSquare, exact: false },
        { name: 'Tasks', href: `/workspaces/${workspaceId}/tasks`, icon: StickyNote, exact: false },
        { name: 'Tags', href: `/workspaces/${workspaceId}/tags`, icon: Tag, exact: false },
        { name: 'History', href: `/workspaces/${workspaceId}/history`, icon: History, exact: false },
    ];
// ... rest of the file ...

    const globalItems = [
        { name: 'Agents', href: '/agents', icon: Bot, exact: false },
    ];

    const settingsItems = [
        { name: 'Workspaces', href: '/settings/workspaces', icon: Briefcase, exact: false }
    ];

    const isActive = (item: { href: string, exact: boolean }) => {
        return item.exact ? pathname === item.href : pathname.startsWith(item.href);
    }

    return (
        <div className={cn("h-full flex flex-col", className)}>
            <div className="px-3 py-4">
                <h2 className="mb-2 px-4 text-lg font-semibold tracking-tight">
                    JobRunner
                </h2>
                <div className="px-2">
                    <WorkspaceSelector />
                </div>
            </div>

            {workspaceId && (
                <div className="px-3 py-2">
                    <h3 className="mb-2 px-4 text-xs font-semibold uppercase text-muted-foreground tracking-wider">
                        Workspace
                    </h3>
                    <div className="space-y-1">
                        {workspaceItems.map((item) => (
                            <Button
                                key={item.href}
                                variant={isActive(item) ? "secondary" : "ghost"}
                                className="w-full justify-start"
                                asChild
                            >
                                <Link to={item.href}>
                                    <item.icon className="mr-2 h-4 w-4" />
                                    {item.name}
                                </Link>
                            </Button>
                        ))}
                    </div>
                </div>
            )}

            <div className="px-3 py-2">
                <h3 className="mb-2 px-4 text-xs font-semibold uppercase text-muted-foreground tracking-wider">
                    Global
                </h3>
                <div className="space-y-1">
                    {globalItems.map((item) => (
                        <Button
                            key={item.href}
                            variant={isActive(item) ? "secondary" : "ghost"}
                            className="w-full justify-start"
                            asChild
                        >
                            <Link to={item.href}>
                                <item.icon className="mr-2 h-4 w-4" />
                                {item.name}
                            </Link>
                        </Button>
                    ))}
                </div>
            </div>

            <div className="mt-auto px-3 py-2">
                <Separator className='my-2' />
                <div className="space-y-1">
                    {settingsItems.map((item) => (
                        <Button
                            key={item.href}
                            variant={isActive(item) ? "secondary" : "ghost"}
                            className="w-full justify-start"
                            asChild
                        >
                            <Link to={item.href}>
                                <item.icon className="mr-2 h-4 w-4" />
                                {item.name}
                            </Link>
                        </Button>
                    ))}
                </div>
            </div>
        </div>
    );
}


export default function Layout() {
    const [open, setOpen] = useState(false);

    return (
        <div className="flex min-h-screen w-full flex-col md:flex-row bg-background">
            {/* Mobile Sidebar */}
            <Sheet open={open} onOpenChange={setOpen}>
                <SheetTrigger asChild>
                    <Button variant="ghost" size="icon" className="md:hidden fixed top-3 left-3 z-50">
                        <Menu className="h-5 w-5" />
                        <span className="sr-only">Toggle Sidebar</span>
                    </Button>
                </SheetTrigger>
                <SheetContent side="left" className="w-[240px] p-0 pt-8 sm:w-[300px]">
                    <Sidebar />
                </SheetContent>
            </Sheet>

            {/* Desktop Sidebar */}
            <aside className="hidden md:block w-[240px] border-r">
                <Sidebar />
            </aside>

            {/* Main Content */}
            <div className="flex flex-col flex-1">
                <header className="md:hidden sticky top-0 flex h-14 items-center gap-4 border-b bg-background px-4 sm:px-6">
                    {/* Header content for mobile if needed, e.g., breadcrumbs */}
                </header>
                <main className="flex-1 p-4 sm:p-6 lg:p-8 bg-muted/30">
                    <Outlet />
                </main>
            </div>
        </div>
    );
}
