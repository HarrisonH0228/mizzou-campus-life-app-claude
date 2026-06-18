import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Central configuration loaded from environment variables."""

    SECRET_KEY = os.getenv("SECRET_KEY") or "dev-fallback-key-change-in-prod"
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
    DEBUG = os.getenv("FLASK_DEBUG", "0") == "1"
