# config.py
"""
SrinivasKalyan Buthkur - Framework Configuration
This module aggregates environment variables and system-level settings, ensuring 
clean decoupled configurations for local and production hosts.
"""

import os

class Settings:
    # Project Info
    PROJECT_NAME: str = "Srinivas Portfolio RAG API"
    VERSION: str = "2.0.4"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")

    # Network Binding (Defaults to Port 3000 as per AI Studio specifications)
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", 3000))

    # CORS Allowed Origins (Wildcard allowed for portfolio deployment ease)
    ALLOWED_ORIGINS: list = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
        "*", # Fallback for easy sharing
    ]

    # Static Directory Path (React build output)
    STATIC_DIR: str = os.path.join(os.path.dirname(__file__), "dist")

settings = Settings()
