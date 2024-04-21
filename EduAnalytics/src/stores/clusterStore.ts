import {defineStore} from "pinia";

export const useClusterStore = defineStore("clusterStore",{
    state() {
        return {
            cluster:3,
            score:0,
            method:'Kmeans',
            spinning:false
        }
    },
    actions:{},
    getters:{}
})