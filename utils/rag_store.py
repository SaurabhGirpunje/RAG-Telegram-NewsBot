"""
rag_store.py
-------------
Handles the storage and retrieval of summarized articles using ChromaDB.
This allows the bot to avoid re-summarizing duplicates and can later be
extended for retrieval-augmented generation (RAG) queries.
"""

import os
from chromadb.config import Settings
import chromadb

# Disable telemetry globally
os.environ["ANONYMIZED_TELEMETRY"] = "false"

# Ensure directory exists for persistent storage
os.makedirs("./data/chroma", exist_ok=True)

# Initialize persistent Chroma client (only one instance!)
client = chromadb.Client(
    Settings(
        persist_directory="./data/chroma",
        anonymized_telemetry=False
    )
)

# Create or get the persistent collection
collection = client.get_or_create_collection("news_summaries")


def add_summary_to_store(title: str, summary: str, link: str):
    """
    Adds a summarized article to the vector store.
    """
    try:
        collection.add(
            ids=[link],
            documents=[summary],
            metadatas=[{"title": title, "link": link}]
        )
    except Exception as e:
        print(f"Error adding to store: {e}")


def search_similar_articles(query: str, n_results: int = 3):
    """
    Searches for existing articles in the store similar to a given query.
    Useful for RAG-style retrieval or duplication checks.
    """
    try:
        results = collection.query(
            query_texts=[query],
            n_results=n_results
        )
        return results
    except Exception as e:
        print(f"Error querying store: {e}")
        return {}


def get_all_articles():
    """
    Retrieves all stored articles (metadata only).
    """
    try:
        items = collection.get()
        return items.get("metadatas", [])
    except Exception as e:
        print(f"Error retrieving all articles: {e}")
        return []
