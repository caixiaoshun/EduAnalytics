<script setup lang="ts">
import {getCurrentInstance, onMounted, ref} from "vue";
import request from "../request";
import {ElLoading, ElMessage} from "element-plus";
// @ts-ignore
const {proxy} = getCurrentInstance()
const method = ref('Kmeans')
const cluster = ref(3)
const data = ref([])
const names = ref([])
const categorys = ref([])
const title = ref([])
const singleAxis = ref([])
const series = ref([])
const preference = ref(2)
const bandwidth = ref(0.0)
const min_samples = ref(0)
const config = ref({
  data: [55],
  shape: 'round',
})
const options = [
  {
    value: "Kmeans",
    label: "Kmeans"
  },
  {
    value: "Mean Shift",
    label: "Mean Shift"
  },
  {
    value: "Spectral clustering",
    label: "Spectral clustering"
  },
  {
    value: "层次聚类",
    label: "层次聚类"
  },
  {
    value: "DBSCAN",
    label: "DBSCAN"
  },
  {
    value: "OPTICS",
    label: "OPTICS"
  },

]
const init = async () => {
  let response = await request.get("/getStudentCluster", {
    params: {
      method: method.value,
      cluster: cluster.value,
      preference:preference.value,
      bandwidth:bandwidth.value,
      min_samples:min_samples.value
    }
  })
  cluster.value = response.data.cluster
  bandwidth.value = response.data.bandwidth
  config.value.data = [Math.ceil(response.data.score * 100)]
  data.value = []
  names.value = []
  categorys.value = []
  title.value = []
  singleAxis.value = []
  series.value = []
  for (let i = 0; i < cluster.value; i++) {
    // @ts-ignore
    categorys.value.push(i)
  }
  // @ts-ignore
  response.data.data.forEach(info => {
    // @ts-ignore
    data.value.push([info['label'], info['姓名'], 1, info])
    // @ts-ignore
    names.value.push(info['姓名'])
  })
  categorys.value.forEach((category, idx) => {
    // @ts-ignore
    title.value.push({
      textBaseline: 'middle',
      top: ((idx + 0.5) * 100) / cluster.value + '%',
      text: category,
      textStyle: {
        color: "#44b7c6",
        fontSize: 18,
        fontWeight: 'bold', // 标题文本字体粗细
      },
      show:false
    })
    // @ts-ignore
    singleAxis.value.push({
      left: 150,
      type: 'category',
      boundaryGap: false,
      data: names.value,
      top: (idx * 100) / cluster.value + 5 + '%',
      height: 100 / cluster.value - 10 + '%',
      axisLabel: {
        show: false
      },
      axisLine: {
        lineStyle: {
          color: 'blue', // 坐标轴轴线的颜色
          width: 2, // 坐标轴轴线的宽度
          type: 'solid' // 坐标轴轴线的类型，'solid', 'dashed', 'dotted'
        }
      }
    })
    // @ts-ignore
    series.value.push({
      singleAxisIndex: idx,
      coordinateSystem: 'singleAxis',
      type: 'scatter',
      data: [],
      // @ts-ignore
      symbolSize: function (dataItem) {
        return dataItem[1] * 4;
      }
    })

  })
  data.value.forEach(function (dataItem) {
    // @ts-ignore
    series.value[dataItem[0]].data.push([dataItem[1], dataItem[2]]);
  });
  let option = {
    tooltip: {
      position: 'top',
      formatter: function (params: any) {
        let name = params.data[0]
        let res = data.value.filter((ele) => {
          return ele[1] === name
        })
        let info = res[0][3]
        return `label:${info['label']}<br/>姓名:${info['姓名']}<br/>学号:${info['学号']}<br/>性别:${info['性别']}<br/>班级:${info['班级']}<br/>
课堂表现记录:${info['课堂表现记录']}`
      }
    },
    title: title.value,
    singleAxis: singleAxis.value,
    series: series.value,

  }
  let myechart = proxy.$echarts.init(document.getElementById('cluster'))
  myechart.setOption(option)
  ElMessage({
    type:"success",
    message:"成功对学生进行聚类分析"
  })
}
onMounted(() => {
  init()
})
const handleChange = ()=>{
  init()
}
</script>

<template>
  <div style="display: flex;justify-content: center">
    <el-text type="success" style="margin-right: 10px">轮廓系数</el-text>
    <dv-water-level-pond :config="config" style="width:50px;height:50px"/>
    <el-text type="success" style="margin-left: 10px;margin-right: 10px">聚类方法</el-text>
    <el-select v-model="method" placeholder="请选择聚类方法" style="width: 200px;margin-top: 10px" filterable @change="handleChange">
      <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value">
      </el-option>
    </el-select>
    <div v-if="method === 'Kmeans' || method === 'Spectral clustering' || method === 'Spectral clustering' ||method === '层次聚类'">
      <el-text type="primary" style="margin-left: 10px;margin-right: 10px;">聚类数</el-text>
      <el-input size="small" style="width: 100px;height: 50px" v-model="cluster">
        <template #prefix>
          <el-icon><Odometer /></el-icon>
        </template>
      </el-input>
    </div>

    <div v-else-if="method === 'Mean Shift'">
        <div style="color: beige;margin-top: 15px;margin-left: 10px;margin-right: 10px">bandwidth:{{bandwidth.toFixed(2)}}</div>
    </div>

    <div v-else-if="method === 'DBSCAN' || method === 'OPTICS'">
      <el-text type="primary" style="margin-left: 10px;margin-right: 10px">min_samples</el-text>
      <el-input size="small" style="width: 100px;height: 50px" v-model="min_samples">
        <template #prefix>
          <el-icon><Odometer /></el-icon>
        </template>
      </el-input>
    </div>
    <dv-button @click="handleChange" border="Border3" color="#c8161d" font-color="#e18a3b" style="margin-left: 10px;height: 40px;text-align: center;line-height: 40px">重新聚类</dv-button>

  </div>
  <div style="width: 100%;height: 100%" id="cluster"></div>
</template>

<style>
.el-input__wrapper{
  height: 40px;
  background-color: cadetblue;
}
.el-input__inner{
  color: azure;
}
.el-select__input{
  color: azure;
}
.el-popper.is-customized {
  /* Set padding to ensure the height is 32px */
  padding: 6px 12px;
  background: linear-gradient(90deg, rgb(159, 229, 151), rgb(204, 229, 129));
}

.el-popper.is-customized .el-popper__arrow::before {
  background: linear-gradient(45deg, #b2e68d, #bce689);
  right: 0;
}
</style>