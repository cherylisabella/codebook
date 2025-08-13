/************************************************************
 * 01_create_schema.sql
 * Airbnb Analytics — Data Model Foundation
 * Target: MySQL 8.0+
 * Notes: Run this script as root or a user with CREATE/ALTER
 *       privileges. This script drops & recreates the database
 *       so it's repeatable for local development.
 ************************************************************/

-- enforce strict SQL mode for data quality
SET @@GLOBAL.sql_mode = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
SET sql_mode = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- Drop DB if exists (safe for development)
DROP DATABASE IF EXISTS airbnb_analytics;
CREATE DATABASE airbnb_analytics CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
USE airbnb_analytics;

-- ---------------------------
-- LOCATION (normalized geo)
-- ---------------------------
CREATE TABLE Location (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  city VARCHAR(128) NOT NULL,
  region VARCHAR(128),
  country VARCHAR(64) DEFAULT 'Unknown',
  latitude DECIMAL(9,6),
  longitude DECIMAL(9,6),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY uq_location_city_region_country (city, region, country)
) ENGINE=InnoDB;

-- Rationale: centralize geo information so Listings and Hosts refer to a single source.

-- ---------------------------
-- HOST
-- ---------------------------
CREATE TABLE Host (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  phone_num VARCHAR(40) UNIQUE,
  email VARCHAR(255) UNIQUE,
  superhost BOOLEAN NOT NULL DEFAULT FALSE,
  response_time ENUM('Within an hour','Within 12 hours','Within a day','Within a few days') DEFAULT NULL,
  location_id INT UNSIGNED,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (location_id) REFERENCES Location(id) ON DELETE SET NULL
) ENGINE=InnoDB;

-- ---------------------------
-- GUEST
-- ---------------------------
CREATE TABLE Guest (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(128) NOT NULL,
  last_name VARCHAR(128) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_num VARCHAR(40) UNIQUE,
  location_id INT UNSIGNED,
  joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (location_id) REFERENCES Location(id) ON DELETE SET NULL
) ENGINE=InnoDB;

-- ---------------------------
-- LISTING
-- ---------------------------
CREATE TABLE Listing (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  host_id INT UNSIGNED NOT NULL,
  name VARCHAR(128) NOT NULL,
  description TEXT,
  price DECIMAL(9,2) NOT NULL CHECK (price > 0),
  location_id INT UNSIGNED,
  street VARCHAR(255),
  house_num VARCHAR(32),
  property_type ENUM('Entire Place','Private Rooms','Hotel Rooms','Shared Rooms') NOT NULL,
  bedroom_num TINYINT UNSIGNED NOT NULL CHECK (bedroom_num > 0 AND bedroom_num < 100),
  bathroom_num TINYINT UNSIGNED NOT NULL CHECK (bathroom_num > 0 AND bathroom_num < 100),
  guest_capacity TINYINT UNSIGNED NOT NULL CHECK (guest_capacity > 0 AND guest_capacity < 100),
  area_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (host_id) REFERENCES Host(id) ON DELETE CASCADE,
  FOREIGN KEY (location_id) REFERENCES Location(id) ON DELETE SET NULL
) ENGINE=InnoDB;

-- Index to support queries by location and price
CREATE INDEX idx_listing_location_price ON Listing(location_id, price);

-- ---------------------------
-- AMENITY
-- ---------------------------
CREATE TABLE Amenity (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  label VARCHAR(100) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- ---------------------------
-- LISTING_AMENITY (M:N)
-- ---------------------------
CREATE TABLE ListingAmenity (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  listing_id INT UNSIGNED NOT NULL,
  amenity_id INT UNSIGNED NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY uq_listing_amenity (listing_id, amenity_id),
  FOREIGN KEY (listing_id) REFERENCES Listing(id) ON DELETE CASCADE,
  FOREIGN KEY (amenity_id) REFERENCES Amenity(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- ---------------------------
-- BOOKING
-- ---------------------------
CREATE TABLE Booking (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  listing_id INT UNSIGNED NOT NULL,
  guest_id INT UNSIGNED NOT NULL,
  arrival_date DATE NOT NULL,
  departure_date DATE NOT NULL,
  booking_date DATE NOT NULL,
  status ENUM('confirmed','cancelled','no_show') DEFAULT 'confirmed',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CHECK (arrival_date < departure_date),
  CHECK (booking_date <= arrival_date),
  FOREIGN KEY (listing_id) REFERENCES Listing(id) ON DELETE CASCADE,
  FOREIGN KEY (guest_id) REFERENCES Guest(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Index to speed up availability / occupancy lookups
CREATE INDEX idx_booking_listing_dates ON Booking(listing_id, arrival_date, departure_date);
CREATE INDEX idx_booking_arrival_date ON Booking(arrival_date);

-- ---------------------------
-- PAYMENT
-- ---------------------------
CREATE TABLE Payment (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  booking_id INT UNSIGNED NOT NULL,
  paid_amount DECIMAL(12,2) NOT NULL CHECK (paid_amount >= 0),
  currency CHAR(3) DEFAULT 'USD' NOT NULL,
  method ENUM('card','paypal','bank_transfer') DEFAULT 'card',
  paid_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  status ENUM('paid','refunded','pending') DEFAULT 'paid',
  FOREIGN KEY (booking_id) REFERENCES Booking(id) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE INDEX idx_payment_paid_at ON Payment(paid_at);

-- ---------------------------
-- CANCELLATION
-- ---------------------------
CREATE TABLE Cancellation (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  booking_id INT UNSIGNED NOT NULL UNIQUE,
  cancelled_by ENUM('guest','host','system') DEFAULT 'guest',
  reason VARCHAR(255),
  cancelled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  refund_amount DECIMAL(12,2) DEFAULT 0 CHECK (refund_amount >= 0),
  FOREIGN KEY (booking_id) REFERENCES Booking(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- ---------------------------
-- REVIEW
-- ---------------------------
CREATE TABLE Review (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  listing_id INT UNSIGNED NOT NULL,
  guest_id INT UNSIGNED NOT NULL,
  comment TEXT,
  rating DECIMAL(3,2) NOT NULL CHECK (rating > 0 AND rating <= 5),
  created_at DATE NOT NULL,
  FOREIGN KEY (listing_id) REFERENCES Listing(id) ON DELETE CASCADE,
  FOREIGN KEY (guest_id) REFERENCES Guest(id) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE INDEX idx_review_listing_date ON Review(listing_id, created_at);

-- ---------------------------
-- OPTIONAL: ListingCalendar (day-level availability)
-- ---------------------------
-- Useful for exact occupancy and dynamic pricing. Commented out—enable if you plan day-level calculations.
-- CREATE TABLE ListingCalendar (
--   id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
--   listing_id INT UNSIGNED NOT NULL,
--   calendar_date DATE NOT NULL,
--   available BOOLEAN DEFAULT TRUE,
--   price_override DECIMAL(9,2),
--   UNIQUE (listing_id, calendar_date),
--   FOREIGN KEY (listing_id) REFERENCES Listing(id) ON DELETE CASCADE
-- ) ENGINE=InnoDB;

-- ---------------------------
-- Helpful: basic metadata table for schema migrations
-- ---------------------------
CREATE TABLE IF NOT EXISTS schema_migrations (
  id INT AUTO_INCREMENT PRIMARY KEY,
  script VARCHAR(255) NOT NULL,
  applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- initial migration record
INSERT INTO schema_migrations (script) VALUES ('01_create_schema.sql');

-- End of DDL
