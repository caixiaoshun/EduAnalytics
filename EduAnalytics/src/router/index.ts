import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Welcome from "@/views/welcome.vue";
import CourseOverview from "@/views/CourseOverview.vue";
// @ts-ignore
import NProgress from 'nprogress' // progress bar
import 'nprogress/nprogress.css' // progress bar style


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:'/home',
      name:'home',
      component:Home
    },
    {
      path:'/',
      name:'welcome',
      component:Welcome
    },
    {
      path:'/courseOverView',
      name:'courseOverView',
      component:CourseOverview
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
