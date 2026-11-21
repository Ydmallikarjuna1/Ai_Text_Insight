import re
from collections import Counter

import pandas as pd
import streamlit as st
from textblob import TextBlob


st.set_page_config(
    page_title="AI Text Insight Studio",
    page_icon="🧠",
    layout="wide",
)

STOPWORDS = {
    "the", "is", "are", "was", "were", "a", "an", "and", "or", "but",
    "to", "of", "in", "on", "for", "with", "this", "that", "it", "as",
    "by", "be", "at", "from", "has", "have", "had", "we", "they", "he",
    "she", "you", "i", "my", "our", "their", "will", "can", "very",
    "not", "its", "which", "who", "what",
}


def get_keywords(text: str) -> list[tuple[str, int]]:
    words = re.findall(r"\b[a-zA-Z]{3,}\b", text.lower())
    return Counter(word for word in words if word not in STOPWORDS).most_common(5)


def summarize(text: str, sentence_limit: int = 3) -> str:
    sentences = [
        sentence.strip()
        for sentence in re.split(r"(?<=[.!?])\s+", text.strip())
        if sentence.strip()
    ]
    if len(sentences) <= sentence_limit:
        return text.strip()

    word_frequencies = Counter(
        word
        for word in re.findall(r"\b[a-zA-Z]{3,}\b", text.lower())
        if word not in STOPWORDS
    )
    if not word_frequencies:
        return " ".join(sentences[:sentence_limit])

    sentence_scores = []
    for index, sentence in enumerate(sentences):
        words = re.findall(r"\b[a-zA-Z]{3,}\b", sentence.lower())
        score = sum(word_frequencies[word] for word in words if word not in STOPWORDS)
        sentence_scores.append((score, index, sentence))

    selected = sorted(
        sentence_scores,
        key=lambda item: (-item[0], item[1]),
    )[:sentence_limit]
    return " ".join(sentence for _, _, sentence in sorted(selected, key=lambda item: item[1]))


def describe_sentiment(polarity: float) -> str:
    if polarity > 0.1:
        return "Positive"
    if polarity < -0.1:
        return "Negative"
    return "Neutral"


st.title("🧠 AI Text Insight Studio")
st.write(
    "Explore the tone, key terms, and a concise extractive summary of your text."
)

text = st.text_area(
    "Enter or paste text to analyze",
    height=240,
    placeholder="Paste a paragraph or a few sentences here...",
)

if st.button("Analyze text", type="primary"):
    if not text.strip():
        st.warning("Enter some text before starting the analysis.")
    else:
        blob = TextBlob(text)
        polarity = float(blob.sentiment.polarity)
        subjectivity = float(blob.sentiment.subjectivity)

        st.subheader("Sentiment")
        sentiment_col, polarity_col, subjectivity_col = st.columns(3)
        sentiment_col.metric("Overall tone", describe_sentiment(polarity))
        polarity_col.metric("Polarity", f"{polarity:.2f}", help="Ranges from -1 (negative) to 1 (positive).")
        subjectivity_col.metric(
            "Subjectivity",
            f"{subjectivity:.2f}",
            help="Ranges from 0 (objective) to 1 (subjective).",
        )

        keywords = get_keywords(text)
        st.subheader("Top keywords")
        if keywords:
            keyword_data = pd.DataFrame(keywords, columns=["Keyword", "Occurrences"])
            st.dataframe(keyword_data, hide_index=True, width="stretch")
        else:
            st.info("No keywords found. Try a longer text with more descriptive words.")

        st.subheader("Summary")
        st.write(summarize(text))

st.caption("Sentiment and keyword results are automated estimates and may miss context or nuance.")
