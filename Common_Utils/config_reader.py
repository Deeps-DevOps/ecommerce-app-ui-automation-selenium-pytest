import yaml
import os

class ConfigReader:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_path = os.path.join(base_dir, 'Config', 'config.yaml')
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)

    def get_url(self):
        return self.config.get('url')

    def get_username(self):
        return self.config.get('credentials', {}).get('username')

    def get_password(self):
        return self.config.get('credentials', {}).get('password')