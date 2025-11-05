#!/usr/bin/env python
"""
Run the full demo pipeline on a CSV of sample surveys.
Usage:
    python scripts/run_pipeline.py --data data/dummy/sample_surveys.csv --out results/
"""

import argparse
import os
from src.utils import load_csv, save_df
from src.data_preprocessing import combine_prompt_response, filter_blank
from src.sentiment_model import SentimentClassifier
from src.topic_modeling import fit_bertopic
from src.ner import extract_entities

def main(data, outdir):
    os.makedirs(outdir, exist_ok=True)
    df = load_csv(data)
    df = combine_prompt_response(df)
    df = filter_blank(df)
    texts = df['text'].tolist()

    # Sentiment (demo)
    print("Loading sentiment model (demo)...")
    sc = SentimentClassifier()
    sres = sc.predict(texts)
    df = df.join(sres)

    # Topic modeling (demo - optional, may take time)
    try:
        print("Fitting BERTopic (demo)...")
        topic_model, topics, probs = fit_bertopic(texts, n_topics=15)
        df['topic'] = topics
    except Exception as e:
        print("BERTopic failed (demo). Skipping. Error:", e)
        df['topic'] = None

    # NER (demo)
    df['entities'] = extract_entities(texts)

    out_file = os.path.join(outdir, "pipeline_output.csv")
    save_df(df, out_file)
    print(f"Pipeline completed. Output: {out_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True)
    parser.add_argument("--out", default="results/")
    args = parser.parse_args()
    main(args.data, args.out)
