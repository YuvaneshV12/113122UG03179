import React, { useState } from "react";
import axios from "axios";
import './style1.css';

const ShortenForm = ({ setShortLink, setStats }) => {
  const [url, setUrl] = useState("");
  const [shortcode, setShortcode] = useState("");
  const [validity, setValidity] = useState(30);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post("http://localhost:5000/shorturls", { url, shortcode, validity: Number(validity) });
      setShortLink(res.data);
      setStats(null);
    } catch (err) {
      alert(err.response?.data?.error || "Error creating short URL");
    }
  };

  const handleStats = async () => {
    try {
      const res = await axios.get(`http://localhost:5000/shorturls/${shortcode}`);
      setStats(res.data);
      setShortLink(null);
    } catch (err) {
      alert(err.response?.data?.error || "Error fetching stats");
    }
  };

  const preventEnterSubmit = (e) => { if (e.key === "Enter") e.preventDefault(); };

  return (
    <form onSubmit={handleSubmit}>
      <input type="url" placeholder="Enter URL" value={url} onChange={e => setUrl(e.target.value)} required onKeyDown={preventEnterSubmit}/>
      <input type="text" placeholder="Custom shortcode" value={shortcode} onChange={e => setShortcode(e.target.value)} onKeyDown={preventEnterSubmit}/>
      <input type="number" placeholder="Validity in minutes" value={validity} onChange={e => setValidity(e.target.value)} onKeyDown={preventEnterSubmit}/>
      <button type="submit">Create Short URL</button>
      <button type="button" onClick={handleStats}>Get Stats</button>
    </form>
  );
};

export default ShortenForm;