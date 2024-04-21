<script setup lang="ts">
import {onMounted, reactive, ref} from "vue";
import {useStudentPerformance} from "@/stores/studentPerformance";
import {storeToRefs} from "pinia";
import {request} from "@/request";

const {showWhichChart} = storeToRefs(useStudentPerformance())
const props = defineProps({
  studentName: {
    type:String,
    default:'刘婧'
  },
  classTh:{
    type:String,
    default:'第一课'
  },
  title:{
    type:String,
    default:"刘婧"
  }
})
const spinning = ref(true)
const config = reactive({
  data: [
    {
      name: '周口',
      value: 55,
    },
  ],
  unit: '万元',
})
onMounted(async () => {
  let response = await request.get("/getClassByNameOrClassTh",{
    params:{
      'showWhichChart':showWhichChart.value,
      'student_name':props.studentName,
      'class_th':props.classTh
    }
  })
  let data = response.data.data
  config.data = []
  config.unit = '分'
  if (showWhichChart.value === 1) {
    for(let i = 4;i<data[0].length;i++){
      config.data.push({
        name:`第${i-3}课`,
        value: data[0][i]
      })
    }
  } else {
    for (let i = 0; i < data.length; i++) {
      config.data.push({
        name:data[i][0],
        value: data[i][1]
      })
    }
  }
  spinning.value = false
})


</script>

<template>
  <a-spin :spinning="spinning">
    <div style="height: 15px;margin-bottom: 5px;text-align: center;color: #32C5FF">{{props.title}}</div>
    <dv-scroll-ranking-board style="height: 380px;width: 550px;" :config="config" />
  </a-spin>

</template>

<style scoped lang="scss">

</style>