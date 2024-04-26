<script setup lang="ts">
import {getCurrentInstance, onMounted, ref} from "vue";

const instance = getCurrentInstance()
const echarts = instance?.appContext.config.globalProperties.$echarts
const domRef = ref(null)
const option = {
  textStyle: {
    fontFamily: 'YouSheTitleHei',
  },
  tooltip: {
    trigger: 'item'
  },
  title:{
    text:"课程标准",
    textStyle:{
      color:'#fff'
    }
  },
  legend: {
    orient: 'vertical',
    top: '80%',
    left: 'right',
    textStyle:{
      fontSize: 18,//字体大小
      color: '#ffffff'//字体颜色
    }
  },
  series: [
    {
      name: '考核标准',
      type: 'pie',
      radius: ['40%', '70%'],
      avoidLabelOverlap: false,
      label: {
        show: false,
        position: 'center',
      },
      emphasis: {
        label: {
          show: true,
          fontSize: 40,
          fontWeight: 'bold'
        }
      },
      labelLine: {
        show: false
      },
      data: [
        { value: 0.5*0.2*100, name: '考勤' },
        { value: 0.5*0.6*100, name: '实验作业' },
        { value: 0.5*0.2*100, name: '期中成绩' },
        { value: 0.5*100, name: '期末' },
      ]
    }
  ]
};
onMounted(()=>{
  let myChart = echarts.init(domRef.value)
  myChart.setOption(option)
})
</script>

<template>
<div ref="domRef" style="width: 100%;height: 100%"></div>
</template>

<style scoped lang="scss">

</style>