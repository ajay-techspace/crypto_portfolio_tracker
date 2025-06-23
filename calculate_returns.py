import pandas as pd
from fetch_prices import fetch_price

def calculate_returns(df):
    if 'current_price' not in df.columns or df['current_price'].isnull().any():
        df['current_price'] = df['coin'].apply(fetch_price)
    df['cost'] = df['quantity'] * df['buy_price']
    df['value'] = df['quantity'] * df['current_price']
    df['profit_loss'] = df['value'] - df['cost']
    return df