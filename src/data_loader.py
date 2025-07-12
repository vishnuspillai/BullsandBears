import yfinance as yf
import pandas as pd
import os

def download_stock_data(symbol: str, period: str = "1y", interval: str = "1d", save: bool = True) -> pd.DataFrame:
    print(f"Downloading {symbol}...")
    df = yf.download(symbol, period=period, interval=interval)
    df.reset_index(inplace=True)

    if save:
        os.makedirs("data/raw", exist_ok=True)
        df.to_csv(f"data/raw/{symbol.replace('.', '_')}.csv", index=False)
        print("Saved to data/raw/")

    return df
