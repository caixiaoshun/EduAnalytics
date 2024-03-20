<template>
  <div style="width: 100%;height: 500px">
    <div id="acrossChart" style="width: 100%;height: 100%"></div>
  </div>
</template>

<script setup lang="ts">

import {onMounted, ref, getCurrentInstance} from "vue";
import request from "../request/index.ts";
// @ts-ignore
const {proxy} = getCurrentInstance()
const mychart = ref()
const colors = [
  '#FF0000', '#FF4500', '#FF7E00', '#FFD700', '#FFFF00',
  '#9ACD32', '#87CEEB', '#6495ED', '#4169E1', '#8B0000',
  '#B22222', '#A52A2A', '#800080', '#800000', '#8B4513',
  '#A0522D', '#CD853F', '#DAA520', '#D2B48C', '#D3D3D3',
  '#B0E0E6', '#32CD99', '#00FA9A', '#20B2AA', '#40E0D0',
  '#7FFF00', '#7CFC00', '#00CED1', '#00FFFF', '#FFA07A'
];
let count = 1
const dataArr = ref([])
const option: any = ref({
  xAxis: {
    max: 'dataMax',
    name: '分数',
    axisLabel: {
      show: true,
      fontFamily: '微软雅黑',
      color: "#fff",
      fontSize: '16',
    }
  },
  yAxis: {
    type: 'category',
    // @ts-ignore
    data: null,
    inverse: true,
    animationDuration: 300,
    animationDurationUpdate: 300,
    max: 30,// only the largest 3 bars will be displayed
    axisLabel: {
      textStyle: {
        show: true,
        fontFamily: '微软雅黑',
        color: "#fff",
        fontSize: '16',
      }
    }
  },
  series: [
    {
      realtimeSort: true,
      name: '分数',
      type: 'bar',
      data: null,
      label: {
        show: true,
        position: 'right',
        valueAnimation: true
      },
      itemStyle: {
        color: function (params: any) {
          return colors[params.dataIndex] || '#5470c6';
        }
      }
    }
  ],
  legend: {
    show: true,
    textStyle: {
      color: '#fff'
    }
  },
  animationDuration: 0,
  animationDurationUpdate: 3000,
  animationEasing: 'linear',
  animationEasingUpdate: 'linear'
})
const updateData = (index: number) => {
  if(index>=dataArr.value.length){
    return;
  }
  // @ts-ignore
  option.value.yAxis.data = dataArr.value[index].name
  // @ts-ignore
  option.value.series[0].data = dataArr.value[index].scores
  // @ts-ignore
  option.value.xAxis.name = dataArr.value[index].cdate
  // @ts-ignore
  option.value.series[0].name = dataArr.value[index].cdate + "排名"
  mychart.value.setOption(option.value)
  if (index > 0) {
    count += 1
  }
}

const init = async ()=>{
  mychart.value = proxy.$echarts.init(document.getElementById('acrossChart'))
  let response = await request.get("/student/getSelfAssessment")
  dataArr.value = Object.values(response.data)
  updateData(0)
}
onMounted( () => {
  init()
})

setInterval(()=>{
  updateData(count)
},3000)
</script>
