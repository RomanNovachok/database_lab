from dotenv import load_dotenv
import os

load_dotenv()

def load_config():
    root_user = os.environ.get("MYSQL_ROOT_USER")
    root_password = os.environ.get("MYSQL_ROOT_PASSWORD")
    db_host = os.environ.get("DB_HOST")
    db_name = os.environ.get("DB_NAME")
    jwt_secret = os.environ.get("JWT_SECRET")

    return {
        "SQLALCHEMY_DATABASE_URI": (
            f"mysql+pymysql://{root_user}:{root_password}@{db_host}/{db_name}"
        ),
        "SECRET_KEY": os.environ.get("SECRET_KEY"),
        "JWT_SECRET_KEY": jwt_secret,  # <-- ОСЬ ЦЕЙ ВАЖЛИВИЙ РЯДОК
        "DEBUG": os.environ.get("DEBUG", "False").lower() == "true",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False
    }

