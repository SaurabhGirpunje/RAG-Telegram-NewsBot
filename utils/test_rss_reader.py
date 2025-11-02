# test_rss_reader.py
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.rss_reader import fetch_new_articles

articles = fetch_new_articles()
for i, a in enumerate(articles, 1):
    print(f"{i}. {a['title']} — {a['link']}")
