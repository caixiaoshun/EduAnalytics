<script setup lang="ts">
import {getCurrentInstance, onMounted, reactive} from "vue";
import {request} from "@/request";
const Instance = getCurrentInstance()
const echarts = Instance?.appContext?.config.globalProperties.$echarts
const props = defineProps({
  url:{
    required:true,
    type:String
  },
  documentId:{
    required:true,
    type:String
  },
  title:{
    required:true,
    type:String
  },
})
const option = reactive({
  textStyle: {
    fontFamily: 'YouSheTitleHei',
  },
  title:{
    text:props.title,
    left:'center',
    textStyle:{
      //文字颜色
      color:'#ccc',
      //字体风格,'normal','italic','oblique'
      fontStyle:'normal',
      //字体粗细 'normal','bold','bolder','lighter',100 | 200 | 300 | 400...
      fontWeight:'bold',
      //字体系列
      fontFamily:'sans-serif',
      //字体大小
      fontSize:18
    }
  },
  backgroundColor: '#081736',
  tooltip: {
    trigger: 'axis',
  },
  grid: {
    top: '25%',
    right: '5%',
    left: '10%',
    bottom: '36%'
  },

  xAxis: [{
    name: '姓名',
    type: 'category',
    axisLabel: {
      color: '#fff'
    },
    axisLine: {
      show: true,
      lineStyle: {
        color: '#fff'
      }
    },
    axisTick: {
      show: false,
    },
    splitLine: {
      show: false,
      lineStyle: {
        color: '#195384',
        type: "dotted",
      }
    },
    data: ["1","2","3","4","5","6","7","8","9","10","11","12"]
  }],
  yAxis: [
    {
      type: 'value',
      name: "分数",
      min: 0,
      position: 'left',
      nameTextStyle: {
        color: "#fff",
        fontSize: 11,
      },
      axisLine: {
        show: true,
        lineStyle: {
          color: '#fff'
        }
      },
      axisTick: {
        show: false,
      },
      splitLine: {
        show: true,
        lineStyle: {
          color: '#0a3e98',
          type: "dotted",
        }
      },
      axisLabel: {
        formatter: '{value}',
        textStyle: {
          color: "#fff",
        }
      },
    }
  ],
  series: [
    {
      name:'分数',
      type: 'line',
      smooth: true, //是否平滑
      showAllSymbol: false,
      symbol: 'circle',
      symbolSize: 10,
      lineStyle: {
        normal: {
          color: "#7F4CEF",
        },
      },
      label: {
        show: false,
      },
      itemStyle: {
        color: "#fff",
        borderColor: "#7F4CEF",
        borderWidth: 3,
      },
      areaStyle: {
        normal: {
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
            offset: 0,
            color: 'RGBA(127, 76, 239, 1)'
          },
            {
              offset: 1,
              color: 'RGBA(127, 76, 239, 0.2)'
            }
          ], false),
          shadowColor: 'RGBA(80, 38, 72, 0.2)',
          shadowBlur: 20
        }
      },
      data: ["0","0","0","0","0","0","0","0","0","5000","7689","14839"]
    }
  ]
})
onMounted(async ()=>{
  let result = await request.get(props.url)
  let data = result.data.data
  let names = []
  let scores = []
  for (let i = 0; i < data.length; i++) {
    names.push(data[i][0])
    scores.push(data[i][1])
  }
  option.xAxis[0].data = names
  option.series[0].data = scores
  let myChart = echarts.init(document.getElementById(props.documentId))
  myChart.setOption(option)
})
</script>

<template>
<div :id="props.documentId" style="width: 100%;height: 100%"></div>
</template>

<style scoped lang="scss">

</style>