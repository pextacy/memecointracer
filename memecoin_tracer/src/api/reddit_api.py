import praw
from config.api_keys import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT

reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID, client_secret=REDDIT_CLIENT_SECRET, user_agent=REDDIT_USER_AGENT)

def scan_reddit(coin_symbol):
    """Scan Reddit for mentions"""
    subreddit = reddit.subreddit("CryptoCurrency")
    mentions = sum(1 for submission in subreddit.search(coin_symbol, limit=100) if coin_symbol.lower() in submission.title.lower())
    return mentions