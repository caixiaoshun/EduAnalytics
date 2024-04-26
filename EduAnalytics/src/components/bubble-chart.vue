<script setup lang="ts">

import {getCurrentInstance, onBeforeMount, onMounted, reactive} from 'vue'
import {request} from "@/request";

const instance = getCurrentInstance()
const echarts = instance?.appContext.config.globalProperties.$echarts
const option = reactive({
  textStyle: {
    fontFamily: 'YouSheTitleHei',
  },
  backgroundColor: new echarts.graphic.RadialGradient(0.3, 0.3, 0.8, [
    {
      offset: 0,
      color: '#42454b'
    },
    {
      offset: 1,
      color: '#093275'
    }
  ]),
  title: {
    text: '当前学生成绩',
    left: '5%',
    top: '3%',
    textStyle: {
      color: '#fff'
    }
  },
  legend: {
    show: false
  },
  xAxis: {
    type: 'category',
    data: null,
    axisLabel: {
      color: '#fff'
    }

  },
  yAxis: {
    type: 'value',
    axisLabel: {
      color: '#fff'
    }
  },
  series: [
    {
      name: '分数',
      data: null,
      type: 'scatter',
      itemStyle: {
        shadowBlur: 10,
        shadowColor: 'rgba(25, 100, 150, 0.5)',
        shadowOffsetY: 5,
        color: new echarts.graphic.RadialGradient(0.4, 0.3, 1, [
          {
            offset: 0,
            color: 'rgb(251, 118, 123)'
          },
        ])
      },
      symbolSize: function (data: any) {
        return Math.sqrt(data[1]) * 5;
      },
      emphasis: {
        focus: 'series',
        label: {
          show: true,
          color: '#3bd992',
          formatter: function (param: any) {
            return param.data[0] + ':' + param.data[1];
          },
          position: 'top'
        }
      },
    },
  ]
});
const init = async () => {
  let response = await request.get("/getBubbleData")
  let data = response.data.data
  option.xAxis.data = data.map(function (item: any) {
    return item[0]
  })
  option.series[0].data = data.map(function (item: any) {
    return [item[0], item[1], item[1] * item[1]]
  })
  let myEcharts = echarts.init(document.getElementById('bubble-chart'))
  myEcharts.setOption(option)
}
onMounted(() => {
  init()
})
const interval = setInterval(()=>{
  init()
},1000*5)
onBeforeMount(()=>{
  clearInterval(interval)
})
</script>

<template>
  <div id="bubble-chart" style="height: 90%;width: 90%"></div>
</template>

<style scoped lang="scss">

</style>