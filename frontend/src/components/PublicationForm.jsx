import { useState } from "react";
import { createPublication } from "../api/publications";

export default function PublicationForm({ onCreated }) {
  const [form, setForm] = useState({
    title: "",
    abstract: "",
    authors: "",
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await createPublication(form);
    setForm({ title: "", abstract: "", authors: "" });
    onCreated();
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="title" value={form.title} onChange={handleChange} placeholder="Title" />
      <input name="authors" value={form.authors} onChange={handleChange} placeholder="Authors" />
      <textarea name="abstract" value={form.abstract} onChange={handleChange} placeholder="Abstract" />
      <button className="primary" type="submit">Create</button>
    </form>
  );
}