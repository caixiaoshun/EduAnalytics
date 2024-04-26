import axios from "axios";

export const request = axios.create({
    baseURL: 'http://8.130.163.88:5000',
    timeout: 3000
});