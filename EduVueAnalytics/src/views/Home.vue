<script setup lang="ts">

import Header from "../components/Header.vue";
import TeamReviewScoreChart from "../components/TeamReviewScoreChart.vue";

</script>

<template>
  <dv-full-screen-container>
    <!--  大标题  -->
    <Header></Header>
    <el-row>
      <el-col :span="8">
        <team-review-score-chart></team-review-score-chart>
      </el-col>
    </el-row>

  </dv-full-screen-container>
</template>

<style scoped>

</style>