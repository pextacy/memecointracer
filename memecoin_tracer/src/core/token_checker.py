from src.api.rugcheck_api import check_rug_potential
from src.api.solscan_api import check_solscan_liquidity
from src.api.coingecko_api import get_price_and_volume

def is_token_safe(coin_symbol, contract_address):
    """Check token safety with advanced scoring"""
    if not contract_address:
        return False
    rugcheck_safe = check_rug_potential(contract_address)
    liquidity_locked, liquidity_amount = check_solscan_liquidity(contract_address)
    price, volume = get_price_and_volume(coin_symbol)
    
    safety_score = 0
    if rugcheck_safe:
        safety_score += 40
    if liquidity_locked:
        safety_score += 30
    if liquidity_amount > 10000:
        safety_score += 20
    if volume > 100000:
        safety_score += 10
    return safety_score