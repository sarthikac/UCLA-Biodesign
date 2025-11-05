import os
import json
import logging
import pandas as pd

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def load_csv(path: str) -> pd.DataFrame:
    log.info(f"Loading data from {path}")
    return pd.read_csv(path)


def save_df(df: pd.DataFrame, out_path: str):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    df.to_csv(out_path, index=False)
    log.info(f"Saved dataframe to {out_path}")
