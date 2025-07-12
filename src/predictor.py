import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def predict_next_prices(df: pd.DataFrame, window: int = 5, forecast_days: int = 5) -> pd.DataFrame:
    """
    Predict future closing prices using linear regression on moving average trend.

    Args:
        df (pd.DataFrame): DataFrame with columns ['Date', 'Close']
        window (int): Moving average window
        forecast_days (int): How many future days to predict

    Returns:
        pd.DataFrame: DataFrame with future predicted 'Date' and 'Close'
    """
    df = df.copy()

    # Create moving average as feature
    df['MA'] = df['Close'].rolling(window=window).mean()
    df = df.dropna()

    # Create time index
    df['Index'] = np.arange(len(df))

    # Train Linear Regression
    model = LinearRegression()
    model.fit(df[['Index']], df['MA'])

    # Forecast future index points
    last_index = df['Index'].iloc[-1]
    future_indices = np.arange(last_index + 1, last_index + forecast_days + 1)

    # Predict future prices
    predicted_prices = model.predict(future_indices.reshape(-1, 1))

    # Create result DataFrame
    last_date = pd.to_datetime(df['Date'].iloc[-1])
    future_dates = [last_date + pd.Timedelta(days=i) for i in range(1, forecast_days + 1)]

    prediction_df = pd.DataFrame({
        'Date': future_dates,
        'Predicted_Close': predicted_prices
    })

    return prediction_df
