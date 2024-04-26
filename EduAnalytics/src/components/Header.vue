<script setup lang="ts">
const props = defineProps({
  title:{
    type:String,
    default:"ClassTrack and TeachVis"
  }
})
</script>

<template>
<div class="header">
  <div class="header-item">
    <dv-decoration-10 style="height:44px;" />
  </div>
  <div class="header-title">
    <div style="display: flex;align-items: center">
      <dv-decoration-8 style="height: 44px;flex: 1" />
      <div style="flex: 1;color: ghostwhite;text-align: center;font-weight: 400;font-size: 17px" class="animate__backInLeft">{{props.title}}</div>
      <dv-decoration-8 style="height: 44px;flex: 1" :reverse="true" />
    </div>

  </div>
  <div class="header-item">
    <dv-decoration-10 style="height:50px;transform: rotate(180deg)" />
  </div>
</div>
</template>

<style scoped>
.header{
  display: flex;
}
.header-item{
  flex: 3;
}
.header-title{
  flex: 4;
}
</style>