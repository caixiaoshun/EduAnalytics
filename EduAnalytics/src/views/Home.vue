<script setup lang="ts">

import Header from "@/components/Header.vue";
import ScoresLineGraph from "@/components/ScoresLineGraph.vue";
</script>

<template>
<div class="container">
  <Header></Header>
  <div class="content">
  <div class="left-item">
    <div class="line-graph">
      <scores-line-graph></scores-line-graph>
    </div>
  </div>
  <div class="middle-item"></div>
  <div class="right-item"></div>
  </div>
</div>
</template>

<style scoped lang="scss">
.content{
  height: 986px;
  width: 100%;
  display: flex;
  .left-item{
    width: 450px;
    padding-left: 25px;
    padding-right: 25px;
    .line-graph{
      height: 488px;
      width: 100%;
    }
  }
  .middle-item{
    width: 1020px;

  }
  .right-item{
    width: 450px;

  }
}
</style>