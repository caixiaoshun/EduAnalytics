<script setup lang="ts">
import {useRouter} from "vue-router";
const router = useRouter()
import Header from "@/components/Header.vue";
import welcomeImg from '@/assets/welcome.png'

const handleClick = ()=>{
  router.push({name:'courseOverView'})
}
</script>

<template>
  <Header></Header>
  <div class="welcome">
    <img :src="welcomeImg" alt="" style="height: 750px"/>
    <div>
      <div class="title">
        ClassTrack and TeachVis
      </div>
      <div style="margin-top: 100px;text-align: center">

        <div class="start-title" :onclick="handleClick">
          <dv-border-box10>
            进入系统
          </dv-border-box10>
        </div>

      </div>
    </div>
  </div>
  <div style="margin-top: 90px;font-family: sans-serif;text-align: center">
    <span style="color: #808080"><a href="http://beian.miit.gov.cn/" target="_blank">豫ICP备2024065810号-1</a></span>
  </div>
</template>

<style scoped lang="scss">
@font-face {
  font-family: 'HuXiaoBoNanShenTi'; /* 定义一个自定义的字体名称 */
  src: url('../assets/ttfs/HuXiaoBoNanShenTi-2.otf') format('opentype'); /* 指定字体文件的路径和格式 */
}

.welcome {
  display: flex;
  align-items: center;
}

.title {
  /** 文本1 */
  font-family: 'HuXiaoBoNanShenTi', sans-serif;
  font-size: 72px;
  font-weight: 400;
  letter-spacing: 0;
  line-height: 75.38px;
  color: rgba(255, 255, 255, 1);
  text-align: center;
  vertical-align: top;

}

.start-title {
  height: 150px;
  font-size: 60px;
  font-weight: 400;
  letter-spacing: 0;
  line-height: 120px;
  color: rgba(255, 255, 255, 1);
  vertical-align: top;
  display: inline-block;
  cursor: pointer;
  font-family: 'HuXiaoBoNanShenTi', sans-serif;
}
</style>