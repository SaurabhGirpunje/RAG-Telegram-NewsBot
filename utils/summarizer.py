# ==========================================
# summarizer.py — Summarize article text using FLAN-T5
# ==========================================

from transformers import pipeline

# Load once globally (so it doesn't reload for every article)
# model = google/flan-t5-small → lightweight, works fine on CPU
summarizer = pipeline("summarization", model="google/flan-t5-small")

def summarize_text(text: str, max_words: int = 60) -> str:
    """
    Generate a concise summary of the input text.
    """
    if not text.strip():
        return "No content to summarize."

    # The model works best with < 512 tokens
    max_input_length = 1000
    text = text[:max_input_length]

    try:
        result = summarizer(
            text,
            max_length=max_words,
            min_length=25,
            do_sample=False
        )
        return result[0]["summary_text"].strip()
    except Exception as e:
        print(f"Summarization error: {e}")
        return text[:200] + "..."
