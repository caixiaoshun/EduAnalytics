<script setup lang="ts">

import Header from "@/components/Header.vue";
import ScoresLineGraph from "@/components/ScoresLineGraph.vue";
import GradeDescription from "@/components/gradeDescription.vue";
import StudentCluster from "@/components/studentCluster.vue";
import {useClusterStore} from "@/stores/clusterStore";
import {storeToRefs} from "pinia";
import {ref} from "vue";
import {message} from "ant-design-vue";
import WaterLevelChart from "@/components/WaterLevelChart.vue";

const {cluster, score, method} = storeToRefs(useClusterStore())
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
const childDom = ref(null)
const clusterStart = async () => {
  // @ts-ignore
  await childDom.value.init()
  message.success('聚类成功');
}
</script>

<template>
  <div class="container">
    <Header></Header>
    <div class="content">
      <div class="left-item">
        <dv-border-box12 class="left-item-border">
          <div class="line-graph">
            <scores-line-graph></scores-line-graph>
          </div>
        </dv-border-box12>
      </div>
      <div class="middle-item">
        <!--  三列-->
        <div>
          <div class="water-level-chart-item">
            <water-level-chart documentId="water-level-chart1" title="人文素养"></water-level-chart>
          </div>
          <div class="water-level-chart-item">
            <water-level-chart documentId="water-level-chart2" title="团队协作能力"></water-level-chart>
          </div>
          <div class="water-level-chart-item">
            <water-level-chart documentId="water-level-chart3" title="实验素养"></water-level-chart>
          </div>

        </div>
        <div style="height: 420px;width: 500px">
          <a-image :width="500" :height="420" src="https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png">

          </a-image>
        </div>

        <div>
          <div class="water-level-chart-item">
            <water-level-chart documentId="water-level-chart4" title="科学素养"></water-level-chart>
          </div>
          <div class="water-level-chart-item">
            <water-level-chart documentId="water-level-chart5" title="信息化素养"></water-level-chart>
          </div>
          <div class="water-level-chart-item">
            <water-level-chart documentId="water-level-chart6" title="创新素养"></water-level-chart>
          </div>

        </div>
      </div>
      <div class="right-item">
        <dv-border-box8>
          <div class="grade-description">
            <grade-description></grade-description>
          </div>
          <div class="student-cluster">
            <div style="display: flex;justify-content: space-around;margin-bottom: 10px">
              <span style="color: #32C5FF;font-size: 12px;height: 24px;line-height: 24px">聚类方法</span>
              <a-select
                  v-model:value="method"
                  show-search
                  placeholder="Select a person"
                  style="width: 200px"
                  :options="options"
                  size="small"
              ></a-select>
              <span style="color: #32C5FF;font-size: 12px;height: 24px;line-height: 24px">聚类数量</span>
              <a-input v-model:value.number="cluster" size="small" style="width: 100px"></a-input>

            </div>
            <div style="display: flex;justify-content: center;margin-bottom: 10px">
              <dv-button @click="clusterStart" border="Border6" color="#615ea8">进行聚类分析</dv-button>
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
            <student-cluster ref="childDom"></student-cluster>
          </div>
        </dv-border-box8>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.content {
  height: 1200px;
  width: 100%;
  display: flex;

  .left-item {
    width: 450px;

    .left-item-border {
      padding-left: 25px;
      padding-right: 25px;
    }

    .line-graph {
      height: 488px;
      width: 100%;
    }
  }

  .middle-item {
    width: 1020px;
    display: flex;
    padding-top: 10px;
    justify-content: space-around;
    .water-level-chart-item{
      width: 140px;
      height: 140px;
    }

  }

  .right-item {
    width: 450px;

    .grade-description {
      height: 444px;
      width: 100%;
    }

    .student-cluster {
      height: 542px;
      width: 100%;
    }
  }
}

.decoration-9-content {
  font-size: 28px;
  text-shadow: 0 0 3px #7acaec;
  color: #32C5FF;
  background-color: #06324F;
}
</style>