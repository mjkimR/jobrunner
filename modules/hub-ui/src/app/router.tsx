import { createBrowserRouter } from 'react-router-dom'
import RootLayout from '../views/RootLayout'
import HomeView from '../views/HomeView'

export const router = createBrowserRouter([
  {
    path: '/',
    element: <RootLayout />,
    children: [
      {
        index: true,
        element: <HomeView />,
      },
    ],
  },
])
