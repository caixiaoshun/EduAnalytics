<script setup lang="ts">
import {onMounted,getCurrentInstance} from "vue";
const Instance = getCurrentInstance()
const echarts = Instance?.appContext?.config.globalProperties.$echarts
const data = [
  [20, 15, 15, 30, 10, 10]
];
const option = {
  textStyle: {
    fontFamily: 'YouSheTitleHei',
  },
  title: {
    text: '指标体系',
    left: 'left',
    textStyle: {
      color: '#eee'
    }
  },
  legend: {
    show:false
  },
  tooltip: {
    trigger: 'axis'
  },
  radar: {
    indicator: [
      { name: '课堂表现', max: 30 },
      { name: '自评成绩', max: 25 },
      { name: '他评成绩', max: 25 },
      { name: '作业成绩', max: 40 },
      { name: '期中成绩', max: 15 },
      { name: '期末成绩', max: 15 }
    ],
    axisName: {
      color: 'rgb(238, 197, 102)'
    },
    axisLine: {
      lineStyle: {
        color: 'rgba(238, 197, 102, 0.5)'
      }
    },
    splitLine: {
      lineStyle: {
        color: [
          'rgba(238, 197, 102, 0.1)',
          'rgba(238, 197, 102, 0.2)',
          'rgba(238, 197, 102, 0.4)',
          'rgba(238, 197, 102, 0.6)',
          'rgba(238, 197, 102, 0.8)',
          'rgba(238, 197, 102, 1)'
        ].reverse()
      }
    },
  },
  series: [
    {
      name: '指标体系',
      type: 'radar',
      tooltip:{
        trigger:'item',
      },
      areaStyle: {},
      data: data,
    },
  ]
};
onMounted(()=>{
  let myChart = echarts.init(document.getElementById('radar-chart'))
  myChart.setOption(option)
})
</script>

<template>
<div id="radar-chart" style="width: 100%;height: 100%"></div>
</template>

<style scoped lang="scss">

</style>