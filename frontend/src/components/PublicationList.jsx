import { useEffect, useState } from "react";
import {
  getPublications,
  deletePublication
} from "../api/publications";

import EditPublication from "./EditPublication";

export default function PublicationList() {

  const [publications, setPublications] = useState([]);
  const [editingId, setEditingId] = useState(null);
  const [loading, setLoading] = useState(true);

  const fetchData = async () => {
    setLoading(true);
    const response = await getPublications();
    setPublications(response.data);
    setLoading(false);
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleDelete = async (id) => {
    const confirmDelete = window.confirm(
      "Are you sure you want to delete this publication?"
    );
    if (!confirmDelete) return;
    await deletePublication(id);
    fetchData();
  };

  if (loading) {
    return <p>Loading publications...</p>;
  }

  return (
    <div>

      {publications.map((pub) => (

        <div key={pub.id} className="publication-card">

          {editingId === pub.id ? (

            <EditPublication
              publication={pub}
              onUpdated={() => {
                setEditingId(null);
                fetchData();
              }}
            />

          ) : (

            <>
              <h3>{pub.title}</h3>

              <span className={pub.published ? "badge published" : "badge draft"}>
                {pub.published ? "Published" : "Draft"}
              </span>

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