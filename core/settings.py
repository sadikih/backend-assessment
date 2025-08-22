import os
import environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Initialize environment variables
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = env("SECRET_KEY", default="fallback-secret-key")

DEBUG = env.bool("DEBUG", default=True)

ALLOWED_HOSTS = []

# Database
# Use DATABASE_URL if available, otherwise fallback to SQLite
DATABASES = {
    "default": env.db(
        "DATABASE_URL",
        default=f"sqlite:///{os.path.join(BASE_DIR, 'db.sqlite3')}"
    )
}
