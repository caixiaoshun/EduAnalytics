<script setup lang="ts">

import Header from "../components/Header.vue";
// import HeatmapOfStudentPerformance from "../components/StudentPerformance3D.vue";
// import SeleAssessment from "../components/SelfAssessment.vue";
import GenderPieChart from "../components/GenderPieChart.vue";
// import StudentTable from "../components/student-table.vue";

</script>

<template>
  <dv-full-screen-container>
    <!--  大标题  -->
    <Header></Header>
    <el-row>
      <el-col :span="8">
<!--        <StudentTable></StudentTable>-->
<!--        <sele-assessment></sele-assessment>-->
<!--        <heatmap-of-student-performance></heatmap-of-student-performance>-->
        <gender-pie-chart></gender-pie-chart>
      </el-col>
    </el-row>

  </dv-full-screen-container>
</template>

<style scoped>

</style>