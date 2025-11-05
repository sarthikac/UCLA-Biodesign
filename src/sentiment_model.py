"""
Sentiment model wrapper.
This is a demo stub using HuggingFace transformers with a RoBERTa tokenizer + model.
Replace model_name with your fine-tuned RoBERTa model path or Hub repo that has credentialed access.
"""

from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import numpy as np
import pandas as pd

DEFAULT_MODEL = "distilroberta-base"  # demo; replace with fine-tuned checkpoint

class SentimentClassifier:
    def __init__(self, model_name: str = DEFAULT_MODEL, device: int = -1):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=3)
        # load pipeline
        self.pipe = pipeline("text-classification", model=self.model, tokenizer=self.tokenizer, return_all_scores=True, device=device)

        # mapping: label order depends on model; ensure mapping is correct if using custom model
        self.label_map = {0: "NEGATIVE", 1: "NEUTRAL", 2: "POSITIVE"}

    def predict(self, texts: list) -> pd.DataFrame:
        results = self.pipe(texts)
        # results: list per sample of dicts [{'label':..,'score':..},...]
        mapped = []
        for res in results:
            # convert to dict label->score
            d = {r['label']: r['score'] for r in res}
            # crude label selection (highest score)
            label = max(res, key=lambda r: r['score'])['label']
            score = max(res, key=lambda r: r['score'])['score']
            mapped.append({'label': label, 'score': float(score)})
        return pd.DataFrame(mapped)
