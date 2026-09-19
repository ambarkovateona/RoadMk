import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RoadsView from '../views/RoadsView.vue'
import AboutView from '../views/AboutView.vue'
import ContactView from '../views/ContactView.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: HomeView },
    { path: '/roads', component: RoadsView },
    { path: '/about', component: AboutView },
    { path: '/contact', component: ContactView },
  ]
})

export default router