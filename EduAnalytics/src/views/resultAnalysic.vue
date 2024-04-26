<script setup lang="ts">

import Header from "@/components/Header.vue";
import GradeDescription from "@/components/gradeDescription.vue";
import WordCloudChart from "@/components/word-cloud-chart.vue";
import StudentCluster from "@/components/studentCluster.vue";
import {message} from "ant-design-vue";
import {storeToRefs} from "pinia";
import {useClusterStore} from "@/stores/clusterStore";
import {ref} from "vue";
import {useRouter} from "vue-router";
const {cluster, score, method,spinning} = storeToRefs(useClusterStore())
const router = useRouter()
const childDom = ref(null)
const options = [
  {
    value: "Kmeans",
    label: "Kmeans"
  },
  {
    value: "Spectral clustering",
    label: "Spectral clustering"
  },
  {
    value: "层次聚类",
    label: "层次聚类"
  },

]
const clusterStart = async () => {
  // @ts-ignore
  await childDom.value.init()
  message.success('聚类成功');
}
const handleClick = () => {
  router.push({name:'home'})
}
</script>

<template>
  <Header title="结果分析与展示"></Header>
  <div class="layout">
    <div class="left-content">
      <dv-border-box8 :dur="5" style="padding: 50px">
          <div style="width: 100%;height: 400px"><grade-description></grade-description></div>
          <div style="width: 100%;height: 400px"> <word-cloud-chart></word-cloud-chart></div>

      </dv-border-box8>
    </div>
    <div class="right-content">
      <dv-border-box8 :dur="5" :reverse="true" style="padding: 50px">
        <div class="student-cluster">
          <div style="display: flex;justify-content: center;margin-bottom: 10px">
            <div style="display: flex;">
              <span style="color: #32C5FF;font-size: 18px;height: 24px;line-height: 24px;margin-right: 10px">聚类方法</span>
              <a-select
                  v-model:value="method"
                  show-search
                  placeholder="Select a person"
                  style="width: 200px"
                  :options="options"
                  size="small"
              ></a-select>
            </div>
            <div style="display: flex;margin-left: 30px">
              <span style="color: #32C5FF;font-size: 18px;height: 24px;line-height: 24px;margin-right: 10px">聚类数量</span>
              <a-input v-model:value.number="cluster" size="small" style="width: 100px"></a-input>
            </div>


          </div>
          <div style="display: flex;justify-content: center;margin-bottom: 10px;margin-top: 40px">
            <dv-button @click="clusterStart" border="Border6" color="#34cc80">进行聚类分析</dv-button>
          </div>
          <div
              style="height: 10px;width: 100%;display: flex;justify-content: space-around;margin-bottom: 10px;color: #32C5FF">
            <div>聚类数量</div>
            <div>轮廓系数</div>
          </div>
          <div style="height: 100px;width: 100%;display: flex;justify-content: space-around;margin-bottom: 10px">
            <dv-decoration-9 style="width:90px;height:90px;">
              <div class="decoration-9-content">
                {{ cluster }}
              </div>
            </dv-decoration-9>

            <dv-decoration-9 style="width:90px;height:90px;">
              <div class="decoration-9-content">
                {{ score.toFixed(2) }}
              </div>
            </dv-decoration-9>
          </div>
<!--          <div style="display: flex;justify-content: flex-end">-->
<!--            <dv-button @click="handleClick" border="Border3" color="#c8161d" font-color="#e18a3b">总览</dv-button>-->
<!--          </div>-->
          <a-spin style="height: 500px;width: 100%" :spinning="spinning">
          <student-cluster style="height: 500px" ref="childDom"></student-cluster>
          </a-spin>
        </div>
      </dv-border-box8>
    </div>

  </div>
</template>

<style scoped lang="scss">
.layout {
  display: flex;
  width: 100%;
  height: 100%;

  .left-content {
    width: 100%;
    height: 100%;
    flex: 1 0;
  }

  .right-content {
    width: 100%;
    height: 100%;
    flex: 2 0;
  }
}
.decoration-9-content {
  font-size: 28px;
  text-shadow: 0 0 3px #7acaec;
  color: #32C5FF;
  background-color: #06324F;
}
</style>