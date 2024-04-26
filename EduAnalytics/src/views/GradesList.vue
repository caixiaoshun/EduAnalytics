<script setup lang="ts">

import Header from "@/components/Header.vue";
import {onMounted, ref} from "vue";
import {useRouter} from "vue-router";
import RingChart from "@/components/ring-chart.vue";
import ConicalBarChart from "@/components/conicalBarChart.vue";
import {request} from "@/request";
import {useClusterStore} from "@/stores/clusterStore";
import {storeToRefs} from "pinia";
import ScoresLineGraph from "@/components/ScoresLineGraph.vue";
import NodeChart from "@/components/node-chart.vue";
import StudentPerformance3D from "@/components/StudentPerformance3D.vue";

const {spinning} = storeToRefs(useClusterStore())
const studentName = ref('宋显浩')
const options = ref()
const ConicalBarChartChild = ref(null)
const router = useRouter()
onMounted(async () => {
  let response = await request.get('/getStudentNames')
  let data = response.data.data
  options.value = []
  for (let i = 0; i < data.length; i++) {
    options.value.push({
      value: data[i],
      label: data[i]
    })
  }
})
const handleChange = async () => {
  //@ts-ignore
  await ConicalBarChartChild.value.init()
}
const handleClick = () => {
  router.push({name: 'resultAnalysic'})
}
</script>

<template>
  <Header title="成绩展示"></Header>
  <div class="content">
    <dv-border-box8 :dur="5" style="padding: 20px;">
      <div style="width: 100%;height: 100%;display: flex">
        <!--   左边     -->
        <div style="flex: 1 0;display: flex;flex-direction: column">
          <div style="flex: 1 0">
            <ring-chart></ring-chart>
          </div>
          <div style="flex: 1 0">
            <div style="display: flex;justify-content: flex-end;width: 100%;height: 20%">
              <a-select
                  v-model:value="studentName"
                  show-search
                  placeholder="请选择学生"
                  style="width: 200px"
                  :options="options"
                  @change="handleChange"
              >
              </a-select>
            </div>
            <div style="width: 100%;height: 80%">
              <a-spin :spinning="spinning">
                <conical-bar-chart :name="studentName" ref="ConicalBarChartChild"></conical-bar-chart>
              </a-spin>
            </div>

          </div>
        </div>

        <!--   右边     -->
        <div style="flex: 2 0;display: flex;flex-direction: column;justify-content: space-between">
          <div style="flex: 1 0;text-align: center">
            <!--            <node-chart></node-chart>-->
            <student-performance3-d></student-performance3-d>
          </div>
          <div style="flex: 2 0;">
            <div style="width: 100%;height: 90%">
              <scores-line-graph></scores-line-graph>
            </div>
            <div style="width: 100%;height: 10%;display: flex;justify-content: flex-end;align-items: center">
              <dv-button @click="handleClick" border="Border4" color="#a6559d">结果分析</dv-button>
            </div>
          </div>
        </div>
      </div>

    </dv-border-box8>
  </div>
</template>

<style scoped lang="scss">
.content {
  width: 100%;
  height: 100%;
  font-family: 'YouSheTitleHei',serif;

}

</style>