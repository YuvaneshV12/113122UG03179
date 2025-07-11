import React, { useState } from "react";
import ShortenForm from "./components/ShortenForm.jsx";
import Stats from "./components/Stats";
import './components/style1.css';

function App() {
  const [shortLink, setShortLink] = useState('');
  const [stats, setStats] = useState('');

  return (
    <div>
      <h1>URL Shortener</h1>
      <ShortenForm setShortLink={setShortLink} setStats={setStats} />
      {shortLink && (
        <div>
          <p>Shortened URL:</p>
          <a href={shortLink.shortLink} target="_blank" rel="noreferrer">
            {shortLink.shortLink}
          </a>
          <p>Expires at: {new Date(shortLink.expiry).toLocaleString()}</p>
        </div>
      )}
      {stats && <Stats stats={stats} />}
    </div>
  );
}

export default App;