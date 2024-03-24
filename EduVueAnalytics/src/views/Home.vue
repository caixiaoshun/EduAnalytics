<script setup lang="ts">

import Header from "../components/Header.vue";
import StudentPerformance3D from "../components/StudentPerformance3D.vue";
import StudentTable from "../components/student-table.vue";
import SelfAssessment from "../components/SelfAssessment.vue";
import GenderPieChart from "../components/GenderPieChart.vue";
import TeamReviewScoreChart from "../components/TeamReviewScoreChart.vue";

</script>

<template>
  <dv-full-screen-container>
    <!--  大标题  -->
    <Header></Header>

    <!--  第一行  -->
    <div class="module-box" style="height: 50vh;width: 100%">
      <div style="flex: 0 1 30%">
        <dv-border-box1>
          <StudentPerformance3D></StudentPerformance3D>
        </dv-border-box1>
      </div>
      <div style="flex: 0 1 40%;">
        <dv-border-box8 :dur="5">
          <student-table></student-table>
        </dv-border-box8>
      </div>
      <div style="flex: 0 1 30%">
        <dv-border-box9>
          <self-assessment></self-assessment>
        </dv-border-box9>
      </div>
    </div>

    <!--  第二行  -->
    <div class="module-box" style="height: 40vh;width: 100%;margin-top: 30px;margin-right: 10px;">
      <div>
        <dv-border-box10 style="width: 100%;height: 100%">
          <gender-pie-chart></gender-pie-chart>
        </dv-border-box10>

      </div>

      <div>
        <dv-border-box8 :reverse="true">
          <team-review-score-chart></team-review-score-chart>
        </dv-border-box8>
      </div>
      <div style="flex: 0 1 40%">

      </div>

    </div>

  </dv-full-screen-container>
</template>

<style scoped>
.module-box {
  display: flex;
  justify-content: space-between;
  margin: 5px;
}
</style>