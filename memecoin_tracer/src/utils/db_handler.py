import sqlite3
from time import strftime, gmtime
from config.api_keys import DATABASE_PATH

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS memecoins (
                    coin TEXT, mentions INTEGER, reddit_mentions INTEGER, 
                    safety INTEGER, sentiment TEXT, price REAL, volume REAL, 
                    timestamp TEXT)''')
conn.commit()

def save_to_db(coin, data):
    """Save coin data to database"""
    timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    cursor.execute("INSERT INTO memecoins VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   (coin, data["mentions"], data["reddit_mentions"], data["safety"],
                    data["sentiment"], data["price"], data["volume"], timestamp))
    conn.commit()