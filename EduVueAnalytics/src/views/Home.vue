<script setup lang="ts">

import Header from "../components/Header.vue";
import StudentPerformance3D from "../components/StudentPerformance3D.vue";


</script>

<template>
  <dv-full-screen-container>
    <!--  大标题  -->
    <Header></Header>
    <el-row>
      <el-col :span="8">
        <student-performance3-d></student-performance3-d>
      </el-col>
    </el-row>

  </dv-full-screen-container>
</template>

<style scoped>

</style>