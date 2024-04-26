<script setup lang="ts">
import {onMounted, getCurrentInstance, ref} from "vue";
import {request} from "@/request";

// @ts-ignore
const {proxy} = getCurrentInstance()
const data = ref()
const option = ref(
    {
      textStyle: {
        fontFamily: 'YouSheTitleHei',
      },
      title:{
        show:true,
        text:"学生课堂表现",
        x:'center',
        y:'top',
        textStyle:{
          color:'#fff',//'red'，字体颜色
          fontStyle:'normal',//'italic'(倾斜) | 'oblique'(倾斜体) ，字体风格
          fontWeight:'normal',//'bold'(粗体) | 'bolder'(粗体) | 'lighter'(正常粗细) ，字体粗细
          // 'Microsoft YaHei'(微软雅黑) ，文字字体
          fontSize:18,//字体大小
          lineHeight:18,//字体行高
        },
      },
      tooltip: {
        show:true,
        trigger: 'item',
        triggerOn:'mousemove',
        showContent: true,
        backgroundColor: 'rgba(50,50,50,0.7)',
        formatter: function (params:any) {
          // console.log(params);
          // 自定义 tooltip 内容的格式
          // return "hello world"
          return params.value[0] + '<br/>' + params.value[1] + '<br/>' + params.value[2]+'分';
        },
        textStyle:{
          color:'#fff'
        }
      },
      grid3D: {},
      xAxis3D: {
        type: 'category',
        lineStyle:{
          color:'white',
          width:3,
          type:'solid',
          opacity:1
        },
        nameTextStyle:{
          color:'white',
          fontSize:18
        },
        name:'学生姓名',
        axisLabel:{
          rotate:30,
          color:'white'
        }
      },
      yAxis3D: {
        type: 'category',
        name:"课程",
        lineStyle:{
          color:'white',
          width:3,
          type:'solid',
          opacity:1
        },
        nameTextStyle:{
          color:'white',
          fontSize:18
        },
        axisLabel:{
          rotate:30,
          color:'white'
        }
      },
      zAxis3D: {
        lineStyle:{
          color:'white',
          width:3,
          type:'solid',
          opacity:1
        },
        nameTextStyle:{
          color:'white',
          fontSize:18
        },
        axisLabel:{
          rotate:30,
          color:'white'
        },
        name:"得分"
      },
      dataset: {
        source: null
      },
      series: [{
        type: 'scatter3D',
        symbolSize: 2.5,
        data: null,
        itemStyle: {
          color: 'rgba(59,178,69,0.8)'
        }
      }]
    }
)
const myechart = ref()
const spinning = ref(true)
onMounted(async () => {
  let response = await request.get("/getStudentPerformer")
  // xAxis.value = response.data['xAxis']
  // yAxis.value = response.data['yAxis']
  data.value = response.data['data']

  // option.value.xAxis3D = xAxis.value
  // option.value.yAxis3D = yAxis.value
  option.value.dataset.source = data.value

  myechart.value = proxy.$echarts.init(document.getElementById('heatMap'))
  myechart.value.setOption(option.value)
  spinning.value = false
})
</script>

<template>
  <a-spin :spinning="spinning" style="width: 100%;height: 100%">
    <div style="height: 400px;width: 600px;display: inline-block" id="heatMap"></div>
  </a-spin>

</template>

<style scoped>

</style>