import React from "react";
import './style1.css';

const Stats = ({ stats }) => {
  return (
    <div>
      <h2>URL Stats</h2>
      <p><strong>Original URL:</strong> <a href={stats.original_url} target="_blank" rel="noopener noreferrer" className="text-blue-600 hover:underline break-words">{stats.original_url}</a></p>
      <p><strong>Created At:</strong> {new Date(stats.created_at).toLocaleString()}</p>
      <p><strong>Expires At:</strong> {new Date(stats.expires_at).toLocaleString()}</p>
      <p><strong>Total Clicks:</strong> {stats.click_count}</p>
      
      <h3>Click Logs:</h3>
      <ul>
        {stats.clicks.length === 0 && (
          <li>No click logs available</li>
        )}
        {stats.clicks.map((click, idx) => (
          <li key={idx} >
            <span>{new Date(click.timestamp).toLocaleString()}</span> —{" "}
            <span>{click.referrer || <em>No Referrer</em>}</span> —{" "}
            <span>{click.location}</span>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Stats;