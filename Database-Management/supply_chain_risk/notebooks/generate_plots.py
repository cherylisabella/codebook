import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector as mysql
from datetime import datetime
from dotenv import load_dotenv

# Load .env
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
load_dotenv(os.path.join(ROOT_DIR, ".env"))

DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

EXPORTS_DIR = os.path.join(ROOT_DIR, "exports")
DOCS_DIR = os.path.join(ROOT_DIR, "docs")
os.makedirs(DOCS_DIR, exist_ok=True)

ts = datetime.now().strftime("%Y%m%d_%H%M")

def connect():
    return mysql.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASS, database=DB_NAME)

def fetch_df(sql):
    conn = connect()
    df = pd.read_sql(sql, conn)
    conn.close()
    return df

def save_csv(df, name):
    path = os.path.join(EXPORTS_DIR, f"{name}_{ts}.csv")
    df.to_csv(path, index=False)

def save_plot(fig, name):
    path = os.path.join(DOCS_DIR, f"{name}_{ts}.png")
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)

if __name__ == "__main__":
    # 1) Supplier risk 30d
    df1 = fetch_df("""
        WITH RecentRisk AS (
          SELECT sh.supplier_id, r.risk_score
          FROM Shipment sh
          JOIN ShipmentRiskScore r ON r.shipment_id = sh.shipment_id
          WHERE r.generated_on >= NOW() - INTERVAL 30 DAY
        )
        SELECT s.name, ROUND(AVG(rr.risk_score),3) AS avg_risk_30d
        FROM Supplier s JOIN RecentRisk rr ON rr.supplier_id = s.supplier_id
        GROUP BY s.name ORDER BY avg_risk_30d DESC LIMIT 20;
    """)
    save_csv(df1, "supplier_risk_30d")
    if not df1.empty:
        fig, ax = plt.subplots()
        ax.bar(df1["name"], df1["avg_risk_30d"])
        ax.set_xlabel("Supplier"); ax.set_ylabel("Avg Risk (30d)")
        ax.set_title("Top Suppliers by Avg Risk (30d)")
        ax.tick_params(axis='x', rotation=60)
        save_plot(fig, "supplier_risk_30d")

    # 2) Corridor risk
    df2 = fetch_df("""
      SELECT origin_country, destination_country, shipments, avg_risk, p90_risk
      FROM mv_country_corridors
      ORDER BY avg_risk DESC, shipments DESC
      LIMIT 25;
      """)
    save_csv(df2, "corridor_risk_table")
    if len(df2) > 0:
        fig, ax = plt.subplots(figsize=(8, 6))
        labels = df2["origin_country"] + " → " + df2["destination_country"]
        ax.barh(labels, df2["avg_risk"])
        ax.set_xlabel("Avg Risk")
        ax.set_ylabel("Corridor")
        ax.set_title("Top Corridors by Avg Risk")
        ax.invert_yaxis()
        save_plot(fig, "corridor_risk_barh")
    else:
       print("No corridor data found.")

    # 3) Monthly risk trend
    df3 = fetch_df("""
      SELECT DATE_FORMAT(sh.departure_date, '%Y-%m') AS month,
             ROUND(AVG(r.risk_score), 3) AS avg_risk
      FROM Shipment sh JOIN ShipmentRiskScore r ON r.shipment_id = sh.shipment_id
      GROUP BY month ORDER BY month;
    """)
    save_csv(df3, "monthly_risk_trend")
    if not df3.empty:
        fig, ax = plt.subplots()
        ax.plot(df3["month"], df3["avg_risk"], marker="o")
        ax.set_xlabel("Month"); ax.set_ylabel("Avg Risk")
        ax.set_title("Monthly Average Risk")
        ax.tick_params(axis='x', rotation=45)
        save_plot(fig, "monthly_risk_trend")