import yaml


def load_config(config_path: str = "config/config.yaml") -> dict:
    with open(config_path, "r") as file:
        config=yaml.safe_load(file)
    #print(config)
    return config

'''
1. Config files are data, not code

YAML files contain configuration data (settings, parameters), not Python code or functions.

import is designed to load Python modules (code files with .py) so Python can run functions, classes, etc.
'''
