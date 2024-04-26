<script setup lang="ts">
import {getCurrentInstance, onMounted, reactive, ref} from "vue";
import {request} from "@/request";
import {useClusterStore} from "@/stores/clusterStore";
import {storeToRefs} from "pinia";

const {spinning} = storeToRefs(useClusterStore())
const instance = getCurrentInstance()
const echarts = instance?.appContext.config.globalProperties.$echarts
const props = defineProps({
  name: {
    type: String,
    default: '宋显浩'
  }
})
const domRef = ref(null)
//@ts-ignore
let chart = null
const option = reactive({
  textStyle: {
    fontFamily: 'YouSheTitleHei',
  },
  backgroundColor: '#2da48f',
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'shadow'
    }
  },
  title: {
    text: `${props.name}成绩`,
    textStyle: {
      color: '#855f38',
      fontSize: 20
    },
    top: "10%",
    left: 'left',
// 		right: '5%'
  },
  grid: {
    left: '12%',
    top: '25%',
    bottom: '30%',
    right: '10%',
  },
  xAxis: {
    // name: 'X',
    nameTextStyle: {
      color: '#333333',
      padding: [0, 0, 0, 20],
    },
    show: true,
    axisLine: {
      show: true,
      lineStyle: {
        color: '#7bb4dc',
        shadowColor: 'rgba(91,100,134,1)',
        shadowOffsetX: '20',
      },
      symbol: ['none', 'arrow'],
      symbolOffset: [0, 25],
    },
    splitLine: {
      show: false,
      lineStyle: {
        color: 'rgba(255,255,255,0.2)',
      },
    },
    axisLabel: {
      show: true,
      // rotate: -1,
      textStyle: {
        fontSize: 14,
        // fontFamily: PangMenZhengDao,
        fontWeight: 500,
        rotate: '90',
        color: '#8839ea',
      },
      //@ts-ignore
      formatter: function (value, index) {
        let strs = value.split('');
        let str = ''
        for (var i = 0, s; s = strs[i++];) {
          str += s;
          if (!(i % 4)) str += '\n';
        }
        return str
      }
    },
    axisTick: {
      show: false,
    },
// 		data: ['物业纠纷', '其他合同', '道路交通']
    //@ts-ignore
    data: null
  },
  yAxis: [{
    nameTextStyle: {
      color: '#333333',
      padding: [0, 0, 0, 20],
    },
    max: 100,
    min: 0,
    splitNumber: (100 % 5).toFixed(0),
    show: true,
    axisTick: {
      show: false,
    },
    axisLine: {
      show: true,
      symbol: ['none', 'arrow'],
      symbolOffset: [0, 15],
      lineStyle: {
        // color: 'rgba(255, 129, 109, 0.1)',
        width: 1, //这里是为了突出显示加上的
        color: '#7bb4dc',
        shadowColor: 'rgba(91,100,134,1)',
      },
    },
    axisLabel: {
      show: true,
      textStyle: {
        fontSize: 12,
        // fontFamily: PangMenZhengDao,
        fontWeight: 600,
        color: '#000'
      },
    },
    splitArea: {
      areaStyle: {
        color: 'rgba(255,255,255,.5)',
      },
    },
    splitLine: {
      show: true,
      lineStyle: {
        color: '#cfe9f9',
        width: 1,
        type: 'solid',
      },
    }
  }],
  series: [{
    type: 'pictorialBar',
    barCategoryGap: '-20%',
    /*多个并排柱子设置柱子之间的间距*/
    // symbol: 'path://M0,10 L10,10 C5.5,10 5.5,5 5,0 C4.5,5 4.5,10 0,10 z',
    symbol: 'path://M0,10 L10,10 C5.5,10 6.5,5 5,5 C3.5,5 4.5,10 0,10 z',
    label: {
      show: true,
      position: 'top',
      distance: 10,
      color: '#000',
      fontWeight: 'bolder',
      fontSize: 12,
    },
    itemStyle: {
      normal: {
        //@ts-ignore
        color: params => {
          const colorList = [{
            type: 'linear',
            x: 0,
            y: 0,
            x2: 0,
            y2: 1,
            colorStops: [{
              offset: 0,
              color: '#297ff2',
            },
              {
                offset: 1,
                color: '#cce7fc',
              },
            ]
          },
            {
              type: 'linear',
              x: 0,
              y: 0,
              x2: 0,
              y2: 1,
              colorStops: [{
                offset: 0,
                color: '#3bfafe',
              },
                {
                  offset: 1,
                  color: '#aaf4fe',
                },
              ]
            },
            {
              type: 'linear',
              x: 0,
              y: 0,
              x2: 0,
              y2: 1,
              colorStops: [{
                offset: 0,
                color: '#e08440',
              },
                {
                  offset: 1,
                  color: '#decabd',
                },
              ]
            },
            {
              type: 'linear',
              x: 0,
              y: 0,
              x2: 0,
              y2: 1,
              colorStops: [{
                offset: 0,
                color: '#a7e36f',
              },
                {
                  offset: 1,
                  color: '#c3d31b',
                },
              ]
            },
            {
              type: 'linear',
              x: 0,
              y: 0,
              x2: 0,
              y2: 1,
              colorStops: [{
                offset: 0,
                color: '#69e5e5',
              },
                {
                  offset: 1,
                  color: '#77cacc',
                },
              ]
            },
            {
              type: 'linear',
              x: 0,
              y: 0,
              x2: 0,
              y2: 1,
              colorStops: [{
                offset: 0,
                color: '#2554ea',
              },
                {
                  offset: 1,
                  color: '#414867',
                },
              ]
            }
          ];
          return colorList[params.dataIndex];
        },
        opacity: 0.7
      },
      // 鼠标移入柱子上 透明度变为 1
      emphasis: {
        opacity: 1,
      },
    },
    data: null
    // data: [123, 60, 25]
  },],
})
const init = async () => {
  spinning.value = true
  let response = await request.get('/singleStudentGrade', {
    params: {
      'name': props.name
    }
  })
  let list = response.data.data
  option.title.text = `${props.name}成绩`
  //@ts-ignore
  option.series[0].data = list.map(v => {
    return v.value
  })
  //@ts-ignore
  option.xAxis.data = list.map(v => {
    return v.name
  })
  //@ts-ignore
  chart.setOption(option)
  spinning.value = false
}
onMounted(async () => {
  chart = echarts.init(document.getElementById('conical'))
  await init()
})
defineExpose({init})
</script>

<template>
  <div style="width: 540px;height: 330px" id="conical"></div>
</template>

<style scoped lang="scss">

</style>