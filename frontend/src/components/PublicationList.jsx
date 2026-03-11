import { deletePublication } from "../api/publications";
import { useState } from "react";
import EditPublication from "./EditPublication";

export default function PublicationList({ publications, refresh }) {

  const [editingId, setEditingId] = useState(null);

  const handleDelete = async (id) => {
    const confirmDelete = window.confirm(
      "Are you sure you want to delete this publication?"
    );
    if (!confirmDelete) return;

    await deletePublication(id);
    refresh();
  };

  return (
    <div>

      {publications.map((pub) => (

        <div key={pub.id} className="publication-card">

          {editingId === pub.id ? (

            <EditPublication
              publication={pub}
              onUpdated={() => {
                setEditingId(null);
                refresh();
              }}
            />

          ) : (

            <>
              <h3>{pub.title}</h3>

              <p><strong>Authors:</strong> {pub.authors}</p>

              <p>{pub.abstract}</p>

              <button className="secondary" onClick={() => setEditingId(pub.id)}>
                Edit
              </button>

              <button className="danger" onClick={() => handleDelete(pub.id)}>
                Delete
              </button>
            </>

          )}

        </div>

      ))}

    </div>
  );
}