"""
Data preprocessing utilities:
- basic cleaning
- combine prompts + responses
- minimal anonymization (demo)
"""

import re
import pandas as pd
from typing import List

def basic_clean(text: str) -> str:
    if pd.isna(text):
        return ""
    text = str(text)
    text = text.strip()
    # basic anonymization pattern - demo only
    # Replace email-like patterns and phone-like patterns
    text = re.sub(r'\S+@\S+\.\S+', '[REDACTED_EMAIL]', text)
    text = re.sub(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b', '[REDACTED_PHONE]', text)
    return text

def combine_prompt_response(df: pd.DataFrame,
                            prompt_col: str = 'prompt',
                            response_col: str = 'response',
                            out_col: str = 'text') -> pd.DataFrame:
    df = df.copy()
    df[out_col] = df[prompt_col].fillna('') + " - " + df[response_col].fillna('')
    df[out_col] = df[out_col].apply(basic_clean)
    return df

def filter_blank(df: pd.DataFrame, text_col: str = 'text') -> pd.DataFrame:
    return df[df[text_col].str.strip().astype(bool)].reset_index(drop=True)
