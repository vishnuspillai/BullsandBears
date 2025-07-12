import pandas as pd

# ===== Moving Averages =====
def compute_sma(df: pd.DataFrame, window: int = 14) -> pd.Series:
    return df['Close'].rolling(window=window).mean()

def compute_ema(df: pd.DataFrame, span: int = 14) -> pd.Series:
    return df['Close'].ewm(span=span, adjust=False).mean()

# ===== RSI =====
def compute_rsi(df: pd.DataFrame, window: int = 14) -> pd.Series:
    delta = df['Close'].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()

    rs = avg_gain / (avg_loss + 1e-10)  # avoid divide-by-zero
    rsi = 100 - (100 / (1 + rs))
    return rsi

# ===== MACD =====
def compute_macd(df: pd.DataFrame, short_span=12, long_span=26, signal_span=9):
    ema_short = df['Close'].ewm(span=short_span, adjust=False).mean()
    ema_long = df['Close'].ewm(span=long_span, adjust=False).mean()
    macd_line = ema_short - ema_long
    signal_line = macd_line.ewm(span=signal_span, adjust=False).mean()
    histogram = macd_line - signal_line

    return pd.DataFrame({
        'MACD_Line': macd_line,
        'Signal_Line': signal_line,
        'MACD_Hist': histogram
    })