import pandas as pd
from src.data_preprocessing import combine_prompt_response, filter_blank

def test_combine_and_filter():
    df = pd.DataFrame({
        'prompt': ['Q1', None, 'Q3'],
        'response': ['Answer1', '', None]
    })
    df2 = combine_prompt_response(df)
    df2 = filter_blank(df2)
    assert 'text' in df2.columns
    assert len(df2) == 1
