#### 项目概述
EduAnalytics 是一个专为课堂数据追踪与可视化设计的应用程序，旨在为教师和教育管理者提供一个强大的工具集，以便更加直观、深入地分析学生的课堂表现。通过整合学生的课堂成绩、学习表现、自评和互评数据，EduAnalytics提供多维度的数据分析与可视化，帮助用户做出数据驱动的教学决策。系统包含前后端两部分，支持实时数据交互展示，并能够处理大规模的课堂数据，生成有针对性的分析报告。

---

### 目录结构

```
EduAnalytics-master/
│
├── EduAnalytics/  # 前端部分
│   ├── public/    # 静态资源文件
│   │   └── favicon.ico  # 网站图标
│   ├── src/       # 前端源码
│   │   ├── assets/  # 图像资源
│   │   ├── components/  # 组件（例如图表、学生聚类等）
│   │   ├── stores/  # Vuex store模块，负责状态管理
│   │   ├── views/   # 页面视图
│   │   ├── App.vue  # 主应用组件
│   │   └── main.ts  # 入口文件
│   ├── package.json  # 项目依赖和脚本
│   └── vite.config.ts  # 项目构建配置
│
└── api/           # 后端部分
    ├── app.py     # Flask后端服务
    ├── requirements.txt  # Python依赖文件
    └── data/      # 数据文件，包括学生成绩、自评、课堂表现等
```

---

### 前端部分

#### 1. 技术栈
- **框架**: Vue.js 3，使用现代的组件化开发方式，提升开发效率和代码可维护性。
- **状态管理**: Vuex，用于全局状态管理，确保应用内的数据在不同组件间的一致性和同步性。
- **构建工具**: Vite，极快的开发服务器和构建工具，简化了配置，并提供快速的开发环境。
- **样式**: 使用原生CSS，支持样式重置（reset.css）和自定义样式，保证界面的一致性和美观性。

#### 2. 关键组件

- **`ring-chart.vue`**: 环形图组件，用于展示如成绩分布等数据的环状分布，支持不同颜色和数据标签自定义。
- **`studentCluster.vue`**: 学生聚类可视化组件，基于学生的成绩和表现使用聚类算法进行分组，直观地展示学生的学习群体差异。
- **`studentPerformance2D.vue`**: 二维图组件，用于在坐标系中展示学生表现，提供多维数据分析支持。
- **`word-cloud-chart.vue`**: 词云图组件，通过解析学生自评中的关键词，生成视觉化的词汇分布图，展现学生情感和反馈的重点。

#### 3. 页面视图

- **`Home.vue`**: 系统首页，提供导航入口、系统概览以及关键功能的快捷访问。
- **`CourseOverview.vue`**: 课程概览页面，展示该课程所有班级和小组的总体表现、成绩概况。
- **`GradesList.vue`**: 成绩列表页面，支持按班级或小组查看详细成绩，带有搜索、筛选功能。
- **`resultAnalysic.vue`**: 成绩分析页面，展示成绩趋势图、对比图等，支持按时间或学生个体查询详细数据。
- **`welcome.vue`**: 系统指引页面，首次登录时向用户介绍主要功能和使用方法。

#### 4. 状态管理

- **`clusterStore.ts`**: 用于存储和管理学生聚类信息，能够根据不同的数据维度进行分组展示。
- **`studentPerformance.ts`**: 存储学生的表现数据，包括测试成绩、课堂活动参与、自评与小组评分等信息，为数据可视化提供支撑。

---

### 后端部分

#### 1. 技术栈
- **框架**: Flask，轻量级Python Web框架，适合快速构建REST API。
- **依赖管理**: 使用`requirements.txt`统一管理Python依赖库，如Flask、Pandas等。
- **数据处理**: 后端负责数据的处理、清洗和分析，确保前端所需的可视化数据按请求格式返回。

#### 2. 数据源

后端主要处理多个Excel数据文件，涵盖以下信息：
- **学生成绩数据**: 包含每次测试的分数、课堂表现、以及平时表现评分等。
- **自评与互评数据**: 学生在不同时间段的自评数据和对小组成员的评价，能够反映学生对自身及同伴表现的看法。
- **小组表现数据**: 包括小组作业的评分、小组内部成员之间的评分，以及每个成员的贡献值。

数据样例文件：
- `2022数据分析与处理技术课程分组数据依据.xlsx`
- `2022数据分析与处理技术课程自评.xlsx`
- `第一次组员打分表.xlsx`

#### 3. 后端接口设计

- **数据获取接口**: 后端提供了多种API接口，前端通过调用这些接口获取成绩、表现、评估数据。例如：`/api/grades`返回所有学生的成绩数据，`/api/cluster`返回学生聚类后的数据。
- **分析功能接口**: 后端集成了数据处理逻辑，支持基于不同维度（如班级、小组、个体）进行分析，并返回适用于可视化的结构化数据。

---

### 部署说明

#### 0. 拉取项目
```
git clone https://github.com/caixiaoshun/EduAnalytics.git
```

#### 1. 前端

1. **安装依赖**:
    ```bash
    pnpm install
    ```
2. **运行项目**:
    ```bash
    pnpm run dev
    ```
    该命令将在本地启动开发服务器，并自动打开浏览器预览页面。

3. **构建项目**:
    ```bash
    pnpm run build
    ```
    构建的静态文件将输出至`dist`目录下，供生产环境部署使用。

#### 2. 后端

1. **安装依赖**:
    ```bash
    pip install -r requirements.txt
    ```
2. **运行后端服务器**:
    ```bash
    python app.py
    ```
    服务器将启动在`localhost:5000`端口，前端可以通过此端口请求后端数据。

---

### 功能模块

#### 1. 数据可视化

- **环形图**: 显示成绩分布，直观展示不同分数段学生的比例。
- **学生聚类**: 采用K-Means等聚类算法将学生按成绩和表现分组，帮助教师识别不同群体的学习特点。
- **成绩分析**: 提供如折线图、柱状图等，分析学生成绩的变化趋势，显示整体进步情况。
- **词云图**: 基于学生的自评，生成关键词词云图，突出学生最常用的词汇和表达方式。

#### 2. 数据管理

- **小组打分和自评管理**: 支持从Excel中导入学生的自评和互评数据，系统自动汇总生成总分和组内贡献比例。
- **班级表现记录**: 系统定期统计班级每个学生的表现，通过量化的方式生成班级表现报告，帮助教师掌握全班动态。

---

### 潜在的改进方向

1. **机器学习模型集成**: 通过历史数据训练机器学习模型，预测学生未来的成绩走势与课堂表现，辅助教师决策。
2. **实时反馈系统**: 集成课堂实时反馈功能，教师能够立即获取学生的意见和建议，灵活调整教学策略。
3. **移动端支持**: 开发移动端应用或响应式网页设计，方便教师随时随地查看学生表现数据。

---

该系统通过综合应用前沿技术与教育数据分析方法，旨在为教师和教育管理者提供高效的数据可视化工具，提升课堂管理和教学质量。