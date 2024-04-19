<script setup lang="ts">

import Header from "@/components/Header.vue";
import ScoresLineGraph from "@/components/ScoresLineGraph.vue";
import GradeDescription from "@/components/gradeDescription.vue";
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
        <dv-border-box10>

        </dv-border-box10>
      </div>
      <div class="right-item">
        <dv-border-box8>
          <div class="grade-description">
            <grade-description></grade-description>
          </div>
        </dv-border-box8>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.content {
  height: 986px;
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

  }

  .right-item {
    width: 450px;

    .grade-description {
      height: 704px;
      width: 100%;
    }
  }
}
</style>