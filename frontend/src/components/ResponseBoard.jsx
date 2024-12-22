import React from "react";
import JobCard from "./JobCard";

const ResponseBoard = ({ data }) => {
  return (
    <div className="p-4 bg-white rounded shadow md:flex md:flex-col">
      {data ? (
        <div className="p-4 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {data.map((job) => (
            <JobCard key={job.id} job={job} />
          ))}
        </div>
      ) : (
        <div className="p-4 bg-red-100 rounded">
          <p className="text-red-800">No data available</p>
        </div>
      )}
    </div>
  );
};

export default ResponseBoard;
