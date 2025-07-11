from flask import Flask, request, jsonify, redirect
from flask_cors import CORS
from datetime import datetime, timedelta
import pytz
import mysql.connector
import string
import random

app = Flask(__name__)
CORS(app)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Gova@12345",
        database="donotdelete"
    )

def generate_shortcode(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route("/shorturls", methods=["POST"])
def create_short_url():
    data = request.get_json()
    url = data.get("url")
    shortcode = data.get("shortcode")
    validity = int(data.get("validity", 30))

    if not url:
        return jsonify({"error": "URL is required"}), 400

    if not shortcode:
        shortcode = generate_shortcode()

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM urls WHERE shortcode = %s", (shortcode,))
    existing = cursor.fetchone()

    if existing:
        cursor.close()
        conn.close()
        return jsonify({"error": "Shortcode already exists"}), 409

    IST = pytz.timezone('Asia/Kolkata')
    created_at = datetime.now(IST).replace(tzinfo=None)
    expires_at = (created_at + timedelta(minutes=validity)).replace(tzinfo=None)

    cursor.execute("""
        INSERT INTO urls (long_url, shortcode, created_at, expires_at)
        VALUES (%s, %s, %s, %s)
    """, (url, shortcode, created_at, expires_at))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({
        "shortLink": f"http://localhost:5000/{shortcode}",
        "expiry": expires_at.isoformat()
    }), 201

@app.route("/<shortcode>")
def redirect_url(shortcode):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM urls WHERE shortcode = %s", (shortcode,))
    url_data = cursor.fetchone()

    if not url_data:
        cursor.close()
        conn.close()
        return jsonify({"error": "Shortcode not found"}), 404

    IST = pytz.timezone('Asia/Kolkata')
    now = datetime.now(IST).replace(tzinfo=None)

    if url_data["expires_at"] < now:
        cursor.close()
        conn.close()
        return jsonify({"error": "Link expired"}), 410

    cursor.execute("UPDATE urls SET click_count = click_count + 1 WHERE shortcode = %s", (shortcode,))
    cursor.execute("""
        INSERT INTO clicks (shortcode, timestamp, referrer, location)
        VALUES (%s, %s, %s, %s)
    """, (shortcode, now, request.referrer or "Unknown", "Unknown"))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_data["long_url"])

@app.route("/shorturls/<shortcode>", methods=["GET"])
def get_stats(shortcode):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM urls WHERE shortcode = %s", (shortcode,))
    url = cursor.fetchone()

    if not url:
        cursor.close()
        conn.close()
        return jsonify({"error": "Shortcode not found"}), 404

    cursor.execute("SELECT * FROM clicks WHERE shortcode = %s", (shortcode,))
    clicks = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify({
        "original_url": url["long_url"],
        "created_at": url["created_at"].isoformat(),
        "expires_at": url["expires_at"].isoformat(),
        "click_count": url["click_count"],
        "clicks": [
            {
                "timestamp": click["timestamp"].isoformat(),
                "referrer": click["referrer"],
                "location": click["location"]
            }
            for click in clicks
        ]
    })

if __name__ == "__main__":
    app.run(debug=True)