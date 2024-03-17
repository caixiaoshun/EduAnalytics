import axios from "axios";
// 创建 axios 请求实例
const request = axios.create({
    baseURL:" http://localhost:8000/", // 基础请求地址
    timeout: 3000, // 请求超时设置
    withCredentials: false, // 跨域请求是否需要携带 cookie
});

export default request