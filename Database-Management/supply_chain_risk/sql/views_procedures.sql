-- High-risk materialized table + refresh proc
DROP TABLE IF EXISTS mv_high_risk_shipments;
CREATE TABLE mv_high_risk_shipments (
    shipment_id INT UNSIGNED PRIMARY KEY,
    risk_score DECIMAL(4,2),
    predicted_delay_days DECIMAL(5,2),
    generated_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

DELIMITER //
DROP PROCEDURE IF EXISTS sp_refresh_mv_high_risk_shipments//
CREATE PROCEDURE sp_refresh_mv_high_risk_shipments()
BEGIN
  TRUNCATE TABLE mv_high_risk_shipments;
  INSERT INTO mv_high_risk_shipments (shipment_id, risk_score, predicted_delay_days)
  SELECT shipment_id, risk_score, predicted_delay_days
  FROM ShipmentRiskScore
  WHERE risk_score >= 0.7;
END//
DELIMITER ;

-- Helpful views
CREATE OR REPLACE VIEW v_supplier_risk AS
SELECT s.supplier_id, s.name AS supplier_name, AVG(r.risk_score) AS avg_risk
FROM Supplier s
JOIN Shipment sh ON s.supplier_id = sh.supplier_id
JOIN ShipmentRiskScore r ON sh.shipment_id = r.shipment_id
GROUP BY s.supplier_id, s.name;

CREATE OR REPLACE VIEW v_route_corridor AS
SELECT r.route_id, r.origin, r.origin_country, r.destination, r.destination_country,
       COUNT(sh.shipment_id) AS shipments, ROUND(AVG(rsk.risk_score),2) AS avg_risk
FROM Route r
LEFT JOIN Shipment sh ON r.route_id = sh.route_id
LEFT JOIN ShipmentRiskScore rsk ON sh.shipment_id = rsk.shipment_id
GROUP BY r.route_id, r.origin, r.origin_country, r.destination, r.destination_country;