
import { Outlet, Link, useLocation } from 'react-router-dom';
import { cn } from '@/lib/utils';
import { Button } from '@/components/ui/button';
import {
    LayoutDashboard,
    Tags,
    History,
    Menu,
} from 'lucide-react';
import { useState } from 'react';
import { Sheet, SheetContent, SheetTrigger } from '@/components/ui/sheet';

interface SidebarProps extends React.HTMLAttributes<HTMLDivElement> { }

export function Sidebar({ className }: SidebarProps) {
    const location = useLocation();
    const pathname = location.pathname;

    const items = [
        { name: 'Tasks', href: '/tasks', icon: LayoutDashboard },
        { name: 'Tags', href: '/tags', icon: Tags },
        { name: 'History', href: '/history', icon: History },
    ];

    return (
        <div className={cn("pb-12", className)}>
            <div className="space-y-4 py-4">
                <div className="px-3 py-2">
                    <h2 className="mb-2 px-4 text-lg font-semibold tracking-tight">
                        Hub UI
                    </h2>
                    <div className="space-y-1">
                        {items.map((item) => (
                            <Button
                                key={item.href}
                                variant={pathname === item.href ? "secondary" : "ghost"}
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
        </div>
    );
}

export default function Layout() {
    const [open, setOpen] = useState(false);

    return (
        <div className="flex min-h-screen flex-col md:flex-row">
            {/* Mobile Sidebar */}
            <Sheet open={open} onOpenChange={setOpen}>
                <SheetTrigger asChild>
                    <Button variant="outline" size="icon" className="md:hidden m-4 fixed top-0 left-0 z-50">
                        <Menu className="h-4 w-4" />
                    </Button>
                </SheetTrigger>
                <SheetContent side="left" className="w-[240px] sm:w-[300px]">
                    <Sidebar />
                </SheetContent>
            </Sheet>

            {/* Desktop Sidebar */}
            <div className="hidden md:block w-[240px] border-r min-h-screen bg-background">
                <Sidebar />
            </div>

            {/* Main Content */}
            <main className="flex-1 p-8 pt-16 md:pt-8 bg-muted/10 min-h-screen">
                <Outlet />
            </main>
        </div>
    );
}
