from dotenv import load_dotenv
import os

load_dotenv()

def load_config():
    root_user = os.environ.get("MYSQL_ROOT_USER")
    root_password = os.environ.get("MYSQL_ROOT_PASSWORD")

    return {
        "SQLALCHEMY_DATABASE_URI": (
            f"mysql+pymysql://{root_user}:{root_password}"
            "@database-1.cpacg4020euz.eu-north-1.rds.amazonaws.com:3306/lab_4"
        ),
        "SECRET_KEY": os.environ.get("SECRET_KEY"),
        "DEBUG": os.environ.get("DEBUG", "False").lower() == "true",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False
    }
