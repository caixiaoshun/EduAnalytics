<script setup lang="ts">
import {notification} from "ant-design-vue";
import img1 from '@/assets/冠军.png'
import img2 from '@/assets/钻石.png'
import img3 from '@/assets/白金.png'
import img4 from '@/assets/铂金.png'
import img5 from '@/assets/银章.png'

interface Value {
  name: string,
  value: number
}

import {computed, h, onMounted, reactive, type Ref, ref} from "vue";
import {request} from "@/request";
import {SmileOutlined} from "@ant-design/icons-vue";

const excellenceRate = ref(0)
const passRate = ref(0)
const cur = ref(0)
const pageSize = 5
const totalPages = ref(0)
const allData: Ref<Array<Value>> = ref([])
const getCurrentTime = computed(() => {
  const now = new Date(); // 获取当前时间
  const year = now.getFullYear(); // 获取年份
  const month = now.getMonth() + 1; // 获取月份，月份是从0开始计数的
  const day = now.getDate(); // 获取日期

  // 格式化月份、日期、小时和分钟，确保它们都是两位数
  const monthStr = month < 10 ? '0' + month : month.toString();
  const dayStr = day < 10 ? '0' + day : day.toString();

  // 组合成所需的时间格式
  return `${year}年${monthStr}月${dayStr}日`;
})
const config = ref({
  data: [
    {
      name: '周口',
      value: 55,
    },
  ],
  showValue: true,
  img: [
    img1,
    img2,
    img3,
    img4,
    img5,
  ]
})
onMounted(async () => {
  let response = await request.get("getStudentGrade")
  let data = response.data.data
  // @ts-ignore
  let passCount = data.filter(score => score['总成绩'] >= 60).length
  // @ts-ignore
  let excellentCount = data.filter(score => score['总成绩'] >= 90).length
  let totalCount = data.length
  excellenceRate.value = (excellentCount / totalCount) * 100
  passRate.value = (passCount / totalCount) * 100
  allData.value = []
  for (let i = 0; i < data.length; i++) {
    allData.value.push({
      name: data[i]['姓名'],
      value: data[i]['总成绩']
    })
  }
  allData.value.sort(function (a, b) {
    return b.value - a.value; // 降序排序
  });
  config.value.data = allData.value.slice(cur.value * pageSize, cur.value * pageSize + pageSize)
  totalPages.value = Math.ceil(allData.value.length / pageSize)
})
const prevPage = () => {
  if (cur.value > 1) cur.value = cur.value - 1
  else {
    notification.open({
      message: '提示',
      description:
          '这已经是第一页了',
      placement: 'topLeft',
      icon: () => h(SmileOutlined, {style: 'color: #108ee9'}),
    });
  }
  config.value.data = allData.value.slice(cur.value * pageSize, cur.value * pageSize + pageSize)
}
const nextPage = () => {
  if (cur.value < totalPages.value) cur.value = cur.value + 1
  else {
    notification.open({
      message: '提示',
      description:
          '这已经是最后一页了',
      placement: 'topLeft',
      icon: () => h(SmileOutlined, {style: 'color: #108ee9'}),
    });
  }
  config.value.data = allData.value.slice(cur.value * pageSize, cur.value * pageSize + pageSize)
}
</script>

<template>
  <div class="container">
    <div class="title"><span>学生成绩总结</span></div>
    <div class="description">
      <div style="font-weight: 600;font-size: 14px;font-family: 'YouSheTitleHei', sans-serif">总分排名</div>
      <div style="font-size: 8px;color:rgb(236,223,223)">截止时间:{{ getCurrentTime }}</div>
    </div>
    <div style="margin-top: 5px;">
      <a-row :gutter="16">
        <a-col :span="12">
          <a-card style="background-color: #0A537D">
            <a-statistic
                :value="excellenceRate"
                :precision="2"
                suffix="%"
                :value-style="{ color: '#66FFFF' }"
            >
              <template #title>
                <span style="color: #cc6464;font-family: 'YouSheTitleHei', sans-serif">学生优秀率</span>
              </template>
            </a-statistic>
          </a-card>
        </a-col>
        <a-col :span="12">
          <a-card style="background-color: #0A537D">
            <a-statistic
                :value="passRate"
                :precision="2"
                suffix="%"
                class="demo-class"
                :value-style="{ color: '#66FFFF' }"
            >
              <template #title>
                <span style="color: #cc6464;font-family: 'YouSheTitleHei', sans-serif">学生及格率</span>
              </template>
            </a-statistic>
          </a-card>
        </a-col>
      </a-row>
    </div>
    <div>
      <dv-conical-column-chart :config="config" style="width:400px;height:200px;"/>
      <div style="display: flex;justify-content: space-around;margin-top: 5px">
        <dv-button @click="prevPage" border="Border4" color="#a6559d">上一页</dv-button>
        <dv-button @click="nextPage" border="Border5" color="#e18a3b">下一页</dv-button>
      </div>
    </div>

  </div>

</template>

<style scoped lang="scss">
@-webkit-keyframes shine { /*创建动画*/
  0%, 100% {
    color: #fff;
    text-shadow: 0 0 10px #0000FF, 0 0 10px #0000FF;
  }
  50% {
    text-shadow: 0 0 10px #0000FF, 0 0 40px #0000FF;
  }
}

.container {
  height: 100%;
  width: 100%;
  padding-left: 10px;
  padding-top: 5px;

  .title {
    text-align: center;

    span {
      font-weight: 700;
      color: #0000FF; /*设置文字颜色*/
      text-decoration: none;
      font-size: 20px; /*设置字体大小*/
      -webkit-animation: shine 2.4s infinite; /*设置动画*/
    }
  }

  .description {
    color: white;
    font-size: 12px;
    margin-top: 5px;
    display: flex;
    justify-content: space-between;
  }

}
</style>