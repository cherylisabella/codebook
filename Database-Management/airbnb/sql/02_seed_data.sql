USE airbnb_analytics;

/************************************************
 * 02_seed_data.sql
 * Expanded sample dataset for analytics testing
 ************************************************/

-- Clear tables if re-running
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE Review;
TRUNCATE TABLE Cancellation;
TRUNCATE TABLE Payment;
TRUNCATE TABLE Booking;
TRUNCATE TABLE ListingAmenity;
TRUNCATE TABLE Amenity;
TRUNCATE TABLE Listing;
TRUNCATE TABLE Guest;
TRUNCATE TABLE Host;
TRUNCATE TABLE Location;
SET FOREIGN_KEY_CHECKS = 1;

-- ----------------------------------------
-- Location
-- ----------------------------------------
INSERT INTO Location (city, region, country, latitude, longitude) VALUES
('Amsterdam', 'Noord-Holland', 'Netherlands', 52.3676, 4.9041),
('Berlin', 'Berlin', 'Germany', 52.5200, 13.4050),
('London', 'England', 'United Kingdom', 51.5072, -0.1276),
('Paris', 'Île-de-France', 'France', 48.8566, 2.3522),
('New York', 'New York', 'USA', 40.7128, -74.0060),
('Tokyo', 'Tokyo', 'Japan', 35.6762, 139.6503);

-- ----------------------------------------
-- Host
-- ----------------------------------------
INSERT INTO Host (name, phone_num, email, superhost, response_time, location_id) VALUES
('Daniel', '+31 71 462 3176', 'daniel@example.com', TRUE, 'Within an hour', 1),
('Alexander', '+49 30 1234567', 'alexander@example.com', TRUE, 'Within 12 hours', 2),
('Laura', '+44 20 7946 0958', 'laura@example.com', FALSE, 'Within a day', 3),
('Camille', '+33 1 23456789', 'camille@example.com', TRUE, 'Within an hour', 4),
('Jake', '+1 917 555 0198', 'jake@example.com', FALSE, 'Within a few days', 5),
('Ren', '+81 3 1234 5678', 'ren@example.com', TRUE, 'Within an hour', 6);

-- ----------------------------------------
-- Guest
-- ----------------------------------------
INSERT INTO Guest (first_name, last_name, email, phone_num, location_id) VALUES
('Jennifer', 'Smith', 'jennifer@example.com', '+1 202 918 2132', 5),
('Wilson', 'Chen', 'wilson@example.com', '+1 424 407 1029', 5),
('Alexandra', 'Wel', 'alexandra@example.com', '+49 1244 5449', 2),
('Lana', 'Anibel', 'lana@example.com', '+43 316 123 456', 4),
('Maxime', 'Roux', 'maxime@example.com', '+33 7 2638 2940', 4),
('Daniel', 'Smith', 'daniel.smith@example.com', '+44 7700 900454', 3),
('Ren', 'Ichiban', 'ren@example.com', '+81 50 803 1310', 6),
('Jim', 'Johnson', 'jim@example.com', '+44 161 496 0322', 3),
('Jake', 'Peralta', 'jake@example.com', '+1 917 413 7693', 5),
('Camille', 'Petit', 'camille@example.com', '+33 7676 00058', 4);

-- ----------------------------------------
-- Amenity
-- ----------------------------------------
INSERT INTO Amenity (label) VALUES
('Wifi'), ('Refrigerator'), ('Washer'), ('Dryer'), ('Shower Essentials'),
('Hangers'), ('Indoor Fireplace'), ('Fire Extinguisher'), ('TV'), ('Hot Tub'),
('Free Parking'), ('Kitchen'), ('First Aid Kit'), ('Hair Dryer'), ('Swimming Pool');

-- ----------------------------------------
-- Listing
-- ----------------------------------------
INSERT INTO Listing (host_id, name, description, price, location_id, street, house_num, property_type,
                     bedroom_num, bathroom_num, guest_capacity, area_description)
VALUES
(1, 'Quiet Garden View Room', 'Quiet neighborhood near city center', 90, 1, 'Hunzestraat', '821', 'Private Rooms', 1, 1, 2, 'Close to shops, quiet area'),
(2, 'Central Hotel Room', 'Cozy room with private bathroom', 165, 2, 'ZimmerStraße', '21', 'Hotel Rooms', 1, 1, 3, 'Quiet and central'),
(3, 'London Loft', 'Bright loft with city views', 200, 3, 'Newton Street', '15', 'Entire Place', 2, 2, 4, 'Near Covent Garden'),
(4, 'Charming Paris Apartment', 'Elegant furnished apartment in Paris', 150, 4, 'Rue de Rivoli', '101', 'Entire Place', 1, 1, 2, 'Historic neighborhood'),
(5, 'NYC Midtown Flat', 'Modern apartment in Midtown', 250, 5, '5th Avenue', '350', 'Entire Place', 2, 2, 4, 'Close to Times Square'),
(6, 'Tokyo Shibuya Studio', 'Compact, stylish studio', 120, 6, 'Shibuya Street', '88', 'Private Rooms', 1, 1, 2, 'Heart of Shibuya');

-- ----------------------------------------
-- Listing Amenities
-- ----------------------------------------
INSERT INTO ListingAmenity (listing_id, amenity_id) VALUES
(1, 1), (1, 12), (1, 5),
(2, 1), (2, 2), (2, 9),
(3, 1), (3, 12), (3, 15),
(4, 1), (4, 12), (4, 14),
(5, 1), (5, 2), (5, 9), (5, 10),
(6, 1), (6, 12), (6, 14);

-- ----------------------------------------
-- Booking
-- ----------------------------------------
INSERT INTO Booking (listing_id, guest_id, arrival_date, departure_date, booking_date, status) VALUES
(1, 1, '2025-05-10', '2025-05-12', '2025-04-01', 'confirmed'),
(2, 2, '2025-06-01', '2025-06-05', '2025-05-15', 'confirmed'),
(3, 3, '2025-07-10', '2025-07-15', '2025-06-20', 'confirmed'),
(4, 4, '2025-08-05', '2025-08-10', '2025-07-01', 'cancelled'),
(5, 5, '2025-09-01', '2025-09-07', '2025-08-10', 'confirmed'),
(6, 6, '2025-10-12', '2025-10-15', '2025-09-25', 'confirmed');

-- ----------------------------------------
-- Payment (with paid_at date)
-- ----------------------------------------
INSERT INTO Payment (booking_id, paid_amount, currency, method, status, paid_at) VALUES
(1, 180.00, 'EUR', 'card', 'paid', '2025-05-10'),
(2, 660.00, 'EUR', 'paypal', 'paid', '2025-06-01'),
(3, 1000.00, 'GBP', 'card', 'paid', '2025-07-10'),
(4, 0.00, 'EUR', 'card', 'refunded', NULL),
(5, 1500.00, 'USD', 'bank_transfer', 'paid', '2025-09-01'),
(6, 360.00, 'JPY', 'card', 'paid', '2025-10-12');

-- ----------------------------------------
-- Cancellation
-- ----------------------------------------
INSERT INTO Cancellation (booking_id, cancelled_by, reason, refund_amount) VALUES
(4, 'guest', 'Change of plans', 150.00);

-- ----------------------------------------
-- Review
-- ----------------------------------------
INSERT INTO Review (listing_id, guest_id, comment, rating, created_at) VALUES
(1, 1, 'Lovely host and location', 4.9, '2025-05-13'),
(2, 2, 'Very comfortable stay', 4.8, '2025-06-06'),
(3, 3, 'Excellent location, well equipped', 5.0, '2025-07-16'),
(5, 5, 'Great views, pricey but worth it', 4.7, '2025-09-08'),
(6, 6, 'Compact but great amenities', 4.5, '2025-10-16');