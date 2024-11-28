# config.py
import os
import yaml


def load_config():
    config_path = os.path.join(os.getcwd(), 'config', 'app.yml')
    with open(config_path, 'r', encoding='utf-8') as yaml_file:
        return yaml.load(yaml_file, Loader=yaml.FullLoader)
