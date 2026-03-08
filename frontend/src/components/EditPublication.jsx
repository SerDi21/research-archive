import { useState } from "react";
import { updatePublication } from "../api/publications";

export default function EditPublication({ publication, onUpdated }) {

  const [title, setTitle] = useState(publication.title);
  const [abstract, setAbstract] = useState(publication.abstract);

  const handleSubmit = async (e) => {
    e.preventDefault();

    await updatePublication(publication.id, {
      title,
      abstract
    });

    onUpdated();
  };

  return (
    <form onSubmit={handleSubmit}>

      <input
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />

      <textarea
        value={abstract}
        onChange={(e) => setAbstract(e.target.value)}
      />

      <button type="submit">
        Save
      </button>

    </form>
  );
}