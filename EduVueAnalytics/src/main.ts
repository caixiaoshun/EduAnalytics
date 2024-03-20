import {createApp} from 'vue'
import DataVVue3 from '@kjgl77/datav-vue3'
import App from './App.vue'
import './reset.css'
import router from "./router";
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import "echarts-gl"
// @ts-ignore
import VueAmazingUI from 'vue-amazing-ui'
import 'vue-amazing-ui/css'
// @ts-ignore
import * as echarts from 'echarts';//引入echarts
const app = createApp(App)
app.config.globalProperties.$echarts = echarts
app.use(DataVVue3)
app.use(ElementPlus)
app.use(router)
app.use(VueAmazingUI)
app.mount('#app')
