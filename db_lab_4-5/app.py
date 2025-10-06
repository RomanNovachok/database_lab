import os
from waitress import serve
from dotenv import load_dotenv
from my_project import create_app
from my_project.config import load_config

DEVELOPMENT_PORT = 5000
PRODUCTION_PORT = 8080
HOST = "0.0.0.0"

if __name__ == '__main__':
    load_dotenv()
    flask_env = os.environ.get("FLASK_ENV", "development").lower()
    debug = os.environ.get("DEBUG", "False").lower() == "true"

    config_data = load_config()

    if flask_env == "development":
        create_app(config_data).run(host="0.0.0.0", port=DEVELOPMENT_PORT, debug=debug)
    elif flask_env == "production":
        serve(create_app(config_data), host=HOST, port=PRODUCTION_PORT)
    else:
        raise ValueError("Check OS environment variable 'FLASK_ENV'")
