from src.api.x_api import scan_x_for_coin
from src.api.coingecko_api import get_contract_address, get_price_and_volume
from src.api.reddit_api import scan_reddit
from src.core.token_checker import is_token_safe
from src.core.sentiment import analyze_sentiment
from src.utils.db_handler import save_to_db
from src.utils.notifier import send_telegram_notification
from src.utils.plotter import plot_trend

def scan_coins(coins, min_mentions, min_safety):
    """Scan and analyze coins"""
    safe_memecoins = {}
    for coin, blockchain in coins:
        mention_count, tweets, hourly_counts = scan_x_for_coin(coin)
        reddit_mentions = scan_reddit(coin)
        if mention_count > min_mentions:
            contract_address = get_contract_address(coin, blockchain)
            if not contract_address:
                contract_address = input(f"Enter contract address for {coin} manually (not found): ").strip()
                if not contract_address:
                    print(f"No contract address provided for {coin}, skipping.")
                    continue
            
            safety_score = is_token_safe(coin, contract_address)
            sentiment = analyze_sentiment(tweets)
            price, volume = get_price_and_volume(coin)
            if safety_score >= min_safety:
                safe_memecoins[coin] = {
                    "mentions": mention_count,
                    "reddit_mentions": reddit_mentions,
                    "safety": safety_score,
                    "sentiment": sentiment,
                    "price": price,
                    "volume": volume
                }
                save_to_db(coin, safe_memecoins[coin])
                send_telegram_notification(coin, safe_memecoins[coin])
                plot_trend(coin, hourly_counts)
            else:
                print(f"{coin} is not safe (score: {safety_score}), removed from the list.")
        else:
            print(f"{coin} does not have enough mentions ({mention_count} mentions).")
    return safe_memecoins