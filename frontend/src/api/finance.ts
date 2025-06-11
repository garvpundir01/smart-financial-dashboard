import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000", // your FastAPI backend
});

export const getAccountSummary = (accountId: number) =>
  API.get(`/transactions/summary/${accountId}`);

export const getMonthlySummary = (accountId: number) =>
  API.get(`/transactions/monthly-summary/${accountId}`);

export const getCategorySummary = (accountId: number) =>
  API.get(`/transactions/category-summary/${accountId}`);
