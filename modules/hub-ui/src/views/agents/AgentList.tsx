
import { useState } from 'react';
import { useConfiguredAgentsQuery } from '@/api/queries/useConfiguredAgentsQuery';
import { DataTable } from '@/components/ui/data-table';
import { getColumns } from './columns';

export default function AgentList() {
    const [pagination, setPagination] = useState({ pageIndex: 0, pageSize: 10 });

    const { data, isLoading } = useConfiguredAgentsQuery({
        offset: pagination.pageIndex * pagination.pageSize,
        limit: pagination.pageSize,
    });

    const columns = getColumns();
    const pageCount = data ? Math.ceil((data.total_count ?? 0) / pagination.pageSize) : 0;

    return (
        <div className="space-y-4">
            <div className="flex justify-between items-center">
                <h2 className="text-3xl font-bold tracking-tight">Agents</h2>
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
