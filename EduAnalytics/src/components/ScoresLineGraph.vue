<script setup lang="ts">
interface Series {
  name: string,
  type: string,
  stack: string,
  smooth: boolean,
  lineStyle: any,
  showSymbol: boolean,
  areaStyle: {
    opacity: number,
    color: any
  },
  emphasis: any,
  data: Array<number>
}

import {getCurrentInstance, onMounted, reactive, type Ref, ref} from "vue";
import {request} from "@/request";

const internalInstance = getCurrentInstance()
const echarts = internalInstance?.appContext.config.globalProperties.$echarts
const legend: Ref<Array<string>> = ref([])
const names: Ref<Array<string>> = ref([])
const series: Ref<Array<Series>> = ref([])
const option = reactive({
  textStyle: {
    fontFamily: 'YouSheTitleHei',
  },
  title: {
    text: '课程情况',
    left: 'center',
    top: 'top',
    textStyle: {
      fontSize: 20,
      color: '#fff',
      fontWeight: 'bold'
    },
  },
  tooltip: {
    trigger: 'axis'
  },
  legend: {
    data: ['123'],
    x:'left',
    y:'bottom',
    textStyle: {
      color: 'white',
      fontSize: '16px',
      fontWeight: 700
    }
  },
  yAxis: {
    type: 'value',
    axisLabel:{
      rotate:0,
      color:'#fff',
    }
  },
  xAxis: {
    type: 'category',
    boundaryGap: false,
    data: ['123'],
    axisLabel:{
      rotate:0,
      color:'#fff',
    }
  },
  series: []
});
onMounted(async () => {
  let response = await request.get("getStudentGrade")
  legend.value = response.data.columns
  names.value = []
  let data = response.data.data
  for (let i = 0; i < data.length; i++) {
    names.value.push(data[i]['姓名'])
  }
  for (let i = 0; i < legend.value.length; i++) {
    let curLegend = legend.value[i]
    let tempData: Array<number> = []
    for (let j = 0; j < data.length; j++) {
      tempData.push(data[j][curLegend])
    }
    let obj: Series = {
      name: curLegend,
      type: 'line',
      stack: 'Total',
      smooth: true,
      lineStyle: {
        width: 0
      },
      showSymbol: false,
      areaStyle: {
        opacity: 0.8,
        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
          {
            offset: 0,
            color: '#7D45C4'
          },
          {
            offset: 1,
            color: 'rgba(119,103,140,0.85)'
          }
        ])
      },
      emphasis: {
        focus: 'series'
      },
      data: tempData
    }
    series.value.push(obj)
  }

  option.legend.data = legend.value
  option.xAxis.data = names.value
  // @ts-ignore
  option.series = series.value

  const myChart = echarts.init(document.getElementById('line-graph'))
  myChart.setOption(option)
})
</script>

<template>

  <div id="line-graph">

  </div>
</template>

<style scoped lang="scss">
#line-graph {
  height: 100%;
  width: 100%;
}
</style>