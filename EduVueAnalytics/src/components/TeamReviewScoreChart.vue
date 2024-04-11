<script setup lang="ts">
import {onMounted, reactive, ref} from "vue";
import request from "../request";

const urls = {
  "组长第一次打分":"/getFirstLeaderScore",
  "组长第二次打分":"/getSecondLeaderScore",
  "组员第一次打分":"/getFirstMemberScore",
  "组员第二次打分":"/getSecondMemberScore",

}
const value = ref('组长第一次打分')
const options = [
  {
    value: '组长第一次打分',
    label: '组长第一次打分',
  },
  {
    value: '组长第二次打分',
    label: '组长第二次打分',
  },
  {
    value: '组员第一次打分',
    label: '组员第一次打分',
  },
  {
    value: '组员第二次打分',
    label: '组员第二次打分',
  },
]
const config = reactive({
  data:[],
  unit:'分'
})
const ChangeScore = async ()=>{
  // @ts-ignore
  let response = await request.get(urls[value.value])
  config.data = response.data.data
}
const handleChange = ()=>{
  ChangeScore()
}
onMounted(()=>{
  ChangeScore()
})
</script>

<template>
<div style="height: 100%;width: 100%">
  <h2 style="color: azure;text-align: center;height: 20px">{{value}}</h2>
  <dv-scroll-ranking-board :config="config" style="width:500px;height:300px;" />
  <div style="text-align: center">

    <el-select
        v-model="value"
        filterable
        placeholder="选择想要查看的成绩"
        tag-type="success"
        placement="bottom-end"
        style="width: 150px;"
        @change="handleChange"
    >
      <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value"
          style="text-align: center"
      />
    </el-select>
  </div>



</div>
</template>

<style>
.el-select__wrapper{
  background-color: #0A2732;
  color: azure;
  text-align: center;
}
.el-select__selected-item span{
  color: azure;
}
</style>