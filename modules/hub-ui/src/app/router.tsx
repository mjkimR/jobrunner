import { createBrowserRouter, Navigate } from 'react-router-dom';
import Layout from '../views/Layout';
import HomeView from '../views/HomeView';
import TaskList from '../views/tasks/TaskList';
import TaskTagList from '../views/tags/TaskTagList';
import TaskHistoryList from '../views/history/TaskHistoryList';
import WorkspaceList from '../views/workspaces/WorkspaceList';
import AgentList from '../views/agents/AgentList';
import GatewayLayout from '../views/gateway/GatewayLayout';
import ConversationList from '../views/gateway/ConversationList';
import ConversationDetail from '../views/gateway/ConversationDetail';
import RoutingLogList from '../views/gateway/RoutingLogList';

export const router = createBrowserRouter([
  {
    path: '/',
    element: <Layout />,
    children: [
      {
        index: true,
        // Redirect to a default workspace path, which will be handled by logic in WorkspaceSelector
        element: <HomeView />,
      },
      {
        path: 'workspaces/:workspaceId',
        children: [
            {
                index: true,
                element: <Navigate to="tasks" replace />
            },
            {
                path: 'tasks',
                element: <TaskList />,
            },
            {
                path: 'tags',
                element: <TaskTagList />,
            },
            {
                path: 'history',
                element: <TaskHistoryList />,
            },
            {
                path: 'gateway',
                element: <GatewayLayout />,
                children: [
                    {
                        index: true,
                        element: <Navigate to="conversations" replace />
                    },
                    {
                        path: 'conversations',
                        element: <ConversationList />,
                    },
                    {
                        path: 'conversations/:conversationId',
                        element: <ConversationDetail />,
                    },
                    {
                        path: 'logs',
                        element: <RoutingLogList />,
                    }
                ]
            }
        ]
      },
      {
        path: 'agents',
        element: <AgentList />,
      },
      {
        path: 'settings',
        children: [
            {
                index: true,
                element: <Navigate to="workspaces" replace />
            },
            {
                path: 'workspaces',
                element: <WorkspaceList />,
            }
        ]
      }
    ],
  },
]);
