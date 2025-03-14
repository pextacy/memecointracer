import tweepy
from config.api_keys import X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(X_API_KEY, X_API_SECRET)
auth.set_access_token(X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def scan_x_for_coin(coin):
    """Scan X for mentions and return count, tweets, and hourly trend"""
    query = f"{coin} -filter:retweets"
    try:
        tweets = api.search_tweets(q=query, count=100, lang="en")
        hourly_counts = [0] * 24
        for tweet in tweets:
            hour = tweet.created_at.hour
            hourly_counts[hour] += 1
        return len(tweets), tweets, hourly_counts
    except Exception as e:
        print(f"X scan error for {coin}: {e}")
        return 0, [], [0] * 24