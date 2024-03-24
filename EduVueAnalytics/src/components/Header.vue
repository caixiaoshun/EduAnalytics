<script setup lang="ts">

</script>

<template>
<div class="header">
  <div class="header-item">
    <dv-decoration-10 style="height:50px;" />
  </div>
  <div class="header-title">
    <div style="display: flex;align-items: center">
      <dv-decoration-8 style="height: 50px;flex: 1" />
      <div style="flex: 1;color: ghostwhite;text-align: center;font-weight: 600;font-size: 17px">数据分析与处理技术课堂分析</div>
      <dv-decoration-8 style="height: 50px;flex: 1" :reverse="true" />
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