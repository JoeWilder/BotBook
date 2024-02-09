import { createRouter, createWebHistory} from "vue-router";
import Home from '../views/Home.vue'
import LandingLayout from '../layouts/LandingLayout.vue'
import LandingPage from '../pages/LandingPage.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            component: LandingLayout,
            children: [
              {
                path: '',
                component: LandingPage
              }
            ]
          }
        /*{
            path: '/',
            component: Home
        },
        {
            path: '/about',
            component: () => import('../views/About.vue')
        },
        {
            path: '/settings',
            component: () => import('../views/Settings.vue')
        }
        */
    ]
})

export default router