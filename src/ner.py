"""
BERT-based NER wrapper (using spaCy transformer or a HuggingFace model) — demo only.
For production, use ClinicalBERT / BioBERT or fine-tuned token classifier and implement threshold tuning.
"""
import spacy

# demo: load small en_core_web_sm for NER (not transformer-based). In production replace with transformer pipeline.
def load_spacy():
    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        # if model not present, fallback to blank
        nlp = spacy.blank("en")
    return nlp

def extract_entities(texts):
    nlp = load_spacy()
    out = []
    for txt in texts:
        doc = nlp(txt)
        ents = [{"text": e.text, "label": e.label_} for e in doc.ents]
        out.append(ents)
    return out
