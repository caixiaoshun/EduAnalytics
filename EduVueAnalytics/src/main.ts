import {createApp} from 'vue'
import DataVVue3 from '@kjgl77/datav-vue3'
import App from './App.vue'
import './reset.css'
import router from "./router";
// @ts-ignore
import * as echarts from 'echarts';//引入echarts
const app = createApp(App)
app.config.globalProperties.$echarts = echarts
app.use(DataVVue3)
app.use(router)
app.mount('#app')
