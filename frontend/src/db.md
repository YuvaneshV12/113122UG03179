USE donotdelete;

CREATE TABLE urls (
  id INT AUTO_INCREMENT PRIMARY KEY,
  long_url TEXT NOT NULL,
  shortcode VARCHAR(10) UNIQUE NOT NULL,
  created_at DATETIME NOT NULL,
  expires_at DATETIME NOT NULL,
  click_count INT DEFAULT 0
);

CREATE TABLE clicks (
  id INT AUTO_INCREMENT PRIMARY KEY,
  shortcode VARCHAR(10),
  timestamp DATETIME,
  referrer TEXT,
  location TEXT,
  FOREIGN KEY (shortcode) REFERENCES urls(shortcode)
);