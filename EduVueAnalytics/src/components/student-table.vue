<template>
  <dv-scroll-board :config="student_table" style="width:500px;height:300px"/>
</template>
<script lang="ts" setup>
import {onMounted, ref} from "vue";
import request from "../request";

const student_table: any = ref({
  header: [], data: [], index: true, columnWidth: [60, 150, 80, 40, 200],
  align: ['center']
})
onMounted(async () => {
  const response = await request.get('/student/getAllStudents')
  student_table.value.header = ['学号', '姓名', '性别', '班级']
  for (let key in response.data) {
    student_table.value.data.push([response.data[key]['student_id'], response.data[key]['name'], response.data[key]['gender'], response.data[key]['class_name']])
  }
})

</script>