# 🤖 RAG-Telegram-NewsBot

An automated **RAG (Retrieval-Augmented Generation)** pipeline that reads the latest **RSS news feeds**, summarizes them using a **lightweight open-source LLM**, and sends concise updates directly to your **Telegram** chat — twice daily.

Built using:
- 🧩 Python (VS Code / GitHub Actions)
- 📰 RSS Feeds (NYTimes, BBC, etc.)
- 🧠 FLAN-T5 Small for Summarization
- 💬 Telegram Bot for delivery
- ⚙️ GitHub Actions Scheduler (runs twice a day)

---

## 📘 **Project Description**

This project automates news summarization using a **RAG-inspired pipeline**:

1. **RSS Reader** — Fetches the latest articles from trusted RSS feeds.
2. **Summarizer** — Uses a small open-source model (`google/flan-t5-small`) to create short, readable summaries.
3. **Vector Store (Chroma)** — Keeps track of processed summaries to avoid duplicates and enables RAG-style retrieval.
4. **Telegram Bot** — Sends daily summaries to your Telegram chat.
5. **Scheduler** — Runs automatically twice daily via GitHub Actions.

### 💡 Objective
To demonstrate an end-to-end **automated AI pipeline** integrating:
- Lightweight LLMs  
- News feed ingestion  
- Vector-based retrieval  
- Cloud automation and delivery  

---

## 🗂️ **Project Structure**
<pre>
RAG-Telegram-NewsBot/
│
├── .github/
│   └── workflows/
│       └── rss-summary.yml        # GitHub Actions scheduler
│
├── data/
│   ├── chroma/                    # Vector store for summaries (auto-created)
│   └── cache.json                 # Track processed articles
│
├── utils/
│   ├── rss_reader.py              # Fetch and clean RSS feeds
│   ├── summarizer.py              # Summarize text using FLAN-T5
│   ├── rag_store.py               # Store & retrieve article vectors
│   ├── telegram_bot.py            # Send summaries to Telegram
│   ├── test_rss_reader.py         # Local test scripts
│   └── test_telegram.py
│
├── config.py                      # Environment variable loader
├── main.py                        # Main pipeline (RSS → Summarizer → Telegram)
├── requirements.txt               # Dependencies
├── .env                           # Local environment secrets
└── .gitignore                     # Files to exclude from GitHub
</pre>
