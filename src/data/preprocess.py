# Lifecycle stage 4 — Data Preparation (sentiment labels)

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import re
import spacy

# Ensure VADER lexicon is available
try:
    nltk.data.find("sentiment/vader_lexicon.zip")
except LookupError:
    nltk.download("vader_lexicon")

# Load sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Load spaCy model ONCE
nlp = spacy.load("en_core_web_sm")

# Negation words carry sentiment, so we never drop them
KEEP = {"not", "no", "never", "nor", "none", "nt"}


# ---------------- SENTIMENT LABEL FUNCTION ---------------- #

def create_sentiment(text):
    score = analyzer.polarity_scores(str(text))["compound"]

    if score >= 0.05:
        return "positive"
    elif score <= -0.05:
        return "negative"
    else:
        return "neutral"


# ---------------- TEXT CLEANING FUNCTION ---------------- #

def clean_text(text):
    text = str(text).lower()

    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"[^a-zA-Z ]", "", text)

    doc = nlp(text)

    words = [
        token.lemma_
        for token in doc
        if token.lemma_ in KEEP or not token.is_stop
    ]

    return " ".join(words)


# ---------------- BATCH CLEANING FUNCTION ---------------- #

def clean_batch(texts):

    cleaned = []

    docs = nlp.pipe(
        texts,
        disable=["parser", "ner"],
        batch_size=200
    )

    for doc in docs:
        words = [
            t.lemma_
            for t in doc
            if t.lemma_ in KEEP or not t.is_stop
        ]
        cleaned.append(" ".join(words))

    return cleaned
