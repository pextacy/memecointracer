from textblob import TextBlob

def analyze_sentiment(tweets):
    """Analyze sentiment of tweets"""
    total_polarity = 0
    for tweet in tweets:
        analysis = TextBlob(tweet.text)
        total_polarity += analysis.sentiment.polarity
    avg_polarity = total_polarity / len(tweets) if tweets else 0
    return "Positive" if avg_polarity > 0 else "Negative" if avg_polarity < 0 else "Neutral"