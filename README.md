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

1. **RSS Reader** - Fetches the latest articles from trusted RSS feeds.
2. **Summarizer** - Uses a small open-source model (`google/flan-t5-small`) to create short, readable summaries.
3. **Vector Store (Chroma)** - Keeps track of processed summaries to avoid duplicates and enables RAG-style retrieval.
4. **Telegram Bot** - Sends daily summaries to your Telegram chat.
5. **Scheduler** - Runs automatically twice daily via GitHub Actions.

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

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/RAG-Telegram-Scheduler.git
cd RAG-Telegram-Scheduler
```

### 2️⃣ Create and Activate Virtual Environment
```bash
python -m venv ragEnv
ragEnv\Scripts\activate      # For Windows
# source ragEnv/bin/activate # For macOS/Linux
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🤖 Setup Telegram Bot

### Step 1: Create a Bot

1. Open **Telegram**.
2. Search for **@BotFather**.
3. Type `/newbot` and follow the prompts.
4. Give your bot a **name** and a **username** (username must end with `_bot`).
5. Once created, you’ll receive a **bot token** like the following:
   1234567890:ABCdefGhIJKlmNoPQRstuVwxyz

⚠️ **Important:** Keep your bot token secure. Do not share or expose it publicly (e.g., in a public GitHub repository).

### Step 2: Get Your Chat ID

1. Open [Telegram Web](https://web.telegram.org)
2. Start a chat with your bot and send any message
3. In the browser URL, look for: https://web.telegram.org/k/#123456789
4. Chat ID = number part (e.g., 123456789)

---

## 🔐 Environment Variables
Create a .env file in your root directory:
```bash
BOT_TOKEN=1234567890:ABCdefGhIJKlmNoPQRstuVwxyz
CHAT_ID=123456789
```
Also, add .env to .gitignore to protect secrets.

---

## 🧪 Test Locally
Test your bot connection:
```bash
python -m utils.test_telegram
```

If successful, you’ll receive a test message in Telegram 🎉

Run the full pipeline manually:
```bash
python main.py
```

---

## 🚀 GitHub Actions: Automate RSS to Telegram

Set up your GitHub Actions workflow to automatically fetch RSS feeds, summarize them, and send updates to your Telegram bot twice a day.

---

### 🔐 Step 1: Add Secrets

1. Go to your **GitHub Repository**
2. Navigate to:  
   `Settings → Secrets and variables → Actions → New repository secret`
3. Add the following secrets:

| Name       | Value                     |
|------------|---------------------------|
| `BOT_TOKEN` | Your Telegram bot token    |
| `CHAT_ID`   | Your Telegram chat ID      |

---

### 📄 Step 2: Verify Workflow File

Path: `.github/workflows/rss-summary.yml`

```yaml
name: Daily RSS to Telegram

on:
  schedule:
    - cron: "0 3,15 * * *"    # Runs at 8:30 AM & 8:30 PM IST
  workflow_dispatch:

jobs:
  run-script:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.10"
      - run: pip install -r requirements.txt
      - env:
          BOT_TOKEN: ${{ secrets.BOT_TOKEN }}
          CHAT_ID: ${{ secrets.CHAT_ID }}
        run: python main.py
```

### ▶️ Step 3: Trigger Workflow
1. Go to the Actions tab in your repo.
2. Select the workflow: Daily RSS to Telegram
3. Click Run workflow to trigger manually OR Wait for the scheduled time.

---

## 🕒 Schedule

The workflow runs automatically at:
🕘 8:30 AM IST
🌆 8:30 PM IST

Every run:
1. Fetches the latest RSS articles
2. Summarizes them
3. Sends messages to your Telegram chat ✨























