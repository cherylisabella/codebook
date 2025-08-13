USE airbnb_analytics;

/************************************************************
 * 03_procs_triggers.sql
 * Business Rules, Automation, and Stored Procedures
 ************************************************************/

-- =========================================================
-- 1) Prevent Overlapping Bookings for Same Listing
-- =========================================================
DELIMITER $$
CREATE TRIGGER trg_prevent_booking_overlap
BEFORE INSERT ON Booking
FOR EACH ROW
BEGIN
    -- Only check for confirmed bookings
    IF NEW.status = 'confirmed' THEN
        IF EXISTS (
            SELECT 1
            FROM Booking b
            WHERE b.listing_id = NEW.listing_id
              AND b.status = 'confirmed'
              AND NOT (
                  NEW.departure_date <= b.arrival_date
                  OR NEW.arrival_date >= b.departure_date
              )
        ) THEN
            SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Booking conflict: listing already booked for overlapping dates';
        END IF;
    END IF;
END$$
DELIMITER ;

-- =========================================================
-- 2) Prevent Illogical Dates in Bookings (Arrival/Departure)
-- =========================================================
DELIMITER $$
CREATE TRIGGER trg_validate_booking_dates
BEFORE INSERT ON Booking
FOR EACH ROW
BEGIN
    IF NEW.arrival_date >= NEW.departure_date THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Invalid booking: arrival_date must be before departure_date';
    END IF;
    IF NEW.booking_date > NEW.arrival_date THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Invalid booking: booking_date must be before arrival_date';
    END IF;
END$$
DELIMITER ;

-- =========================================================
-- 3) Stored Procedure: Refresh SuperHost Status
-- Criteria:
-- - avg_rating >= 4.8 (last 180 days)
-- - cancellation_rate <= 2% (last 180 days)
-- - response_time <= 'Within 12 hours'
-- =========================================================
DELIMITER $$
CREATE PROCEDURE sp_refresh_superhosts()
BEGIN
    UPDATE Host h
    JOIN (
        SELECT
            l.host_id,
            AVG(r.rating) AS avg_rating,
            SUM(CASE WHEN c.id IS NOT NULL THEN 1 ELSE 0 END) / COUNT(b.id) AS cancellation_rate
        FROM Listing l
        JOIN Booking b ON b.listing_id = l.id
        LEFT JOIN Cancellation c ON c.booking_id = b.id
        LEFT JOIN Review r
            ON r.listing_id = l.id
            AND r.created_at >= DATE_SUB(CURDATE(), INTERVAL 180 DAY)
        WHERE b.booking_date >= DATE_SUB(CURDATE(), INTERVAL 180 DAY)
        GROUP BY l.host_id
    ) stats ON stats.host_id = h.id
    SET h.superhost = (
        stats.avg_rating >= 4.8
        AND stats.cancellation_rate <= 0.02
        AND h.response_time IN ('Within an hour','Within 12 hours')
    );
END$$
DELIMITER ;

-- =========================================================
-- 4) Stored Procedure: Monthly Revenue Snapshot by Host
-- =========================================================
DELIMITER $$
CREATE PROCEDURE sp_monthly_host_revenue(IN month_year CHAR(7))
BEGIN
    SELECT
        h.id AS host_id,
        h.name AS host_name,
        SUM(p.paid_amount) AS total_revenue
    FROM Host h
    JOIN Listing l ON l.host_id = h.id
    JOIN Booking b ON b.listing_id = l.id
    JOIN Payment p ON p.booking_id = b.id
    WHERE DATE_FORMAT(p.paid_at, '%Y-%m') = month_year
      AND p.status = 'paid'
    GROUP BY h.id, h.name
    ORDER BY total_revenue DESC;
END$$
DELIMITER ;

-- =========================================================
-- 5) Stored Procedure: Guest Lifetime Value
-- =========================================================
DELIMITER $$
CREATE PROCEDURE sp_guest_lifetime_value(IN guest_email VARCHAR(255))
BEGIN
    SELECT
        g.id AS guest_id,
        CONCAT(g.first_name, ' ', g.last_name) AS guest_name,
        SUM(p.paid_amount) AS lifetime_value,
        COUNT(DISTINCT b.id) AS total_bookings
    FROM Guest g
    JOIN Booking b ON b.guest_id = g.id
    JOIN Payment p ON p.booking_id = b.id
    WHERE g.email = guest_email
      AND p.status = 'paid'
    GROUP BY g.id, guest_name;
END$$
DELIMITER ;