/************************************************
 * Host Performance Analytics
 ************************************************/

-- 1. Top Hosts by Total Revenue
SELECT h.id, h.name,
       SUM(p.paid_amount) AS total_revenue
FROM Host h
JOIN Listing l ON l.host_id = h.id
JOIN Booking b ON b.listing_id = l.id
JOIN Payment p ON p.booking_id = b.id
WHERE p.status = 'paid'
GROUP BY h.id, h.name
ORDER BY total_revenue DESC;

-- 2. Average Rating per Host
SELECT h.id, h.name,
       AVG(r.rating) AS avg_rating
FROM Host h
JOIN Listing l ON l.host_id = h.id
JOIN Review r ON r.listing_id = l.id
GROUP BY h.id, h.name
ORDER BY avg_rating DESC;

-- 3. Host Occupancy Rate (booked nights / total nights)
WITH booked AS (
    SELECT l.host_id,
           SUM(DATEDIFF(b.departure_date, b.arrival_date)) AS booked_nights
    FROM Listing l
    JOIN Booking b ON b.listing_id = l.id
    WHERE b.status = 'confirmed'
    GROUP BY l.host_id
),
capacity AS (
    SELECT l.host_id,
           COUNT(l.id) * 365 AS available_nights_year
    FROM Listing l
    GROUP BY l.host_id
)
SELECT h.name,
       b.booked_nights / c.available_nights_year AS occupancy_rate
FROM booked b
JOIN capacity c ON c.host_id = b.host_id
JOIN Host h ON h.id = b.host_id;

/************************************************
 * Guest Behaviour
 ************************************************/
 -- 4. Repeat Guests (guests with more than 1 booking)
SELECT g.id, CONCAT(g.first_name, ' ', g.last_name) AS guest_name,
       COUNT(b.id) AS bookings_count
FROM Guest g
JOIN Booking b ON b.guest_id = g.id
GROUP BY g.id
HAVING COUNT(b.id) > 1;

-- 5. Guest Lifetime Value Ranking
SELECT g.id, CONCAT(g.first_name, ' ', g.last_name) AS guest_name,
       SUM(p.paid_amount) AS lifetime_value
FROM Guest g
JOIN Booking b ON b.guest_id = g.id
JOIN Payment p ON p.booking_id = b.id
WHERE p.status = 'paid'
GROUP BY g.id
ORDER BY lifetime_value DESC;

-- 6. Booking Lead Time (days between booking and arrival)
SELECT g.id, CONCAT(g.first_name, ' ', g.last_name) AS guest_name,
       AVG(DATEDIFF(b.arrival_date, b.booking_date)) AS avg_lead_days
FROM Guest g
JOIN Booking b ON b.guest_id = g.id
GROUP BY g.id
ORDER BY avg_lead_days DESC;

/************************************************
 * Listing Performance
 ************************************************/
 -- 7. Top Listings by Average Rating
SELECT l.id, l.name, AVG(r.rating) AS avg_rating
FROM Listing l
JOIN Review r ON r.listing_id = l.id
GROUP BY l.id
ORDER BY avg_rating DESC;

-- 8. Revenue per Listing
SELECT l.id, l.name, SUM(p.paid_amount) AS total_revenue
FROM Listing l
JOIN Booking b ON b.listing_id = l.id
JOIN Payment p ON p.booking_id = b.id
GROUP BY l.id
ORDER BY total_revenue DESC;

-- 9. Occupancy by Listing
SELECT l.id, l.name,
       SUM(DATEDIFF(b.departure_date, b.arrival_date)) AS booked_nights
FROM Listing l
JOIN Booking b ON b.listing_id = l.id
WHERE b.status = 'confirmed'
GROUP BY l.id
ORDER BY booked_nights DESC;

/************************************************
 * Amenities Impact
 ************************************************/
 -- 10. Most Common Amenities
SELECT a.label, COUNT(la.id) AS listings_with_amenity
FROM Amenity a
JOIN ListingAmenity la ON la.amenity_id = a.id
GROUP BY a.label
ORDER BY listings_with_amenity DESC;

-- 11. Amenities Correlated with High Ratings
SELECT a.label, AVG(r.rating) AS avg_rating
FROM Amenity a
JOIN ListingAmenity la ON la.amenity_id = a.id
JOIN Listing l ON l.id = la.listing_id
JOIN Review r ON r.listing_id = l.id
GROUP BY a.label
HAVING AVG(r.rating) >= 4.8
ORDER BY avg_rating DESC;

/************************************************
 * Time Series & Trends
 ************************************************/
 -- 12. Monthly Revenue by City
SELECT loc.city,
       DATE_FORMAT(p.paid_at, '%Y-%m') AS month,
       SUM(p.paid_amount) AS total_revenue
FROM Payment p
JOIN Booking b ON b.id = p.booking_id
JOIN Listing l ON l.id = b.listing_id
JOIN Location loc ON loc.id = l.location_id
GROUP BY loc.city, month
ORDER BY month, total_revenue DESC;

-- 13. Monthly Booking Count
SELECT DATE_FORMAT(b.booking_date, '%Y-%m') AS month,
       COUNT(*) AS booking_count
FROM Booking b
GROUP BY month
ORDER BY month;

-- 14. Rolling 3-Month Avg Rating per City
WITH city_ratings AS (
    SELECT loc.city, r.created_at, r.rating
    FROM Review r
    JOIN Listing l ON l.id = r.listing_id
    JOIN Location loc ON loc.id = l.location_id
)
SELECT city, created_at,
       AVG(rating) OVER (
           PARTITION BY city
           ORDER BY created_at
           ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
       ) AS rolling_avg_rating
FROM city_ratings;

/************************************************
 * Operational Insights
 ************************************************/
 -- 15. Cancellation Rate per Host
SELECT h.name,
       SUM(CASE WHEN c.id IS NOT NULL THEN 1 ELSE 0 END) / COUNT(b.id) AS cancellation_rate
FROM Host h
JOIN Listing l ON l.host_id = h.id
JOIN Booking b ON b.listing_id = l.id
LEFT JOIN Cancellation c ON c.booking_id = b.id
GROUP BY h.name
ORDER BY cancellation_rate;

-- 16. Average Booking Duration by City
SELECT loc.city,
       AVG(DATEDIFF(b.departure_date, b.arrival_date)) AS avg_stay_length
FROM Booking b
JOIN Listing l ON l.id = b.listing_id
JOIN Location loc ON loc.id = l.location_id
GROUP BY loc.city;

-- 17. Price Distribution by Property Type
SELECT property_type,
       MIN(price) AS min_price,
       MAX(price) AS max_price,
       AVG(price) AS avg_price
FROM Listing
GROUP BY property_type;

-- 18. Revenue Lost to Cancellations
SELECT SUM(c.refund_amount) AS total_refunds
FROM Cancellation c;

 /************************************************
 * Leaderboards
 ************************************************/
 -- 19. Top Guests by Number of Bookings
SELECT g.id, CONCAT(g.first_name, ' ', g.last_name) AS guest_name,
       COUNT(b.id) AS bookings_count
FROM Guest g
JOIN Booking b ON b.guest_id = g.id
GROUP BY g.id
ORDER BY bookings_count DESC;

-- 20. Host Leaderboard by Revenue & Rating
SELECT h.id, h.name,
       SUM(p.paid_amount) AS total_revenue,
       AVG(r.rating) AS avg_rating
FROM Host h
JOIN Listing l ON l.host_id = h.id
LEFT JOIN Booking b ON b.listing_id = l.id
LEFT JOIN Payment p ON p.booking_id = b.id
LEFT JOIN Review r ON r.listing_id = l.id
GROUP BY h.id
ORDER BY total_revenue DESC, avg_rating DESC;