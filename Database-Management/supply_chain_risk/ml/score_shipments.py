import os
import joblib
import pandas as pd
import mysql.connector as mysql
from etl.config import DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME, PROJECT_ROOT

MODEL_PATH = os.path.join(PROJECT_ROOT, "ml", "artifacts", "delay_model.pkl")

def connect(autocommit=True):
    return mysql.connect(
        host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASS,
        database=DB_NAME, autocommit=autocommit)

def frame_to_score():
    q = """
    SELECT
      sh.shipment_id,
      DATEDIFF(sh.arrival_date, sh.departure_date) AS transit_days,
      CASE rt.primary_mode
        WHEN 'Sea' THEN 0 WHEN 'Air' THEN 1 WHEN 'Road' THEN 2 WHEN 'Rail' THEN 3
        ELSE 4
      END AS mode_code,
      LEAST(rt.distance_km, 20000) AS distance_km,
      COALESCE(s.financial_score,0.8) AS supplier_fin_score,
      r.risk_score
    FROM Shipment sh
    JOIN Route rt ON rt.route_id = sh.route_id
    JOIN Supplier s ON s.supplier_id = sh.supplier_id
    LEFT JOIN ShipmentRiskScore r ON r.shipment_id = sh.shipment_id
    """
    conn = connect(False)
    df = pd.read_sql(q, conn)
    conn.close()
    return df

def upsert_scores(df_out):
    conn = connect(True)
    cur = conn.cursor()
    sql = """
    INSERT INTO ShipmentRiskScore (shipment_id, risk_score, predicted_delay_days)
    VALUES (%s,%s,%s)
    ON DUPLICATE KEY UPDATE
      risk_score = VALUES(risk_score),
      predicted_delay_days = VALUES(predicted_delay_days),
      generated_on = CURRENT_TIMESTAMP
    """
    cur.executemany(sql, list(df_out[["shipment_id","risk_score","predicted_delay_days"]].itertuples(index=False, name=None)))
    cur.close(); conn.close()

def main():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Model not found. Train first: python ml/train_delay_model.py")
    model = joblib.load(MODEL_PATH)

    df = frame_to_score()
    if df.empty: return
    feature_cols = ["transit_days","mode_code","distance_km","supplier_fin_score","risk_score"]
    X = df[feature_cols].fillna(0).values
    y_pred = model.predict(X)

    df_out = df[["shipment_id","risk_score"]].copy()
    df_out["predicted_delay_days"] = y_pred.round(2)

    upsert_scores(df_out)

if __name__ == "__main__":
    main()