<script setup lang="ts">
import {request} from "@/request";
import {getCurrentInstance, onMounted, reactive, ref, watch} from "vue";
import {useClusterStore} from "@/stores/clusterStore";
import {storeToRefs} from "pinia";

const {cluster, score, method,spinning} = storeToRefs(useClusterStore())

function getCurrentYearMonth(): string {
  const now = new Date(); // 获取当前时间
  const year = now.getFullYear(); // 获取年份
  const month = now.getMonth() + 1; // 获取月份，注意 getMonth() 返回的月份是从 0 开始的
  const monthString = month < 10 ? '0' + month : month.toString(); // 确保月份是两位数
  return `${year}/${monthString}`; // 返回格式化的字符串
}

const internalInstance = getCurrentInstance()
const echarts = internalInstance?.appContext.config.globalProperties.$echarts

// 聚类相关的一些变量
const clusterAllData = ref()
const optionData = ref()
const option = reactive({
  textStyle: {
    fontFamily: 'YouSheTitleHei',
  },
  title: {
    text: '学生聚类分析',
    subtext: getCurrentYearMonth(),
    left: 'center',
    textStyle: {
      //文字颜色
      color: '#ccc',
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
  series: [
    {
      type: 'treemap',
      data: []
    }
  ],
  tooltip: {
    formatter: function (info: any) {
      //@ts-ignore
      let student = clusterAllData.value.data.filter((obj) => {
        return obj['姓名'] === info.name
      })[0]
      return `<div style="text-align: left;">`
          + `姓名: ${student['姓名']}<br/>`
          + `学号: ${student['学号']}<br/>`
          + `性别: ${student['性别']}<br/>`
          + `班级: ${student['班级']}<br/>`
          + `自评: ${student['自评']}<br/>`
          + `课堂表现记录: ${student['课堂表现记录']}<br/>` + `</div>`;
    }
  },
})

const CreateOptionData = () => {
  optionData.value = []
  for (let i = 0; i < cluster.value; i++) {
    //@ts-ignore
    let labelData = clusterAllData.value.data.filter((obj) => {
      return obj.label === i
    })
    let obj = {
      name: `类别${i + 1}`,
      value: labelData.length,
      children: []
    }
    for (let j = 0; j < labelData.length; j++) {
      let tmp = {
        name: labelData[j]['姓名'],
        value: 1
      }
      // @ts-ignore
      obj.children.push(tmp)
    }
    optionData.value.push(obj)
  }
}
const init = async () => {
  spinning.value = true
  let response = await request.get("/getStudentCluster", {
    params: {
      method: method.value,
      cluster: cluster.value,
    }
  })
  spinning.value = false
  score.value = response.data.score
  let myEchart = echarts.init(document.getElementById('student-cluster'))
  clusterAllData.value = response.data
  cluster.value = response.data.cluster
  CreateOptionData()
  option.series[0].data = optionData.value
  myEchart.setOption(option)
}
onMounted(async () => {
  await init()
})
defineExpose({
  init
});
</script>

<template>
  <div id="student-cluster" style="width: 100%;height: 100%"></div>
</template>

<style scoped lang="scss">

</style>