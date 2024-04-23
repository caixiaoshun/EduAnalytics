import { createRouter, createWebHistory } from 'vue-router'

// @ts-ignore
import NProgress from 'nprogress' // progress bar
import 'nprogress/nprogress.css' // progress bar style


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
    },
    {
      path:'/courseOverView',
      name:'courseOverView',
      component:()=>import('@/views/CourseOverview.vue')
    }
  ]
})

router.beforeEach((to,from,next)=>{
  NProgress.start()
  next(true)
})

router.afterEach((to,from)=>{
  NProgress.done()
})

export default router
