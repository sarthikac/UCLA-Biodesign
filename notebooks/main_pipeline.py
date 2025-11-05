# Cell 1: Imports
from src.preprocess import load_data
from src.sentiment_model import run_sentiment_analysis
from src.topic_model import run_topic_modeling
from src.ner_model import run_ner
import pandas as pd

# Cell 2: Load data
df = load_data("data/sample_survey_data.csv")

# Cell 3: Sentiment analysis
df_sent = run_sentiment_analysis(df)

# Cell 4: Topic modeling
df_topic, topic_info = run_topic_modeling(df_sent)

# Cell 5: NER
ner_results = run_ner(df_topic)

# Cell 6: Save results
df_topic.to_csv("results/sample_survey_results.csv", index=False)
print("Pipeline complete. Results saved to /results/")

