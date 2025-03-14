import requests
from backoff import on_exception, expo
from functools import lru_cache
from config.api_keys import RUGCHECK_API_KEY

@on_exception(expo, requests.exceptions.RequestException, max_tries=3)
@lru_cache(maxsize=128)
def check_rug_potential(contract_address):
    """Check rug pull risk with RugCheck API"""
    url = f"https://api.rugcheck.xyz/v1/check/{contract_address}"
    headers = {"Authorization": f"Bearer {RUGCHECK_API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json().get("is_safe", False)