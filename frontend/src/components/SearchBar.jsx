import React, { useState } from "react";

const SearchBar = ({ params, setParams, setData, setFilters }) => {
  const [filterInput, setFilterInput] = useState("");

  const addFilter = () => {
    if (filterInput) {
      setFilters((prevFilters) => [...prevFilters, filterInput]);
      setFilterInput("");
    }
  };

  return (
    <div className="mb-4 p-4 bg-white rounded shadow md:flex md:items-center md:justify-between">
      <input
        type="text"
        value={params || ""}
        onChange={(e) => setParams(e.target.value)}
        className="flex-grow p-2 border border-gray-300 rounded"
        placeholder="Search..."
      />
      <button
        onClick={() => setData(params)}
        className="mt-2 md:mt-0 md:ml-4 p-2 bg-blue-500 text-white rounded"
      >
        Search
      </button>
      <input
        type="text"
        value={filterInput}
        onChange={(e) => setFilterInput(e.target.value)}
        className="mt-2 md:mt-0 md:ml-4 p-2 border border-gray-300 rounded"
        placeholder="Add filter"
      />
      <button
        onClick={addFilter}
        className="mt-2 md:mt-0 md:ml-2 p-2 bg-green-500 text-white rounded"
      >
        Add Filter
      </button>
    </div>
  );
};

export default SearchBar;
