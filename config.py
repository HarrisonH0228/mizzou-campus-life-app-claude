import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Central configuration loaded from environment variables."""

    SECRET_KEY = os.getenv("SECRET_KEY", "dev-fallback-key-change-in-prod")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
    FLASK_ENV = os.getenv("FLASK_ENV", "production")
    DEBUG = FLASK_ENV == "development"
