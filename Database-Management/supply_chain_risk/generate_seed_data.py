import random
from faker import Faker
from datetime import timedelta

fake = Faker()
random.seed(77)

NUM_SUPPLIERS = 50
NUM_ROUTES = 100
NUM_SHIPMENTS = 1000
NUM_INCIDENTS = 200
NUM_RISK_FACTORS = 10

def esc(s):
    return s.replace("'", "''")

sql_lines = ["-- AUTO-GENERATED SEED DATA"]

# Suppliers
industries = [
    "Metals","Agriculture","Electronics","Textiles","Machinery",
    "Logistics","Forestry","Pharmaceuticals","Food Processing","Mining"]
for _ in range(NUM_SUPPLIERS):
    sql_lines.append(
        f"INSERT INTO Supplier (name, country, industry, financial_score) "
        f"VALUES ('{esc(fake.company())}', '{esc(fake.country())}', '{random.choice(industries)}', {round(random.uniform(0.6, 0.95), 2)});")

# Routes
for _ in range(NUM_ROUTES):
    sql_lines.append(
        f"INSERT INTO Route (origin, origin_country, destination, destination_country, distance_km, primary_mode, alt_routes) "
        f"VALUES ('{esc(fake.city())}', '{esc(fake.country())}', '{esc(fake.city())}', '{esc(fake.country())}', {random.randint(500, 15000)}, '{random.choice(['Sea','Air','Road','Rail'])}', 'Alt via {esc(fake.city())}');")

# Shipments
for _ in range(NUM_SHIPMENTS):
    dep_date = fake.date_between(start_date="-90d", end_date="today")
    arr_date = dep_date + timedelta(days=random.randint(2, 30))
    sql_lines.append(
        f"INSERT INTO Shipment (supplier_id, route_id, departure_date, arrival_date, status) "
        f"VALUES ({random.randint(1, NUM_SUPPLIERS)}, {random.randint(1, NUM_ROUTES)}, '{dep_date}', '{arr_date}', '{random.choice(['In Transit','Delayed','Delivered'])}');")

# Incidents (match schema: location, country, date, type, severity, description)
incident_types = ["Port Strike","Storm","Customs Delay","Road Block","Accident","Equipment Failure"]
for _ in range(NUM_INCIDENTS):
    sql_lines.append(
        f"INSERT INTO Incident (location, country, date, type, severity, description) "
        f"VALUES ('{esc(fake.city())}', '{esc(fake.country())}', '{fake.date_between(start_date='-90d', end_date='today')}', '{random.choice(incident_types)}', {random.randint(1,5)}, '{esc(fake.sentence())}');")

# Risk Factors
for _ in range(NUM_RISK_FACTORS):
    sql_lines.append(
        f"INSERT INTO RiskFactor (type, description, source) "
        f"VALUES ('{random.choice(['Financial','Weather','Political','Operational','Logistics'])}', '{esc(fake.sentence())}', '{esc(fake.company())}');")

# Shipment Risk Scores
for shipment_id in range(1, NUM_SHIPMENTS+1):
    risk = round(random.uniform(0.1, 0.95), 2)
    delay = round(random.uniform(0, 10), 1) if risk >= 0.7 else round(random.uniform(0, 3), 1)
    sql_lines.append(
        f"INSERT INTO ShipmentRiskScore (shipment_id, risk_score, predicted_delay_days) "
        f"VALUES ({shipment_id}, {risk}, {delay});")

with open("seed_data.sql", "w", encoding="utf-8") as f:
    f.write("\n".join(sql_lines))