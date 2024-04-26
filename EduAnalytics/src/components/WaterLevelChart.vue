<script setup lang="ts">

import {onMounted,getCurrentInstance} from "vue";
const internalInstance = getCurrentInstance()
const echarts = internalInstance?.appContext.config.globalProperties.$echarts
const props = defineProps({
  title:{
    type: String,
    default: '水位图'
  },
  waterLevel: {
    type: Number,
    default: 70
  },
  documentId:{
    type:String,
    default:'water-level-chart'
  }

})
const option = {
  textStyle: {
    fontFamily: 'YouSheTitleHei',
  },
  backgroundColor: "#0e2147",
  title: {
    show: true,
    text: props.title,
    x: '50%',
    y: '60%',
    z: 10,
    textAlign: 'center',
    textStyle: {
      color: '#ffffff',
      fontSize: 14,
      fontWeight: 500
    },
  },
  series: [{
    name: '违规项',
    type: 'liquidFill',
    radius: '60%',
    center: ['50%', '45%'],
    data: [ props.waterLevel /100],
    label:{
      normal:{
        textStyle:{
          color: '#ffffff',
          fontSize: 14,
        }
      }
    },
    color: ['#4366f3'],
    backgroundStyle: {
      color: 'rgba(39,115,229,0.12)'
    },
    outline: {
      borderDistance: 0,
      itemStyle: {
        borderWidth: 5,
        borderColor: 'rgba(49,102,255,0.5)',
      }
    },
    // amplitude: 0,
  }]
}
onMounted(()=>{
  const myChart = echarts.init(document.getElementById(props.documentId))
  myChart.setOption(option)
})
</script>

<template>
  <div :id="props.documentId" :style="{ width: '100%', height: '100%' }"></div>
</template>

<style scoped lang="scss">

</style>