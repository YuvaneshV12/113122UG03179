Flask URL Shortener API

A simple Flask-based URL shortener service with support for expiry, analytics (click tracking), and short code customization.

Features

• Generate short links with optional custom shortcode
• Set expiry time (default 30 minutes)
• Redirect to original URL
• Track click statistics: timestamp, referrer, location (default "Unknown")
• MySQL database integration

Tech Stack

• Python Flask
• MySQL
• Flask-CORS
• pytz (timezone handling)

Setup Instructions

Clone or download the project.

Install dependencies:
pip install flask flask-cors mysql-connector-python pytz

Start the Flask server:
python app.py

Ensure MySQL is running and the database tables are created.

Database Schema

CREATE TABLE urls (
 id INT AUTO_INCREMENT PRIMARY KEY,
 long_url TEXT NOT NULL,
 shortcode VARCHAR(20) UNIQUE NOT NULL,
 created_at DATETIME NOT NULL,
 expires_at DATETIME NOT NULL,
 click_count INT DEFAULT 0
);

CREATE TABLE clicks (
 id INT AUTO_INCREMENT PRIMARY KEY,
 shortcode VARCHAR(20),
 timestamp DATETIME,
 referrer TEXT,
 location TEXT
);

Logs & Images
![Example Screenshot](logs/get1.png)
![Example Screenshot](logs/get2.png)
![Example Screenshot](logs/post1.png)


Postman Collection (Optional)

Export your Postman collection and place the .json file under:
C:\Users\govag\Desktop\Yuvanesh\Affordmen\backend\logs\Postman_Collection.json

Author

Developed by Govarthan & Yuvanesh
Location: C:\Users\govag\Desktop\Yuvanesh\Affordmen\backend

Notes

All times use IST (Asia/Kolkata) timezone

Location is "Unknown" until IP geolocation is added

Logging and screenshots can be saved in the /logs folder for analytics