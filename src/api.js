import axios from "axios";

const API = axios.create({
    baseURL: "http://127.0.0.1:5000/api"
});


export const getRoles = () => {
    return API.get("/roles");
};


export const startInterview = (data) => {
    return API.post("/start", data);
};


export const evaluateAnswer = (data) => {
    return API.post("/evaluate", data);
};


export const getResult = (id) => {
    return API.get(`/result/${id}`);
};


export const getHistory = () => {
    return API.get("/history");
};