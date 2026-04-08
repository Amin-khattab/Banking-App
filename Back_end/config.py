import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
FRONT_END_DIR = BASE_DIR / "front_end"

load_dotenv(BASE_DIR / ".env")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:postgres@localhost:5432/banking_app",
)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
