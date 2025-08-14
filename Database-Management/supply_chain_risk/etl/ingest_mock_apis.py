import random
import mysql.connector as mysql
from datetime import date, timedelta
from faker import Faker
from config import DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME

fake = Faker()
random.seed(42)

def connect():
    return mysql.connect(
        host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASS,
        database=DB_NAME, autocommit=True)

def upsert_incidents(n=50):
    """Simulate fetching incidents & upsert into Incident."""
    conn = connect(); cur = conn.cursor()
    incident_types = ["Port Strike","Storm","Customs Delay","Road Block","Accident","Equipment Failure"]
    for _ in range(n):
        loc = fake.city()
        ctry = fake.country()
        d = date.today() - timedelta(days=random.randint(0, 14))
        itype = random.choice(incident_types)
        sev = random.randint(1,5)
        desc = fake.sentence().replace("'", "''")
        cur.execute(
            "INSERT INTO Incident (location, country, date, type, severity, description) "
            "VALUES (%s,%s,%s,%s,%s,%s)",
            (loc, ctry, d, itype, sev, desc))
    cur.close(); conn.close()

def upsert_risk_library():
    """Simulate reference library refresh."""
    conn = connect(); cur = conn.cursor()
    cur.execute("DELETE FROM RiskFactor")
    rows = [
        ("Financial","Liquidity squeeze risk","Credit Bureau"),
        ("Weather","Tropical storm season elevated","NOAA"),
        ("Political","Tariff policy unstable","GovWatch"),
        ("Operational","Port congestion likelihood","PortOps"),
        ("Logistics","Driver shortage risk","CarrierNet")]
    cur.executemany(
        "INSERT INTO RiskFactor (type, description, source) VALUES (%s,%s,%s)", rows)
    cur.close(); conn.close()

if __name__ == "__main__":
    upsert_incidents(50)
    upsert_risk_library()