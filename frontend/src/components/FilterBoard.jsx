import React from "react";

const FilterBoard = ({ filters }) => {
  return (
    <div className="mb-4 p-4 bg-white rounded shadow md:flex md:flex-wrap">
      {filters.length > 0 ? (
        filters.map((filter, index) => (
          <span
            key={index}
            className="m-1 p-2 bg-gray-200 text-gray-800 rounded"
          >
            {filter}
          </span>
        ))
      ) : (
        <p className="text-gray-500">No filters applied</p>
      )}
    </div>
  );
};

export default FilterBoard;
