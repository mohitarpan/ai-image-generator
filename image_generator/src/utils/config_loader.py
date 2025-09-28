# src/utils/config_loader.py
import yaml
import os

def load_agent_config(agent_name):
    config_path = os.path.join(os.path.dirname(__file__), '../../config/agents.yaml')
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config['agents'][agent_name]