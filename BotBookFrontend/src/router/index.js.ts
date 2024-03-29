import { createRouter, createWebHistory} from "vue-router";
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
          },
          {
            path: '/feed',
            component: () => import('../layouts/FeedLayout.vue'),
            children: [
              {
                path: '',
                component: () => import('../pages/FeedPage.vue')
              }
            ]
          },
          {
            path: '/account',
            component: () => import('../layouts/ProfileLayout.vue'),
            children: [
              {
                path: '',
                component: () => import('../pages/Profile.vue')
              }
            ]
          },
          {
            path: '/about',
            component: LandingLayout,
            children: [
              {
                path: '',
                component: () => import('../pages/About.vue')
              }
            ]
          },
          {
              path: '/settings',
              component: () => import('../pages/Settings.vue')
          },
          {
            path: '/createbot',
            component: () => import('../layouts/CreateBotLayout.vue'),
            children: [
              {
                path: '',
                component: () => import('../pages/Createbot.vue')
              }
            ]
          }
        
    ],
    scrollBehavior() {
      return {top: 0}
    }
})

export default router