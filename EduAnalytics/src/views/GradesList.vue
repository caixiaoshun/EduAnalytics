<script setup lang="ts">

import Header from "@/components/Header.vue";
import {ref} from "vue";
import LineChart from "@/components/LineChart.vue";
import {useRouter} from "vue-router";

const suspend = 4
const whichShow = ref(0)
const router = useRouter()
const cur = ref(4)
setInterval(() => {
  whichShow.value = (whichShow.value + 1) % 5
  cur.value = suspend
}, suspend * 1000)
setInterval(() => {
  cur.value -= 1
}, 1000)
const handleClick = () => {
  router.push({name:'resultAnalysic'})
}
</script>

<template>
  <Header title="成绩展示"></Header>
  <div class="content">
    <dv-decoration7 style="width:240px;height:30px;margin-left: 720px;margin-top: 10px">
      <a-progress
          type="circle"
          :stroke-color="{
        '0%': '#108ee9',
        '100%': '#87d068',
      }"
          :percent="(1 - cur / suspend) * 100"
      />
    </dv-decoration7>
    <div class="chart-item" style="top: 450px;" v-if="whichShow === 0">
      <dv-border-box8 :dur="5">
        <line-chart title="自评成绩" name="" document-id="chart-item1" url="/getselfassess"/>
      </dv-border-box8>
    </div>
    <div class="chart-item" style="top: 250px;left: 200px" v-if="whichShow === 1">
      <dv-border-box8 :dur="5">
        <line-chart title="小组成绩" name="" document-id="chart-item2" url="/getgroupegrade"/>
      </dv-border-box8>
    </div>
    <div class="chart-item" style="top: 160px;left: 400px" v-if="whichShow === 2">
      <dv-border-box8 :dur="5">
        <line-chart title="作业成绩" name="" document-id="chart-item3" url="/gethomeworkgrade"/>
      </dv-border-box8>
    </div>
    <div class="chart-item" style="top: 180px;left: 800px" v-if="whichShow === 3">
      <dv-border-box8 :dur="5">
        <line-chart title="期中成绩" name="" document-id="chart-item4" url="/getmidgrade"/>
      </dv-border-box8>
    </div>
    <div class="chart-item" style="top: 350px;left: 600px" v-if="whichShow === 4">
      <dv-border-box8 :dur="5">
        <line-chart title="期末成绩" name="" document-id="chart-item5" url="/getendgrade"/>
      </dv-border-box8>
    </div>
    <div style="position: absolute;top: 50px;right: 50px">
      <dv-button @click="handleClick" border="Border6" color="#4bbbb2"
                 style="width: 200px;font-size: 18px;margin-top: 5px;margin-right: 50px">点击前往结果分析
      </dv-button>
    </div>
  </div>
</template>

<style scoped lang="scss">
.content {
  width: 100%;
  height: 100%;
  padding: 20px;

  .chart-item {
    width: 800px;
    height: 400px;
    display: inline-block;
    position: absolute;
  }
}

</style>