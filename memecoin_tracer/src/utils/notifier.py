import telegram
from config.api_keys import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

def send_telegram_notification(coin, data):
    """Send notification via Telegram"""
    message = (f"Safe Memecoin Alert: {coin}\n"
               f"Mentions: {data['mentions']}\nReddit Mentions: {data['reddit_mentions']}\n"
               f"Safety Score: {data['safety']}\nSentiment: {data['sentiment']}\n"
               f"Price: ${data['price']}\nVolume: ${data['volume']}")
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)