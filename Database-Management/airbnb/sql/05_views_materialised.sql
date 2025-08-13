USE airbnb_analytics;

/************************************************************
 * 05_views_materialised.sql
 * Pre-aggregated summary tables (Materialised Views)
 ************************************************************/

-- Drop if exists
DROP TABLE IF EXISTS mv_city_performance;

-- Create the materialized view table
CREATE TABLE mv_city_performance (
    city VARCHAR(255),
    total_bookings INT,
    total_revenue DECIMAL(10,2),
    avg_rating DECIMAL(3,2),
    PRIMARY KEY (city)
);

-- Initial load
INSERT INTO mv_city_performance (city, total_bookings, total_revenue, avg_rating)
SELECT loc.city,
       COUNT(DISTINCT b.id) AS total_bookings,
       SUM(p.paid_amount) AS total_revenue,
       AVG(r.rating) AS avg_rating
FROM Location loc
JOIN Listing l ON l.location_id = loc.id
JOIN Booking b ON b.listing_id = l.id
LEFT JOIN Payment p ON p.booking_id = b.id AND p.status = 'paid'
LEFT JOIN Review r ON r.listing_id = l.id
GROUP BY loc.city;

-- Add index for faster queries
CREATE INDEX idx_mv_city_performance_city ON mv_city_performance(city);

-- Refresh procedure
DELIMITER $$
CREATE PROCEDURE sp_refresh_mv_city_performance()
BEGIN
    TRUNCATE mv_city_performance;
    INSERT INTO mv_city_performance (city, total_bookings, total_revenue, avg_rating)
    SELECT loc.city,
           COUNT(DISTINCT b.id) AS total_bookings,
           SUM(p.paid_amount) AS total_revenue,
           AVG(r.rating) AS avg_rating
    FROM Location loc
    JOIN Listing l ON l.location_id = loc.id
    JOIN Booking b ON b.listing_id = l.id
    LEFT JOIN Payment p ON p.booking_id = b.id AND p.status = 'paid'
    LEFT JOIN Review r ON r.listing_id = l.id
    GROUP BY loc.city;
END$$
DELIMITER ;