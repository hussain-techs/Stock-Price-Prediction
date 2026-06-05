import yfinance as yf
import pandas as pd

def get_stock_data(ticker):
    print(f"Downloading data for {ticker}...")
    data = yf.download(ticker, start="2021-01-01", end="2026-01-01")

    # Fix multi-index issue
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    # Target column (next day close)
    data["Next_Close"] = data["Close"].shift(-1)

    data.dropna(inplace=True)

    return data
