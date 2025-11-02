# ======================================
# main.py — Orchestrates RSS → Summary → Telegram
# ======================================

from utils.rss_reader import fetch_new_articles
from utils.summarizer import summarize_text
from utils.telegram_bot import send_telegram_message
from utils.rag_store import add_summary_to_store

def main():
    print("Starting RAG Telegram Scheduler...\n")

    # Step 1: Fetch new articles
    articles = fetch_new_articles()

    if not articles:
        print("No new articles found. Exiting.")
        return

    print(f"Found {len(articles)} new articles to process.\n")

    # Step 2: Process each article
    for idx, article in enumerate(articles, 1):
        print(f"[{idx}] Summarizing: {article['title'][:80]}...")
        summary = summarize_text(article["summary"])

        # Step 3: Format Telegram message
        message = (
            f"<b>{article['title']}</b>\n\n"
            f"{summary}\n\n"
            f"<a href='{article['link']}'>Read more</a>"
        )

        # Step 4: Send to Telegram
        send_telegram_message(message)

        # Step 5: Store summary in RAG store
        add_summary_to_store(article["title"], summary, article["link"])

    print("\nAll new articles summarized and sent to Telegram!")

if __name__ == "__main__":
    main()
