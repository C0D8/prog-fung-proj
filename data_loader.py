import pandas as pd

def load_data_from_csv(file_path):
    data = pd.read_csv(file_path, index_col=0, parse_dates=True)
    return data

def get_daily_returns(data):
    return data.pct_change().dropna()