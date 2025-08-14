-- ==========================================
-- SCHEMA: Supply Chain Risk Management DB
-- ==========================================

-- Drop in dependency order
DROP TABLE IF EXISTS ShipmentRiskScore;
DROP TABLE IF EXISTS Incident;
DROP TABLE IF EXISTS Shipment;
DROP TABLE IF EXISTS Route;
DROP TABLE IF EXISTS Supplier;
DROP TABLE IF EXISTS RiskFactor;

-- Supplier
CREATE TABLE Supplier (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    industry VARCHAR(100),
    financial_score DECIMAL(4,2) CHECK (financial_score BETWEEN 0 AND 1),
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

-- Route
CREATE TABLE Route (
    route_id INT AUTO_INCREMENT PRIMARY KEY,
    origin VARCHAR(50) NOT NULL,
    origin_country VARCHAR(100) NOT NULL,
    destination VARCHAR(50) NOT NULL,
    destination_country VARCHAR(100) NOT NULL,
    distance_km INT,
    primary_mode ENUM('Sea','Air','Road','Rail') NOT NULL,
    alt_routes TEXT);

-- Shipment
CREATE TABLE Shipment (
    shipment_id INT AUTO_INCREMENT PRIMARY KEY,
    supplier_id INT NOT NULL,
    route_id INT NOT NULL,
    departure_date DATE,
    arrival_date DATE,
    status ENUM('In Transit','Delayed','Delivered') NOT NULL,
    FOREIGN KEY (supplier_id) REFERENCES Supplier(supplier_id),
    FOREIGN KEY (route_id) REFERENCES Route(route_id));

-- Incident (external events)
CREATE TABLE Incident (
    incident_id INT AUTO_INCREMENT PRIMARY KEY,
    location VARCHAR(50),
    country VARCHAR(100),
    date DATE,
    type VARCHAR(50),
    severity INT CHECK (severity BETWEEN 1 AND 5),
    description TEXT);

-- RiskFactor (reference library)
CREATE TABLE RiskFactor (
    factor_id INT AUTO_INCREMENT PRIMARY KEY,
    type VARCHAR(50),
    description TEXT,
    source VARCHAR(100),
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

-- Shipment Risk Score (AI outputs)
CREATE TABLE ShipmentRiskScore (
    shipment_id INT PRIMARY KEY,
    risk_score DECIMAL(4,2) CHECK (risk_score BETWEEN 0 AND 1),
    predicted_delay_days DECIMAL(5,2),
    generated_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (shipment_id) REFERENCES Shipment(shipment_id));

-- Indexes
CREATE INDEX idx_supplier_route ON Shipment(supplier_id, route_id);
CREATE INDEX idx_incident_date ON Incident(date);
CREATE INDEX idx_risk_score ON ShipmentRiskScore(risk_score);