<script setup lang="ts">
import backgroundAudio from '@/assets/audio/2.mp3'
import {h, onMounted, ref} from "vue";
import {Modal} from "ant-design-vue";

const audioAutoPlay = () => {
  let audio = document.getElementById("audio");

  // @ts-ignore
  audio.play();

}
onMounted(()=>{
  let oAudio = document.querySelector("#audio");
  // @ts-ignore
  oAudio.onended = function() {
    //播放完毕，重新循环播放
    // @ts-ignore
    oAudio.load();
    // @ts-ignore
    oAudio.play();
  };
})
Modal.info({
  title: '提示',
  content: h('div', {
    class: 'custom-modal-content',
  }, [
    '请注意，本界面含有背景音乐'
  ]),
  onOk() {
    audioAutoPlay()
  },
});
</script>

<template>
  <audio id="audio" :src="backgroundAudio"></audio>
  <RouterView/>
</template>

<style scoped>

</style>
