<template>
  <div style="width:100%;height:100%">
    <el-row>
      <dv-button @click="handleClick()" border="Border2" color="#4c8045"
                 style="margin-bottom: 5px;margin-left: 250px;text-align: center;margin-top: 10px">{{ buttonText }}
      </dv-button>
    </el-row>
    <dv-scroll-board :config="student_table" style="width:90%;height:90%;margin: auto" v-if="buttonText === '班级统计'"
                     :hoverPause="false" :waitTime="1000"/>
    <div v-if="buttonText === '班级明细'" class="class-detail" style="margin-left: 70px">
      <el-row style="margin-top: 50px">
          <el-card style="background-color: #0A2732;border: #0A2732 solid 1px;color: wheat">
            <template #header>
              <div class="card-header" style="text-align: center">
                <span>班级人数分布</span>
              </div>
            </template>
            <el-row>
              <el-col v-for="ele in class_name" :key="ele" :span="24 / class_name.length">
                <el-statistic :value="null">
                  <template #title>
                    <div style="color: ghostwhite">
                      {{ ele }}
                    </div>
                  </template>
                  <template #suffix>
                    <el-tag type="primary" style="margin-left: 10px;margin-bottom: 10px">
                      <NumberAnimation :to="studentInformation['class_name'][ele]" :duration="5000"></NumberAnimation>人
                    </el-tag>
                  </template>
                </el-statistic>
              </el-col>
            </el-row>

            <el-row>
              <el-col :span="12" style="display: flex; justify-content: center; align-items: center; height: 100%;">
                <el-statistic :value="null">
                  <template #title>
                    <div style="display: inline-flex; align-items: center;color: ghostwhite">
                      <el-tooltip
                          effect="dark"
                          content="班级男生人数"
                          placement="top"
                      >
                        <img src="../assets/male.png">
                      </el-tooltip>
                    </div>
                  </template>
                  <template #suffix>
                    <div style="color: ghostwhite;font-size: 18px;font-weight: 600;text-align: center">
                      <el-tag type="success" style="margin-bottom: 10px" size="large">
                        <el-text type="primary">男生</el-text><NumberAnimation :to="male" :duration="5000"></NumberAnimation>人
                      </el-tag>
                    </div>
                  </template>
                </el-statistic>
              </el-col>
              <el-col :span="12" style="display: flex; justify-content: center; align-items: center; height: 100%;">
                <el-statistic :value="null">
                  <template #title>
                    <div style="display: inline-flex; align-items: center;color: ghostwhite">
                      <el-tooltip
                          effect="dark"
                          content="班级女生人数"
                          placement="top"
                      >
<!--                        <el-icon style="margin-left: 4px" :size="12">-->
<!--                          <UserFilled />-->
<!--                        </el-icon>-->
                        <img src="../assets/female.png">
                      </el-tooltip>
                    </div>
                  </template>
                  <template #suffix>
                    <div style="color: ghostwhite;font-size: 18px;font-weight: 600;text-align: center">
                      <el-tag type="success" style="margin-bottom: 10px" size="large">
                        <el-text type="primary">女生</el-text><NumberAnimation :to="female" :duration="5000"></NumberAnimation>人
                      </el-tag>
                    </div>
                  </template>
                </el-statistic>
              </el-col>
            </el-row>

            <template #footer style="text-align: center">总人数:<NumberAnimation :to="total" :duration="5000"></NumberAnimation></template>
          </el-card>

      </el-row>
    </div>
  </div>


</template>
<script lang="ts" setup>
import {onMounted, ref} from "vue";
import request from "../request";

const studentInformation = ref()
const class_name: any = ref([])
const buttonText = ref("班级明细")
const total = ref(0)
const male = ref(0)
const female = ref(0)
const student_table: any = ref({
  header: [], data: [], index: true, columnWidth: [60, 150, 80, 60, 200],
  align: ['center']
})
const init = async ()=>{
  let response = await request.get('/getAllStudents')
  student_table.value.header = ['学号', '姓名', '性别', '班级']
  for (let key in response.data) {
    student_table.value.data.push([response.data[key]['student_id'], response.data[key]['name'], response.data[key]['gender'], response.data[key]['class_name']])
  }
  response = await request.get('/getStudentInformation')
  studentInformation.value = response.data
  class_name.value = Object.keys(studentInformation.value['class_name'])
  total.value = studentInformation.value.total
  male.value = studentInformation.value['gender']['男']
  female.value = studentInformation.value['gender']['女']
}

onMounted(()=>{
  init()
})
const handleClick = () => {
  if (buttonText.value === '班级明细') {
    buttonText.value = '班级统计'
  } else {
    buttonText.value = '班级明细'
  }
}
</script>

<style scoped>
.class-detail {
  width: 100%;
  height: 100%;
  color: ghostwhite;
  margin-left: 20px;
}
</style>
