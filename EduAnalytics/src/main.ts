import '@/reset.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import DataVVue3 from '@kjgl77/datav-vue3'
import App from './App.vue'
import router from './router'
import * as echarts from 'echarts'
import 'ant-design-vue/dist/reset.css';
import Antd from 'ant-design-vue';
import 'echarts-liquidfill'
import "echarts-gl"
import 'echarts-wordcloud'
import 'animate.css';
import Particles from "particles.vue3";
const app = createApp(App)


app.config.globalProperties.$echarts = echarts
app.use(createPinia())
app.use(Particles)
app.use(Antd)
app.use(router)
app.use(DataVVue3)
app.mount('#app')
