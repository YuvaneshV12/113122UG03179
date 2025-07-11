1.Set up a Flask backend with API routes to create short URLs, handle redirection, and fetch statistics.

2.Designed database tables for URLs and click logs, including fields for shortcodes, timestamps, expiry, and click counts.

3.Implemented unique shortcode generation supporting user-defined custom codes and automatic random codes.

4.Added URL expiry feature by storing creation and expiration times and preventing redirection if expired.

5.Tracked clicks by recording timestamp, referrer, and location data for each access to a short URL.

6.Created a React frontend form to input original URL, custom shortcode, and validity duration.

7.Used Axios in React to communicate with backend APIs for creating short URLs and fetching stats.

8.Styled the frontend with plain CSS, focusing on colored input borders, button hover effects, and clean layout.

9.Centered the form on the page with proper spacing, white background, and subtle shadow for a neat appearance.

10.Handled form submission and errors gracefully, preventing Enter key submission and showing alert messages for failures.