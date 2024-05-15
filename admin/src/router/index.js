import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import BrowseView from '../views/BrowseView.vue'
import RestaurantView from '../views/RestaurantView.vue'
import AdminView from '../views/AdminView.vue'
import LogIn from '../views/LogIn.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/browse',
    name: 'browse',
    component: BrowseView
  },
  {
    path:'/restaurant/:id',
    name: 'restaurant',
    component: RestaurantView
  },
  {
    path: '/admin',
    name: 'admin',
    component: AdminView
  },
  {
    path: '/login',
    name: 'login',
    component: LogIn
  },
]

const router = new VueRouter({
  routes
})

export default router
