<template>
  <h2 style="color: ghostwhite;margin-bottom: 10px;margin-left: 10px;text-align: center">班级人员</h2>
  <dv-scroll-board :config="student_table" style="width:500px;height:300px"/>
  <el-descriptions
      title="表格明细"
      :column="3"
  >
    <el-descriptions-item label="Remarks">
      <el-tag size="small">School</el-tag>
    </el-descriptions-item>
    <el-descriptions-item label="Address"
    >No.1188, Wuzhong Avenue, Wuzhong District, Suzhou, Jiangsu Province
    </el-descriptions-item>
  </el-descriptions>
</template>
<script lang="ts" setup>
import {onMounted, ref} from "vue";
import request from "../request";

const student_table: any = ref({
  header: [], data: [], index: true, columnWidth: [60, 150, 80, 60, 200],
  align: ['center']
})
onMounted(async () => {
  let response = await request.get('/student/getAllStudents')
  student_table.value.header = ['学号', '姓名', '性别', '班级']
  for (let key in response.data) {
    student_table.value.data.push([response.data[key]['student_id'], response.data[key]['name'], response.data[key]['gender'], response.data[key]['class_name']])
  }
})

</script>
