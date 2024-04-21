import {defineStore} from "pinia";

export const useStudentPerformance = defineStore("studentPerformance",{
    state() {
        return {
            // 0 3D图
            // 1 查看学生详情
            // 2 查看课堂详情
            showWhichChart:0
        }
    },
    getters:{},
    actions:{}
})