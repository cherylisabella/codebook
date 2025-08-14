import os
import mysql.connector
from datetime import datetime
import subprocess

# Load env vars from GitHub Actions or local .env
from dotenv import load_dotenv
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

EXPORTS_DIR = os.path.join(os.path.dirname(__file__), "..", "exports")
os.makedirs(EXPORTS_DIR, exist_ok=True)

def run_sql_file(cursor, filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        sql = f.read()
    for statement in sql.split(";"):
        if statement.strip():
            cursor.execute(statement)

def export_query(cursor, query, filename):
    cursor.execute(query)
    rows = cursor.fetchall()
    headers = [col[0] for col in cursor.description]

    filepath = os.path.join(EXPORTS_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(",".join(headers) + "\n")
        for row in rows:
            f.write(",".join(map(str, row)) + "\n")

def main():

    # Connect to DB
    conn = mysql.connector.connect(
        host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASS, database=DB_NAME)
    cursor = conn.cursor()

    # Optional: Refresh materialized views
    conn.commit()

    # Run analytical queries & export results
    export_query(cursor,
        "SELECT * FROM mv_high_risk_shipments",
        f"mv_high_risk_shipments_{datetime.now().strftime('%Y%m%d')}.csv")
    export_query(cursor,
        "SELECT * FROM mv_country_corridors",
        f"mv_country_corridors_{datetime.now().strftime('%Y%m%d')}.csv")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()