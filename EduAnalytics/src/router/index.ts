import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Welcome from "@/views/welcome.vue";
import CourseOverview from "@/views/CourseOverview.vue";
// @ts-ignore
import NProgress from 'nprogress' // progress bar
import 'nprogress/nprogress.css'
import GradesList from "@/views/GradesList.vue";
import ResultAnalysic from "@/views/resultAnalysic.vue"; // progress bar style


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
    },
    {
      path:'/gradesList',
      name:'gradesList',
      component:GradesList
    },
    {
      path:'/resultAnalysic',
      name:'resultAnalysic',
      component:ResultAnalysic
    },
    {
      path:'/secondVersion',
      name:'secondVersion',
      component:Home
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
