import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:5000"
});

export const getPublications = () =>
  API.get("/publications");

export const createPublication = (data) =>
  API.post("/publications", data);

export const searchPublications = (query) =>
  API.get(`/search?q=${query}`);

export const updatePublication = (id, data) =>
  API.put(`/publications/${id}`, data);

export const deletePublication = (id) =>
  API.delete(`/publications/${id}`);