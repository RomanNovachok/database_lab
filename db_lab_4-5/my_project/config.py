# config.py
import os

def load_config():
    return {
        "SQLALCHEMY_DATABASE_URI": os.environ.get("DATABASE_URL"),
        "SECRET_KEY": os.environ.get("SECRET_KEY"),
        "DEBUG": os.environ.get("DEBUG", "False").lower() == "true",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False
    }