"""
main_pipeline.py
---------------
End-to-end NLP pipeline for sentiment analysis, topic modeling, and entity recognition
on anonymized hospital survey text data using RoBERTa, BERTopic, and BERT NER.

NOTE:
This version uses dummy data to demonstrate the workflow.
No real UCLA Health data is included.
"""

import pandas as pd
from transformers import pipeline
from bertopic import BERTopic

# --- Dummy survey data (replace with actual data in secure environments) ---
data = {
    "comment": [
        "The nurses were so kind and attentive.",
        "Doctor was in a rush and didn’t answer my questions.",
        "Everyone was friendly and helpful at check-in.",
        "Wait times were long but care was great overall.",
    ]
}

df = pd.DataFrame(data)

# --- Step 1: Sentiment Analysis (RoBERTa) ---
print("Running sentiment analysis...")
sentiment_model = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest")
sentiments = sentiment_model(df["comment"].tolist())
df["sentiment"] = [s["label"] for s in sentiments]
df["sentiment_score"] = [s["score"] for s in sentiments]

# --- Step 2: Topic Modeling (BERTopic) ---
print("Generating topics...")
topic_model = BERTopic(verbose=True)
topics, probs = topic_model.fit_transform(df["comment"])
df["topic"] = topics

# --- Step 3: Named Entity Recognition (BERT) ---
print("Extracting named entities...")
ner_model = pipeline("ner", grouped_entities=True)
ner_results = [ner_model(text) for text in df["comment"]]
df["entities"] = ner_results

# --- Display final output ---
print("\n--- Final Annotated Data ---")
print(df)

# --- Optionally, save results ---
df.to_csv("outputs/annotated_dummy_results.csv", index=False)
print("\nResults saved to outputs/annotated_dummy_results.csv")
