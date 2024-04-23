import { createRouter, createWebHistory } from 'vue-router'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:'/home',
      name:'home',
      component:()=>import('@/views/Home.vue')
    },
    {
      path:'/',
      name:'welcome',
      component:()=>import('@/views/welcome.vue')
    }
  ]
})

export default router
