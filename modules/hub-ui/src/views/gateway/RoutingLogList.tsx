
import { useState } from 'react';
import { useRoutingLogsQuery } from '@/api/queries/useRoutingLogsQuery';
import { DataTable } from '@/components/ui/data-table';
import { getColumns } from './RoutingLogColumns';

export default function RoutingLogList() {
    const [pagination, setPagination] = useState({ pageIndex: 0, pageSize: 10 });

    const { data, isLoading } = useRoutingLogsQuery({
        offset: pagination.pageIndex * pagination.pageSize,
        limit: pagination.pageSize,
    });

    const columns = getColumns();
    const pageCount = data ? Math.ceil((data.total_count ?? 0) / pagination.pageSize) : 0;

    return (
        <div className="space-y-4">
            <div className="flex justify-between items-center">
                <h2 className="text-3xl font-bold tracking-tight">Routing Logs</h2>
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
