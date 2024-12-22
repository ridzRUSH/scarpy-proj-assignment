import React, { useEffect, useState } from "react";
import SearchBar from "./components/SearchBar";
import FilterBoard from "./components/FilterBoard";
import ResponseBoard from "./components/ResponseBoard";

const App = () => {
  const [params, setParams] = useState();
  const [data, setData] = useState();
  const [filters, setFilters] = useState([]);

  useEffect(() => {
    fetchJobs();
  }, []);

  async function fetchJobs() {
    const response = await fetch("http://127.0.0.1:8000/api/jobs");

    const jsonResponse = await response.json();
    setData(jsonResponse);
  }

  return (
    <div className="p-4">
      <SearchBar
        params={params}
        setParams={setParams}
        setData={setData}
        setFilters={setFilters}
      />
      <FilterBoard filters={filters} />
      <ResponseBoard data={data} />
    </div>
  );
};

export default App;
