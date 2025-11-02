# ===============================
# config.py — Project Configuration
# ===============================

import os
from dotenv import load_dotenv
load_dotenv()  # load variables from .env into os.environ

# -------------------------------
# 🔹 TELEGRAM BOT SETTINGS
# -------------------------------
# Create your Telegram bot using @BotFather and get the token
# Then get your chat ID using @userinfobot or via the bot API

TELEGRAM_BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN_HERE")
TELEGRAM_CHAT_ID = os.getenv("CHAT_ID", "YOUR_CHAT_ID_HERE")

# -------------------------------
# 🔹 RSS FEEDS TO TRACK
# -------------------------------
# Add as many RSS feeds as you like — you can mix news, blogs, etc.

RSS_FEEDS = [
    "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
    "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en",
    "https://www.theverge.com/rss/index.xml"
]

# -------------------------------
# 🔹 SYSTEM SETTINGS
# -------------------------------
# Number of new articles to summarize each run
MAX_ARTICLES_PER_RUN = 10

# Path to vector DB and cache files
CHROMA_DB_PATH = "./data/chroma"
CACHE_FILE = "./data/cache.json"
