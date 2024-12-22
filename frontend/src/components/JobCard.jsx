import React from "react";

const JobCard = ({ job }) => {
  return (
    <div className="max-w-sm w-full lg:max-w-full lg:flex shadow-lg rounded-lg overflow-hidden mb-4">
      <div className="p-4 bg-white flex flex-col justify-between leading-normal">
        <div className="mb-8">
          <div className="text-gray-900 font-bold text-xl mb-2">
            {job.job_title}
          </div>
          <p className="text-gray-700 text-base">{job.job_details}</p>
        </div>
        <div className="flex items-center">
          <div className="text-sm">
            <p className="text-gray-900 leading-none">{job.location}</p>
            <p className="text-gray-600">{job.employment_type.join(", ")}</p>
            <p className="text-gray-600">
              {job.compensation.min} - {job.compensation.max}
            </p>
            <p className="text-gray-600">
              Posted: {new Date(job.posted_at).toDateString()}
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default JobCard;
