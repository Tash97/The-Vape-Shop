import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ProductPage from '../views/ProductPage.vue'
import CategoryPage from '@/views/CategoryPage.vue'
import AdminAddProduct from '@/views/AdminAddProduct.vue'
import Admin from '@/views/Admin.vue'
import AdminDashboard from '@/views/AdminDashboard.vue'
import AdminProducts from '@/views/AdminProducts.vue'
import AdminSales from '@/views/AdminSales.vue'
import AdminCustomers from '@/views/AdminCustomers.vue'
import AdminAnalytics from '@/views/AdminAnalytics.vue'
import AdminNotifications from '@/views/AdminNotifications.vue'
import AdminSettings from '@/views/AdminSettings.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
        path: '/productpage/:name',
        name: 'productPage',
        component: ProductPage,
        meta: {
            title: 'Results'
        }
    },
    {
      path: '/categories/:category',
      name: 'categoryPage',
      component: CategoryPage,
      meta: {
          title: 'Category'
      }
  },
  {
    path: '/admin/',
    name: 'admin',
    component: Admin,
    meta: {
        title: 'Admin'
    },
    children: [
      {
        path: 'dashboard',
        name: 'adminDashboard',
        component: AdminDashboard,
      },
      {
        path: 'products/:category?',
        name: 'adminProducts',
        component: AdminProducts,
      },
      {
        path: 'sales',
        name: 'adminSales',
        component: AdminSales,
      },
      {
        path: 'customers',
        name: 'adminCustomers',
        component: AdminCustomers,
      },
      {
        path: 'analytics',
        name: 'adminAnalytics',
        component: AdminAnalytics,
      },
      {
        path: 'notifications',
        name: 'adminNotifications',
        component: AdminNotifications,
      },
      {
        path: 'settings',
        name: 'adminSettings',
        component: AdminSettings,
      },
    ],
},
  ]
})

export default router
