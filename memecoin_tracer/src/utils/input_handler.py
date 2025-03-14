def get_user_input():
    """Get memecoin symbols and filters from user"""
    print("Enter memecoin symbols to scan (e.g., $DOGE $SHIB). Type 'done' to finish.")
    coins = []
    while True:
        coin = input("Coin symbol: ").strip()
        if coin.lower() == "done":
            break
        if coin.startswith("$"):
            blockchain = input(f"Blockchain for {coin} (ethereum/solana, default ethereum): ").strip() or "ethereum"
            coins.append((coin, blockchain))
        else:
            print("Please enter a symbol starting with $ (e.g., $DOGE).")
    min_mentions = int(input("Minimum mention count (default 10): ") or 10)
    min_safety = int(input("Minimum safety score (default 70): ") or 70)
    return coins, min_mentions, min_safety