<script setup lang="ts">

import Header from "../components/Header.vue";
// import SeleAssessment from "../components/SelfAssessment.vue";
// import GenderPieChart from "../components/GenderPieChart.vue";
import StudentTable from "../components/student-table.vue";

</script>

<template>
  <dv-full-screen-container>
    <!--  大标题  -->
    <Header></Header>
    <el-row>
      <el-col :span="8">
        <StudentTable></StudentTable>
<!--        <sele-assessment></sele-assessment>-->
      </el-col>
    </el-row>

<!--  <GenderPieChart></GenderPieChart>-->
  </dv-full-screen-container>
</template>

<style scoped>

</style>