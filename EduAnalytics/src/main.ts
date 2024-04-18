import '@/reset.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import DataVVue3 from '@kjgl77/datav-vue3'
import App from './App.vue'
import router from './router'
import * as echarts from 'echarts'
const app = createApp(App)


app.config.globalProperties.$echarts = echarts
app.use(createPinia())
app.use(router)
app.use(DataVVue3)
app.mount('#app')
