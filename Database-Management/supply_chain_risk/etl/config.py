import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "")
DB_NAME = os.getenv("DB_NAME", "supply_chain_risk")

# folders
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPORTS_DIR = os.getenv("EXPORTS_DIR", os.path.join(PROJECT_ROOT, "exports"))
DOCS_DIR = os.getenv("DOCS_DIR", os.path.join(PROJECT_ROOT, "docs"))

os.makedirs(EXPORTS_DIR, exist_ok=True)
os.makedirs(DOCS_DIR, exist_ok=True)