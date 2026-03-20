import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

# load environment variables from .env (if present)
load_dotenv()


# =========================
# MongoDB Environment Config
# =========================
MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_CLUSTER = os.getenv("MONGO_CLUSTER")

DATABASE_NAME = os.getenv("MONGO_DATABASE_NAME")
COLLECTION_NAME = os.getenv("MONGO_COLLECTION_NAME")


# =========================
# Validation
# =========================

if not MONGO_USERNAME:
    raise ValueError("MONGO_USERNAME is not set in environment variables")

if not MONGO_PASSWORD:
    raise ValueError("MONGO_PASSWORD is not set in environment variables")

if not MONGO_CLUSTER:
    raise ValueError("MONGO_CLUSTER is not set in environment variables")


# =========================
# Build Mongo URI (safe)
# =========================

ENCODED_PASSWORD = quote_plus(MONGO_PASSWORD)

MONGO_URI = (
    f"mongodb+srv://{MONGO_USERNAME}:{ENCODED_PASSWORD}@{MONGO_CLUSTER}/"
    "?retryWrites=true&w=majority"
)
