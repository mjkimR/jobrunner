import { createBrowserRouter } from 'react-router-dom';
import Layout from '../views/Layout';
import HomeView from '../views/HomeView';
import TaskList from '../views/tasks/TaskList';
import TaskTagList from '../views/tags/TaskTagList';
import TaskHistoryList from '../views/history/TaskHistoryList';

export const router = createBrowserRouter([
  {
    path: '/',
    element: <Layout />,
    children: [
      {
        index: true,
        element: <HomeView />,
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
    ],
  },
]);
