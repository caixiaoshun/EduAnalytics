import {createRouter, createWebHashHistory, RouteRecordRaw} from "vue-router";

const routes:Array<RouteRecordRaw> = [
    {
        path:'/',
        name:'index',
        redirect:'home',
        children:[
            {
                path:'home',
                component:()=>import('../views/Home.vue')
            }
        ]
    }
]

const router = createRouter({
    history:createWebHashHistory(),
    routes
})

export default router