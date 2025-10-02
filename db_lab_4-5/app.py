import os
from waitress import serve
from dotenv import load_dotenv
from my_project import create_app

DEVELOPMENT_PORT = 5000
PRODUCTION_PORT = 8080
HOST = "0.0.0.0"

if __name__ == '__main__':
    load_dotenv()
    flask_env = os.environ.get("FLASK_ENV", "development").lower()
    debug = os.environ.get("DEBUG", "False").lower() == "true"
    config_data = {
        "SQLALCHEMY_DATABASE_URI": os.environ.get("DATABASE_URL"),
        "SECRET_KEY": os.environ.get("SECRET_KEY"),
        "DEBUG": debug,
        "SQLALCHEMY_TRACK_MODIFICATIONS": False
    }
    additional_config = {
        "MYSQL_ROOT_USER": os.environ.get("MYSQL_ROOT_USER"),
        "MYSQL_ROOT_PASSWORD": os.environ.get("MYSQL_ROOT_PASSWORD")
    }

    if flask_env == "development":
        create_app(config_data, additional_config).run(port=DEVELOPMENT_PORT, debug=debug)
    elif flask_env == "production":
        serve(create_app(config_data, additional_config), host=HOST, port=PRODUCTION_PORT)
    else:
        raise ValueError(f"Check OS environment variable 'FLASK_ENV'")