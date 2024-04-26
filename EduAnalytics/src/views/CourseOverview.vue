<script setup lang="ts">
import Header from "@/components/Header.vue";
import RadarChart from "@/components/RadarChart.vue";
import WaterLevelChart from "@/components/WaterLevelChart.vue";
import ScoresLineGraph from "@/components/ScoresLineGraph.vue";
import {useRouter} from "vue-router";
import BubbleChart from "@/components/bubble-chart.vue";
import NodeChart from "@/components/node-chart.vue";
const router = useRouter()
const getCurrentDate = () => {
  const date = new Date(); // 创建一个Date对象，表示当前时间
  const year = date.getFullYear(); // 获取四位数的年份
  const month = (date.getMonth() + 1).toString().padStart(2, '0'); // 获取月份，加1是因为getMonth()返回的月份是从0开始的
  const day = date.getDate().toString().padStart(2, '0'); // 获取日期

  return `${year}年${month}月${day}日`; // 返回格式化的日期字符串
}
const configs = [
  {
    data: [25, 100],
    shape: 'roundRect'
  },
  {
    data: [30, 90],
    shape: 'roundRect'
  },
  {
    data: [25, 100],
    shape: 'roundRect'
  },
  {
    data: [25, 100],
    shape: 'roundRect'
  },
]
const handleClick = ()=>{
  router.push({name:'gradesList'})
}
</script>

<template>
  <Header :title="'课程情况'"></Header>
  <div class="course-over-view">
    <div class="left-item">
      <dv-border-box8 :dur="5" style="padding-left: 5px;padding-right: 5px">
      <div style="width: 100%;height: 400px;">
        <!--    标题        -->
        <div style="display: flex;justify-content: space-between;margin-bottom: 20px">
          <h2 style="color: #32C5FF;font-size: 30px;margin-left: 20px">素养评价</h2>
          <div style="color: greenyellow;font-size: 12px;margin-top: 10px">截止时间:{{ getCurrentDate() }}</div>
        </div>
        <!--    一排四个水位图        -->
        <div
            style="display: flex;color: white;justify-content: space-around;margin-bottom: 20px;font-weight: 700;font-size: 18px">
          <dv-decoration-11 style="width:150px;height:50px;">
            <div >知识与认知</div>
          </dv-decoration-11>
          <dv-decoration-11 style="width:150px;height:50px;">
            <div >道德与情感</div>
          </dv-decoration-11>
          <dv-decoration-11 style="width:150px;height:50px;">
            <div >实践与操作</div>
          </dv-decoration-11>
          <dv-decoration-11 style="width:150px;height:50px;">
            <div >创新与批判</div>
          </dv-decoration-11>
        </div>
        <div style="display: flex;justify-content: space-around">
          <dv-water-level-pond v-for="config in configs" :key="config" :config="config"
                               style="width:110px;height:190px"/>
        </div>
      </div>
        <div style="display: flex;width: 100%;justify-content: space-around">
          <water-level-chart documentId="water-level-chart1" title="人文素养" :water-level="10"></water-level-chart>
          <water-level-chart documentId="water-level-chart2" title="团队协作能力" :water-level="20"></water-level-chart>
          <water-level-chart documentId="water-level-chart3" title="实验素养" :water-level="15"></water-level-chart>
          <water-level-chart documentId="water-level-chart4" title="科学素养" :water-level="15"></water-level-chart>
          <water-level-chart documentId="water-level-chart5" title="信息化素养" :water-level="15"></water-level-chart>
          <water-level-chart documentId="water-level-chart6" title="创新素养" :water-level="20"></water-level-chart>
        </div>
      <div style="width: 100%;height: 280px;display: flex;">
        <div style="flex: 1 0;">
          <node-chart></node-chart>
        </div>
        <div style="flex: 1 0">
          <radar-chart></radar-chart>
        </div>

      </div>
      </dv-border-box8>
    </div>
    <div class="right-item">
      <dv-border-box8 :dur="5">
        <div style="width: 100%;height: 770px;display: flex;justify-content: center;align-items: center">
          <bubble-chart></bubble-chart>
        </div>
        <div style="text-align: center;display: flex;justify-content: flex-end;height: 40px">
          <dv-button @click="handleClick" border="Border6" color="#4bbbb2" style="width: 200px;font-size: 18px;margin-top: 5px;margin-right: 50px">点击前往结果分析</dv-button>
        </div>
      </dv-border-box8>
    </div>
  </div>
</template>

<style scoped lang="scss">
.course-over-view{
  display: flex;
  height: 100%;
  width: 100%;
  justify-content: space-between;
  .left-item{
    height: 100%;
    width: 100%;
  }
  .right-item{
    height: 100%;
    width: 100%;
  }
}
</style>