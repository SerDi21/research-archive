import { useState, useEffect } from "react";
import PublicationList from "../components/PublicationList";
import PublicationForm from "../components/PublicationForm";
import SearchBar from "../components/SearchBar";
import { getPublications, searchPublications } from "../api/publications";

export default function Home() {
  const [publications, setPublications] = useState([]);

  const fetchPublications = async () => {
    const response = await getPublications()
    setPublications(response.data)
  }

  useEffect(() => {
    fetchPublications()
  }, [])

  const handleSearch = async (query) => {
    if (!query) {
      fetchPublications()
      return
    }

    const response = await searchPublications(query)
    setPublications(response.data)
  }

  const fetchAll = async () => {
    const response = await getPublications();
    setPublications(response.data);
  };

  useEffect(() => {
    fetchAll();
  }, []);

  return (
    <div>
      <SearchBar onSearch={handleSearch} />
      <PublicationForm onCreated={fetchAll} />
      <PublicationList publications={publications} />
    </div>
  );
}