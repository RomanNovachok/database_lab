import os
from dotenv import load_dotenv
from my_project import create_app
from my_project.config import load_config

load_dotenv()
config_data = load_config()
app = create_app(config_data)
