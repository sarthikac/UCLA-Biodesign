from src.sentiment_model import SentimentClassifier

def test_sentiment_predict():
    sc = SentimentClassifier()
    texts = ["I loved the care.", "It was okay.", "I hated the wait."]
    df = sc.predict(texts)
    assert len(df) == 3
    assert 'label' in df.columns
    assert 'score' in df.columns
