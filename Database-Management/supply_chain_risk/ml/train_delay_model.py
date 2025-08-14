import os
import json
import joblib
import numpy as np
import pandas as pd
import mysql.connector as mysql
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from etl.config import DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME, PROJECT_ROOT

MODEL_DIR = os.path.join(PROJECT_ROOT, "ml", "artifacts")
os.makedirs(MODEL_DIR, exist_ok=True)
MODEL_PATH = os.path.join(MODEL_DIR, "delay_model.pkl")
FEATURES_META = os.path.join(MODEL_DIR, "features.json")

def connect():
    return mysql.connect(
        host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASS,
        database=DB_NAME)

def load_training_frame():
    q = """
    SELECT
      sh.shipment_id,
      DATEDIFF(sh.arrival_date, sh.departure_date) AS transit_days,
      CASE rt.primary_mode
        WHEN 'Sea' THEN 0 WHEN 'Air' THEN 1 WHEN 'Road' THEN 2 WHEN 'Rail' THEN 3
        ELSE 4
      END AS mode_code,
      LEAST(rt.distance_km, 20000) AS distance_km,
      COALESCE(NULLIF(s.financial_score,''),0.8) AS supplier_fin_score,
      r.risk_score,
      r.predicted_delay_days
    FROM Shipment sh
    JOIN Route rt ON rt.route_id = sh.route_id
    JOIN Supplier s ON s.supplier_id = sh.supplier_id
    JOIN ShipmentRiskScore r ON r.shipment_id = sh.shipment_id
    WHERE sh.departure_date IS NOT NULL AND sh.arrival_date IS NOT NULL
    """
    conn = connect()
    df = pd.read_sql(q, conn)
    conn.close()
    return df

def main():
    df = load_training_frame()
    if df.empty:
        raise RuntimeError("No training data found.")
    X = df[["transit_days","mode_code","distance_km","supplier_fin_score","risk_score"]].values
    y = df["predicted_delay_days"].values
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=7)
    model = GradientBoostingRegressor(random_state=7)
    model.fit(X_train, y_train)
    joblib.dump(model, MODEL_PATH)
    with open(FEATURES_META, "w") as f:
        json.dump({"columns":["transit_days","mode_code","distance_km","supplier_fin_score","risk_score"]}, f)

if __name__ == "__main__":
    main()