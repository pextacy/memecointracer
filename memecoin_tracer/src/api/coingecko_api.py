import requests
from backoff import on_exception, expo
from functools import lru_cache
from config.api_keys import COINGECKO_API_URL

@on_exception(expo, requests.exceptions.RequestException, max_tries=3)
@lru_cache(maxsize=128)
def get_contract_address(coin_symbol, blockchain="ethereum"):
    """Get contract address from CoinGecko"""
    coin_id = coin_symbol[1:].lower()
    url = f"{COINGECKO_API_URL}/coins/{coin_id}"
    response = requests.get(url)
    data = response.json()
    if blockchain == "solana":
        return data.get("platforms", {}).get("solana", None)
    return data.get("contract_address", None) or data.get("platforms", {}).get("ethereum", None)

@on_exception(expo, requests.exceptions.RequestException, max_tries=3)
@lru_cache(maxsize=128)
def get_price_and_volume(coin_symbol):
    """Get price and volume from CoinGecko"""
    coin_id = coin_symbol[1:].lower()
    url = f"{COINGECKO_API_URL}/coins/{coin_id}"
    response = requests.get(url)
    data = response.json()
    return data["market_data"]["current_price"]["usd"], data["market_data"]["total_volume"]["usd"]