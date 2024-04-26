<script setup lang="ts">
import {getCurrentInstance, onMounted} from "vue";

const instance = getCurrentInstance()
const echarts = instance?.appContext.config.globalProperties.$echarts
const options = {
  textStyle: {
    fontFamily: 'YouSheTitleHei',
  },
  series: [{
    type: 'wordCloud',
    shape: 'circle',
    // 这个功能没用过
    keepAspect: false,
    // 下面就是位置的配置
    left: 'center',
    top: 'center',
    width: '70%',
    height: '80%',
    right: null,
    bottom: null,
    // 词的大小，最小12px，最大60px，可以在这个范围调整词的大小
    sizeRange: [12, 60],
    // 每个词旋转的角度范围
    rotationRange: [-90, 90],
    rotationStep: 45,
    // 词间距，数值越小，间距越小，这里间距太小的话，会出现大词把小词套住的情况，比如一个大的口字，中间会有比较大的空隙，这时候他会把一些很小的字放在口字里面，这样的话，鼠标就无法选中里面的那个小字
    gridSize: 8,
    // 允许词太大的时候，超出画布的范围
    drawOutOfBound: false,
    // 布局的时候是否有动画
    layoutAnimation: true,
    // 这是全局的文字样式，相对应的还可以对每个词设置字体样式
    textStyle: {
      fontFamily: 'sans-serif',
      fontWeight: 'bold',
      // 颜色可以用一个函数来返回字符串
      color: function () {
        // Random color
        return 'rgb(' + [
          Math.round(Math.random() * 160),
          Math.round(Math.random() * 160),
          Math.round(Math.random() * 160)
        ].join(',') + ')';
      }
    },
    emphasis: {
      focus: 'self',
      textStyle: {
        textShadowBlur: 10,
        textShadowColor: '#333'
      }
    },

    // 数据必须是一个数组，数组是对象，对象必须有name和value属性
    data: [
      {
        name: '人文素养',
        value: 10 * 10
      },
      {
        name: '科学素养',
        value: 16 * 10
      },
      {
        name: '团队协作素养',
        value: 20 * 10
      },
      {
        name: '实验素养',
        value: 20 * 10
      },
      {
        name: '信息化素养',
        value: 15 * 10
      },
      {
        name: '创新素养',
        value: 20 * 10
      },
      {
        name: '沟通表达素养',
        value: 25
      },
      {
        name: '批判性思维素养',
        value: 20
      },
      {
        name: '问题解决素养',
        value: 22
      },
      {
        name: '自主学习素养',
        value: 18
      },
      {
        name: '跨文化交流素养',
        value: 21
      },
      {
        name: '心理素养',
        value: 24
      },
      {
        name: '沟通素养',
        value: 25
      },
      {
        name: '解决问题的能力',
        value: 23
      },
      {
        name: '批判性思维',
        value: 21
      },
      {
        name: '适应能力',
        value: 22
      },
      {
        name: '时间管理',
        value: 24
      },
      {
        name: '领导力',
        value: 27
      },
      {
        name: '自我管理',
        value: 26
      },
      {
        name: '人际关系',
        value: 28
      },
      {
        name: '解决冲突',
        value: 29
      },
      {
        name: '创业精神',
        value: 31
      },
      {
        name: '学习能力',
        value: 20
      },
      {
        name: '跨文化交流',
        value: 18
      },
      {
        name: '环境保护意识',
        value: 17
      },
      {
        name: '责任感',
        value: 32
      },
      {
        name: '判断力',
        value: 33
      },
      {
        name: '分析能力',
        value: 34
      },
      {
        name: '合作精神',
        value: 35
      },
      {
        name: '良好的口头表达能力',
        value: 36
      },
      {
        name: '快速学习能力',
        value: 37
      },
      {
        name: '创造力',
        value: 38
      },
      {
        name: '团队精神',
        value: 39
      },
      {
        name: '决策能力',
        value: 40
      },
      {
        name: '沟通能力',
        value: 41
      },
      {
        name: '逻辑思维',
        value: 42
      },
      {
        name: '批判性阅读能力',
        value: 43
      },
      {
        name: '应变能力',
        value: 44
      },
      {
        name: '自我激励能力',
        value: 45
      },
      {
        name: '学科知识',
        value: 46
      },
      {
        name: '公民意识',
        value: 47
      },
      {
        name: '创业意识',
        value: 48
      },
      {
        name: '创新意识',
        value: 49
      },
      {
        name: '协作意识',
        value: 50
      }
    ]

  }]
}
onMounted(() => {
  let myEcharts = echarts.init(document.getElementById('word-cloud'))
  myEcharts.setOption(options)
})
</script>

<template>
  <div id="word-cloud" style="width: 100%;height: 100%"></div>
</template>

<style scoped lang="scss">

</style>