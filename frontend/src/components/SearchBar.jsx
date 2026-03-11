import { useState } from "react";

export default function SearchBar({ onSearch }) {

  const [query, setQuery] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    onSearch(query);
  };

  return (
    <form onSubmit={handleSubmit} className="searchbar">
      <input
        type="text"
        placeholder="Search publications..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
    </form>
  );
}