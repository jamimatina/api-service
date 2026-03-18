# utils.py

import logging
import os
import json
import requests
from datetime import datetime
from typing import Dict, List

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler('api_service.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

def load_config() -> Dict:
    with open('config.json') as f:
        return json.load(f)

def get_env_var(var_name: str) -> str:
    return os.environ.get(var_name)

def get_api_key() -> str:
    return get_env_var('API_KEY')

def get_api_url() -> str:
    return get_env_var('API_URL')

def get_headers() -> Dict:
    return {
        'Authorization': f'Bearer {get_api_key()}',
        'Content-Type': 'application/json'
    }

def make_request(method: str, url: str, data: Dict = None) -> requests.Response:
    headers = get_headers()
    response = requests.request(method, url, headers=headers, json=data)
    response.raise_for_status()
    return response

def get_current_time() -> str:
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')