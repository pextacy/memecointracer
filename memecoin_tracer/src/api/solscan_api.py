import requests
from backoff import on_exception, expo
from functools import lru_cache
from config.api_keys import SOLSCAN_API_KEY

@on_exception(expo, requests.exceptions.RequestException, max_tries=3)
@lru_cache(maxsize=128)
def check_solscan_liquidity(contract_address):
    """Check liquidity status with Solscan API"""
    url = f"https://public-api.solscan.io/token/meta/{contract_address}"
    headers = {"Authorization": f"Bearer {SOLSCAN_API_KEY}"}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data.get("liquidity", {}).get("locked", False), data.get("liquidity", {}).get("amount", 0)