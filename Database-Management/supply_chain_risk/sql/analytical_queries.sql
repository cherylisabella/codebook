-- ==========================================
-- ANALYTICAL QUERIES — Supply Chain Risk DB
-- ==========================================
USE supply_chain_risk;

-- 1) Supplier risk (last 30 days)
WITH RecentRisk AS (
  SELECT sh.supplier_id, r.risk_score
  FROM Shipment sh
  JOIN ShipmentRiskScore r ON r.shipment_id = sh.shipment_id
  WHERE r.generated_on >= NOW() - INTERVAL 30 DAY)
SELECT s.supplier_id, s.name, ROUND(AVG(rr.risk_score), 3) AS avg_risk_30d
FROM Supplier s
JOIN RecentRisk rr ON rr.supplier_id = s.supplier_id
GROUP BY s.supplier_id, s.name
ORDER BY avg_risk_30d DESC;

-- 2) Top 15 shipments by risk with cumulative predicted delay
SELECT
  r.shipment_id,
  r.risk_score,
  r.predicted_delay_days,
  SUM(r.predicted_delay_days) OVER (ORDER BY r.risk_score DESC, r.shipment_id) AS cumulative_delay
FROM ShipmentRiskScore r
ORDER BY r.risk_score DESC, r.shipment_id
LIMIT 15;

-- 3) Monthly average risk trend (by departure month)
SELECT
  DATE_FORMAT(sh.departure_date, '%Y-%m') AS month,
  ROUND(AVG(r.risk_score), 3) AS avg_risk
FROM Shipment sh
JOIN ShipmentRiskScore r ON r.shipment_id = sh.shipment_id
GROUP BY month
ORDER BY month;

-- 4) Country corridor risk (origin_country -> destination_country)
WITH RiskByRoute AS (
    SELECT rt.origin_country,
           rt.destination_country,
           r.risk_score
    FROM Shipment sh
    JOIN Route rt ON rt.route_id = sh.route_id
    JOIN ShipmentRiskScore r ON r.shipment_id = sh.shipment_id),
RankedScores AS (
    SELECT origin_country,
           destination_country,
           risk_score,
           ROW_NUMBER() OVER (
               PARTITION BY origin_country, destination_country
               ORDER BY risk_score) AS rn,
           COUNT(*) OVER (
               PARTITION BY origin_country, destination_country) AS total
    FROM RiskByRoute),
RouteStats AS (
    SELECT origin_country,
           destination_country,
           COUNT(*) AS shipments,
           ROUND(AVG(risk_score), 3) AS avg_risk
    FROM RiskByRoute
    GROUP BY origin_country, destination_country),
P90 AS (
    SELECT origin_country,
           destination_country,
           MIN(risk_score) AS p90_risk
    FROM RankedScores
    WHERE rn >= total * 0.9
    GROUP BY origin_country, destination_country)
SELECT s.origin_country,
       s.destination_country,
       s.shipments,
       s.avg_risk,
       ROUND(p.p90_risk, 3) AS p90_risk
FROM RouteStats s
JOIN P90 p
  ON s.origin_country = p.origin_country
 AND s.destination_country = p.destination_country
ORDER BY s.avg_risk DESC, s.shipments DESC
LIMIT 25;


-- 5) Incident impact (shipments departing within +/- 3 days of an incident in same country)
WITH ShipCountry AS (
  SELECT sh.shipment_id, sh.departure_date, rt.origin_country
  FROM Shipment sh
  JOIN Route rt ON rt.route_id = sh.route_id
), IncidentWin AS (
  SELECT i.country, i.date AS incident_date, i.severity
  FROM Incident i
)
SELECT
  sc.origin_country,
  COUNT(*) AS impacted_shipments,
  ROUND(AVG(r.risk_score),3) AS avg_risk_impacted,
  ROUND(AVG(iw.severity),2) AS avg_severity
FROM ShipCountry sc
JOIN IncidentWin iw
  ON iw.country = sc.origin_country
 AND sc.departure_date BETWEEN DATE_SUB(iw.incident_date, INTERVAL 3 DAY)
                           AND DATE_ADD(iw.incident_date, INTERVAL 3 DAY)
JOIN ShipmentRiskScore r ON r.shipment_id = sc.shipment_id
GROUP BY sc.origin_country
ORDER BY impacted_shipments DESC;

-- 6) Supplier league table (volume, risk, on-time performance proxy)
WITH Base AS (
  SELECT
    s.supplier_id, s.name,
    r.risk_score,
    sh.status,
    DATEDIFF(sh.arrival_date, sh.departure_date) AS transit_days
  FROM Supplier s
  JOIN Shipment sh ON sh.supplier_id = s.supplier_id
  JOIN ShipmentRiskScore r ON r.shipment_id = sh.shipment_id
)
SELECT
  supplier_id, name,
  COUNT(*) AS shipments,
  ROUND(AVG(risk_score),3) AS avg_risk,
  ROUND(AVG(CASE WHEN status='Delivered' THEN 1 ELSE 0 END),3) AS delivery_rate,
  ROUND(AVG(transit_days),1) AS avg_transit_days,
  RANK() OVER (ORDER BY AVG(risk_score) DESC) AS risk_rank
FROM Base
GROUP BY supplier_id, name
ORDER BY avg_risk DESC, shipments DESC
LIMIT 25;

-- 7) High-risk shipments vs distance (are long routes riskier?)
SELECT
  CASE
    WHEN rt.distance_km < 2000 THEN '<2k'
    WHEN rt.distance_km < 5000 THEN '2k-5k'
    WHEN rt.distance_km < 10000 THEN '5k-10k'
    ELSE '>=10k'
  END AS bucket_distance_km,
  COUNT(*) AS shipments,
  ROUND(AVG(r.risk_score),3) AS avg_risk
FROM Shipment sh
JOIN Route rt ON rt.route_id = sh.route_id
JOIN ShipmentRiskScore r ON r.shipment_id = sh.shipment_id
GROUP BY bucket_distance_km
ORDER BY shipments DESC;

-- 8) Recent week risk momentum by corridor (7d vs prior 7d)
WITH Last7 AS (
  SELECT rt.origin_country, rt.destination_country, r.risk_score
  FROM Shipment sh
  JOIN Route rt ON rt.route_id = sh.route_id
  JOIN ShipmentRiskScore r ON r.shipment_id = sh.shipment_id
  WHERE r.generated_on >= NOW() - INTERVAL 7 DAY
),
Prev7 AS (
  SELECT rt.origin_country, rt.destination_country, r.risk_score
  FROM Shipment sh
  JOIN Route rt ON rt.route_id = sh.route_id
  JOIN ShipmentRiskScore r ON r.shipment_id = sh.shipment_id
  WHERE r.generated_on >= NOW() - INTERVAL 14 DAY
    AND r.generated_on < NOW() - INTERVAL 7 DAY
)
SELECT
  l.origin_country, l.destination_country,
  ROUND(AVG(l.risk_score),3) AS avg_risk_last7,
  ROUND(AVG(p.risk_score),3) AS avg_risk_prev7,
  ROUND(AVG(l.risk_score) - AVG(p.risk_score),3) AS delta
FROM Last7 l
LEFT JOIN Prev7 p
  ON p.origin_country = l.origin_country
 AND p.destination_country = l.destination_country
GROUP BY l.origin_country, l.destination_country
HAVING COUNT(l.risk_score) >= 5
ORDER BY delta DESC
LIMIT 20;

-- 9) Supplier exposure to high-risk corridors
WITH Corridor AS (
  SELECT sh.supplier_id, rt.origin_country, rt.destination_country, r.risk_score
  FROM Shipment sh
  JOIN Route rt ON rt.route_id = sh.route_id
  JOIN ShipmentRiskScore r ON r.shipment_id = sh.shipment_id
)
SELECT
  s.name,
  COUNT(*) AS shipments,
  ROUND(AVG(CASE WHEN risk_score >= 0.7 THEN 1 ELSE 0 END),3) AS high_risk_share
FROM Supplier s
JOIN Corridor c ON c.supplier_id = s.supplier_id
GROUP BY s.name
ORDER BY high_risk_share DESC, shipments DESC
LIMIT 25;

-- 10) Rolling 30-day supplier risk (window over time)
WITH Daily AS (
  SELECT
    sh.supplier_id,
    DATE(r.generated_on) AS d,
    AVG(r.risk_score) AS avg_risk_day
  FROM Shipment sh
  JOIN ShipmentRiskScore r ON r.shipment_id = sh.shipment_id
  GROUP BY sh.supplier_id, DATE(r.generated_on))
SELECT supplier_id, d,
       ROUND(AVG(avg_risk_day)
             OVER (PARTITION BY supplier_id ORDER BY d
                   ROWS BETWEEN 29 PRECEDING AND CURRENT ROW),3) AS roll30_avg_risk
FROM Daily
ORDER BY supplier_id, d;