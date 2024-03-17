<script setup lang="ts">

import Header from "../components/Header.vue";
import GenderPieChart from "../components/GenderPieChart.vue";
// import StudentTable from "../components/student-table.vue";
</script>

<template>
  <dv-full-screen-container>
    <!--  大标题  -->
    <Header></Header>
<!--    <StudentTable></StudentTable>-->
  <GenderPieChart></GenderPieChart>
  </dv-full-screen-container>
</template>

<style scoped>

</style>