import pandas as pd
import numpy as np
from scipy.signal import argrelextrema

def find_support_resistance(df: pd.DataFrame, order: int = 5) -> pd.DataFrame:
    """
    Detect support and resistance points in the given OHLC dataframe.
    Returns a DataFrame with columns: ['Index', 'Date', 'Price', 'Type']
    """
    # Get indices of local minima/maxima
    support_idx = argrelextrema(df['Low'].values, np.less_equal, order=order)[0]
    resistance_idx = argrelextrema(df['High'].values, np.greater_equal, order=order)[0]

    # Build DataFrames using those indices
    support_points = pd.DataFrame({
        'Index': support_idx,
        'Date': df.iloc[support_idx]['Date'].values,
        'Price': df.iloc[support_idx]['Low'].values,
        'Type': 'Support'
    })

    resistance_points = pd.DataFrame({
        'Index': resistance_idx,
        'Date': df.iloc[resistance_idx]['Date'].values,
        'Price': df.iloc[resistance_idx]['High'].values,
        'Type': 'Resistance'
    })

    # Combine and return
    sr_points = pd.concat([support_points, resistance_points], ignore_index=True)
    return sr_points
sr_points.to_csv("D:/BullsandBears/BullsandBears/data/processed/reliance_support_resistance.csv", index=False)

