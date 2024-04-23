<script setup lang="ts">
import {useClusterStore} from "@/stores/clusterStore";
import {storeToRefs} from "pinia";
const {spinning} = storeToRefs(useClusterStore())
// 粒子参数

</script>

<template>

  <a-spin size="large" tip="加载中" :spinning="spinning">
  <RouterView />
  </a-spin>
</template>

<style scoped>

</style>
