<script setup lang="ts">

import Header from "@/components/Header.vue";
import ScoresLineGraph from "@/components/ScoresLineGraph.vue";
import GradeDescription from "@/components/gradeDescription.vue";
import StudentCluster from "@/components/studentCluster.vue";
import {useClusterStore} from "@/stores/clusterStore";
import {storeToRefs} from "pinia";
import {onMounted, reactive, type Ref, ref} from "vue";
import {message} from "ant-design-vue";
import WaterLevelChart from "@/components/WaterLevelChart.vue";
import StudentPerformance3D from "@/components/StudentPerformance3D.vue";
import WordCloudChart from "@/components/word-cloud-chart.vue";
import {useStudentPerformance} from "@/stores/studentPerformance";
import {request} from "@/request";
import StudentPerformance2D from "@/components/studentPerformance2D.vue";

const {cluster, score, method} = storeToRefs(useClusterStore())
const {showWhichChart} = storeToRefs(useStudentPerformance())
const options = [
  {
    value: "Kmeans",
    label: "Kmeans"
  },
  {
    value: "Spectral clustering",
    label: "Spectral clustering"
  },
  {
    value: "层次聚类",
    label: "层次聚类"
  },

]
const childDom = ref(null)
const ModelOpen = ref<boolean>(false);
const confirmLoading = ref<boolean>(false);
const formState = reactive({
  studentname: '',
  classTh: ''
})
const clusterStart = async () => {
  // @ts-ignore
  await childDom.value.init()
  message.success('聚类成功');
}
const handleOk = () => {

  if (formState.studentname.length === 0 && formState.classTh.length === 0) {
    message.error("请输入查询信息")
    return
  } else if (formState.studentname.length > 0) {
    showWhichChart.value = 1
  } else {
    showWhichChart.value = 2
  }
  ModelOpen.value = false
}
const handleClicik = () => {
  ModelOpen.value = true
  formState.studentname = ''
  formState.classTh = ''
  showWhichChart.value = 0
}
const student_names = ref()
const all_grades = ref()
onMounted(async () => {
  let response = await request.get("/getClassInformation")
  let data = response.data
  student_names.value = []
  for (let i = 0; i < data.student_names.length; i++) {
    student_names.value.push({
      value: data.student_names[i],
      label: data.student_names[i]
    })
  }
  all_grades.value = []
  for (let i = 0; i < data.all_classes.length; i++) {
    all_grades.value.push({
      value: data.all_classes[i],
      label: data.all_classes[i]
    })
  }
})
const getCurrentDate = () => {
  const date = new Date(); // 创建一个Date对象，表示当前时间
  const year = date.getFullYear(); // 获取四位数的年份
  const month = (date.getMonth() + 1).toString().padStart(2, '0'); // 获取月份，加1是因为getMonth()返回的月份是从0开始的
  const day = date.getDate().toString().padStart(2, '0'); // 获取日期

  return `${year}年${month}月${day}日`; // 返回格式化的日期字符串
}
const configs = [
  {
    data: [25, 100],
    shape: 'roundRect'
  },
  {
    data: [30, 90],
    shape: 'roundRect'
  },
  {
    data: [25, 100],
    shape: 'roundRect'
  },
  {
    data: [25, 100],
    shape: 'roundRect'
  },
]
</script>

<template>
  <div class="container">
    <Header></Header>
    <div class="content">
      <div class="left-item">
        <dv-border-box12 class="left-item-border">
          <div class="line-graph">
            <scores-line-graph></scores-line-graph>
          </div>
          <div style="width: 100%;height: 450px;margin-top:50px;">
            <!--    标题        -->
            <div style="display: flex;justify-content: space-between">
              <h2 style="color: #32C5FF;font-size: 20px">素养评价</h2>
              <div style="color: greenyellow;font-size: 12px">截止时间:{{ getCurrentDate() }}</div>
            </div>
            <!--    一排四个水位图        -->
            <div
                style="display: flex;color: white;justify-content: space-around;margin-bottom: 10px;font-weight: 700;font-size: 18px">
              <dv-decoration-11>知识与认知</dv-decoration-11>
              <dv-decoration-11>道德与情感</dv-decoration-11>
              <dv-decoration-11>实践与操作</dv-decoration-11>
              <dv-decoration-11>创新与批判</dv-decoration-11>
            </div>
            <div style="display: flex;justify-content: space-around">
              <dv-water-level-pond v-for="config in configs" :key="config" :config="config"
                                   style="width:110px;height:190px"/>
            </div>
            <div
                style="display: flex;color: white;font-weight: 500;justify-content: space-between;margin-top: 20px;font-size: 16px">
              <div>指标体系</div>
              <div>总占比</div>
              <div>计算标准</div>
            </div>
            <div class="gradient-hr"></div>

            <div
                style="display: flex;color: white;font-weight: 500;justify-content: space-between;margin-top: 20px;font-size: 16px">
              <div>课堂表现</div>
              <div style="color: #32C5FF;margin-left: 70px">10%</div>
              <div>课程发言，回答问题</div>
            </div>
            <div class="gradient-hr"></div>

            <div
                style="display: flex;color: white;font-weight: 500;justify-content: space-between;margin-top: 20px;font-size: 16px">
              <div>自评成绩</div>
              <div style="color: #32C5FF;margin-left: 70px">5%</div>
              <div>每次课程自评成绩加总</div>
            </div>
            <div class="gradient-hr"></div>

            <div
                style="display: flex;color: white;font-weight: 500;justify-content: space-between;margin-top: 20px;font-size: 16px">
              <div>他评成绩</div>
              <div style="color: #32C5FF;margin-left: 70px">5%</div>
              <div>每次课程他评成绩加总</div>
            </div>
            <div class="gradient-hr"></div>

            <div
                style="display: flex;color: white;font-weight: 500;justify-content: space-between;margin-top: 20px;font-size: 16px">
              <div>作业</div>
              <div style="color: #32C5FF;margin-left: 100px">30%</div>
              <div>作业完成情况打分加总</div>
            </div>
            <div class="gradient-hr"></div>

            <div
                style="display: flex;color: white;font-weight: 500;justify-content: space-between;margin-top: 20px;font-size: 16px">
              <div>期中成绩</div>
              <div style="color: #32C5FF;margin-left: 70px">10%</div>
              <div>期中作业完成情况打分</div>
            </div>
            <div class="gradient-hr"></div>

            <div
                style="display: flex;color: white;font-weight: 500;justify-content: space-between;margin-top: 20px;font-size: 16px">
              <div>期末成绩</div>
              <div style="color: #32C5FF;margin-left: 70px">10%</div>
              <div>期末作业完成情况打分</div>
            </div>
            <div class="gradient-hr"></div>

          </div>
        </dv-border-box12>
      </div>
      <div class="middle-item">
        <div class="middle-item-upper">
          <div>
            <div class="water-level-chart-item">
              <water-level-chart documentId="water-level-chart1" title="人文素养" :water-level="10"></water-level-chart>
            </div>
            <div class="water-level-chart-item">
              <water-level-chart documentId="water-level-chart2" title="团队协作能力"
                                 :water-level="20"></water-level-chart>
            </div>
            <div class="water-level-chart-item">
              <water-level-chart documentId="water-level-chart3" title="实验素养" :water-level="20"></water-level-chart>
            </div>

          </div>
          <div style="height: 420px;width: 500px">
            <div style="width: 500px;height: 420px">
              <word-cloud-chart></word-cloud-chart>
            </div>
          </div>

          <div>
            <div class="water-level-chart-item">
              <water-level-chart documentId="water-level-chart4" title="科学素养" :water-level="15"></water-level-chart>
            </div>
            <div class="water-level-chart-item">
              <water-level-chart documentId="water-level-chart5" title="信息化素养"
                                 :water-level="15"></water-level-chart>
            </div>
            <div class="water-level-chart-item">
              <water-level-chart documentId="water-level-chart6" title="创新素养" :water-level="20"></water-level-chart>
            </div>

          </div>
        </div>
        <div class="middle-item-lower">
          <div style="height: 400px;width: 600px">
            <StudentPerformance3D v-if="showWhichChart === 0"></StudentPerformance3D>
            <student-performance2-d v-else :student-name="formState.studentname" :class-th="formState.classTh"
                                    :title="showWhichChart === 1?formState.studentname:formState.classTh"></student-performance2-d>
          </div>
          <div>
            <dv-button :bg="false" @click="handleClicik" style="margin-bottom: 100px">查看学生或课堂详情
            </dv-button>
            <dv-button @click="showWhichChart = 0" border="Border2" color="#4c8045">查看总体学生表现</dv-button>
            <a-modal v-model:open="ModelOpen" title="查看学生或课堂详情" :confirm-loading="confirmLoading"
                     @ok="handleOk">
              <a-form>
                <a-form-item
                    label="学生姓名"
                >
                  <a-select
                      v-model:value="formState.studentname"
                      show-search
                      placeholder="请选择学生姓名"
                      style="width: 200px"
                      :options="student_names"
                      :disabled="!(formState.classTh.length === 0)"
                  ></a-select>
                </a-form-item>
                <a-form-item
                    label="第几堂课"
                >
                  <a-select
                      v-model:value="formState.classTh"
                      show-search
                      placeholder="请选择第几堂课"
                      style="width: 200px"
                      :options="all_grades"
                      :disabled="!(formState.studentname.length === 0)"
                  ></a-select>
                </a-form-item>
              </a-form>
            </a-modal>
          </div>

        </div>
      </div>
      <div class="right-item">
        <dv-border-box8>
          <div class="grade-description">
            <grade-description></grade-description>
          </div>
          <div class="student-cluster">
            <div style="display: flex;justify-content: space-around;margin-bottom: 10px">
              <span style="color: #32C5FF;font-size: 12px;height: 24px;line-height: 24px">聚类方法</span>
              <a-select
                  v-model:value="method"
                  show-search
                  placeholder="Select a person"
                  style="width: 200px"
                  :options="options"
                  size="small"
              ></a-select>
              <span style="color: #32C5FF;font-size: 12px;height: 24px;line-height: 24px">聚类数量</span>
              <a-input v-model:value.number="cluster" size="small" style="width: 100px"></a-input>

            </div>
            <div style="display: flex;justify-content: center;margin-bottom: 10px">
              <dv-button @click="clusterStart" border="Border6" color="#615ea8">进行聚类分析</dv-button>
            </div>
            <div
                style="height: 10px;width: 100%;display: flex;justify-content: space-around;margin-bottom: 10px;color: #32C5FF">
              <div>聚类数量</div>
              <div>轮廓系数</div>
            </div>
            <div style="height: 100px;width: 100%;display: flex;justify-content: space-around;margin-bottom: 10px">
              <dv-decoration-9 style="width:90px;height:90px;">
                <div class="decoration-9-content">
                  {{ cluster }}
                </div>
              </dv-decoration-9>

              <dv-decoration-9 style="width:90px;height:90px;">
                <div class="decoration-9-content">
                  {{ score.toFixed(2) }}
                </div>
              </dv-decoration-9>
            </div>
            <student-cluster ref="childDom"></student-cluster>

          </div>
        </dv-border-box8>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.content {
  height: 1200px;
  width: 100%;
  display: flex;

  .left-item {
    width: 450px;

    .left-item-border {
      padding-left: 25px;
      padding-right: 25px;
    }

    .line-graph {
      height: 488px;
      width: 100%;
    }
  }

  .middle-item {
    width: 1020px;

    .middle-item-upper {
      display: flex;
      padding-top: 10px;
      justify-content: space-around;

      .water-level-chart-item {
        width: 140px;
        height: 140px;
      }
    }

    .middle-item-lower {
      display: flex;
      margin-top: 10px;
      padding: 10px;
      align-items: center;
    }

  }

  .right-item {
    width: 450px;

    .grade-description {
      height: 444px;
      width: 100%;
    }

    .student-cluster {
      height: 542px;
      width: 100%;
    }
  }
}

.decoration-9-content {
  font-size: 28px;
  text-shadow: 0 0 3px #7acaec;
  color: #32C5FF;
  background-color: #06324F;
}

.gradient-hr {
  display: inline-block;
  width: 100%; /* 根据需要调整宽度 */
  height: 3px;
  background: linear-gradient(to right, #4a5357, #32C5FF, #4a5357);
}
</style>