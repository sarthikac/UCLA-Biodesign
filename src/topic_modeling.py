"""
BERTopic wrapper for topic modeling of survey comments.
This is illustrative. Adjust embeddings and parameters in production.
"""
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer

def fit_bertopic(texts, n_topics=None, embedding_model="all-MiniLM-L6-v2"):
    embedder = SentenceTransformer(embedding_model)
    embeddings = embedder.encode(texts, show_progress_bar=True)
    topic_model = BERTopic(nr_topics=n_topics)
    topics, probs = topic_model.fit_transform(texts, embeddings)
    return topic_model, topics, probs
