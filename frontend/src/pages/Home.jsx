import { useState, useEffect } from "react";
import PublicationList from "../components/PublicationList";
import PublicationForm from "../components/PublicationForm";
import SearchBar from "../components/SearchBar";
import { getPublications, searchPublications } from "../api/publications";

export default function Home() {

  const [publications, setPublications] = useState([]);
  const [showForm, setShowForm] = useState(false);

  const fetchAll = async () => {
    try {
      const response = await getPublications();
      setPublications(response.data);
    } catch (error) {
      console.log("Backend not ready, retrying...");
      setTimeout(fetchAll, 2000);
    }
  };

  useEffect(() => {
    fetchAll();
  }, []);

  const handleSearch = async (query) => {

    if (!query) {
      fetchAll();
      return;
    }

    const response = await searchPublications(query);
    setPublications(response.data.results);
  };

  return (
    <div>

      <header className="topbar">

        <h1>Research Publications</h1>

        <div className="topbar-right">
          <button
            className="primary"
            onClick={() => setShowForm(true)}
          >
            New Publication
          </button>
          <SearchBar onSearch={handleSearch} />
        </div>

      </header>

      <main className="content">
        <PublicationList publications={publications} refresh={fetchAll} />
      </main>

      {showForm && (
        <div className="modal-overlay">
          <div className="modal">
            <h2>Create Publication</h2>

            <PublicationForm
              onCreated={() => {
                fetchAll();
                setShowForm(false);
              }}
            />

            <button
              className="secondary"
              onClick={() => setShowForm(false)}
            >
              Close
            </button>

          </div>
        </div>
      )}

    </div>
  );
}