<template>
  <div id="pie" style="width:25rem;height:15rem;"></div>
</template>
<script lang="ts" setup>
import {onMounted, ref, getCurrentInstance} from "vue";
import request from "../request";
// @ts-ignore
const {proxy} = getCurrentInstance()

const option: any = ref({
  title: {
    text: '男女比例',
    subtext: '男女生数量',
    left: 'center',
    textStyle: {
      //文字颜色
      color: '#ffffff',
      //字体风格,'normal','italic','oblique'
      fontStyle: 'normal',
      //字体粗细 'normal','bold','bolder','lighter',100 | 200 | 300 | 400...
      fontWeight: 'bold',
      //字体系列
      fontFamily: 'sans-serif',
      //字体大小
      fontSize: 18
    }
  },
  tooltip: {
    trigger: 'item'
  },
  legend: {
    orient: 'vertical',
    left: 'left',
    textStyle:{//图例文字的样式
      color:'#ccc',
      fontSize:16
    }
  },
  series: [
    {
      name: '人数',
      type: 'pie',
      radius: '50%',
      data: [],
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0, 0, 0, 0.5)'
        }
      }
    }
  ]
})
onMounted(async () => {
  let response = await request.get("/student/getGender")

  option.value.series[0].data.push({value: response.data.female, name: '女生'})
  option.value.series[0].data.push({value: response.data.male, name: '男生'})
  let myechart = proxy.$echarts.init(document.getElementById('pie'))
  myechart.setOption(option.value)
})
</script>