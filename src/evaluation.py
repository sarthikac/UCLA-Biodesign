import numpy as np
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix

def evaluate_predictions(y_true, y_pred, labels=None):
    report = classification_report(y_true, y_pred, labels=labels, output_dict=True)
    df = pd.DataFrame(report).transpose()
    return df
