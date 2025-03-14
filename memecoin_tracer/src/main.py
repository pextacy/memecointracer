from time import sleep
from src.utils.input_handler import get_user_input
from src.core.scanner import scan_coins
from config.api_keys import SCAN_INTERVAL

if __name__ == "__main__":
    coins_to_scan, min_mentions, min_safety = get_user_input()
    if not coins_to_scan:
        print("No coins entered, program terminating.")
    else:
        while True:
            safe_memecoins = scan_coins(coins_to_scan, min_mentions, min_safety)
            if safe_memecoins:
                print("\nSafe Memecoins:")
                for coin, data in safe_memecoins.items():
                    print(f"Safe Memecoin: {coin}, Mentions: {data['mentions']}, Reddit Mentions: {data['reddit_mentions']}, "
                          f"Safety Score: {data['safety']}, Sentiment: {data['sentiment']}, Price: ${data['price']}, Volume: ${data['volume']}")
            else:
                print("No safe memecoins found.")
            sleep(SCAN_INTERVAL)