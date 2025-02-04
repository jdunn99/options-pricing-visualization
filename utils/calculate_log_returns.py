import pandas as pd
import numpy as np

def calculate_log_returns(data: pd.DataFrame, window=20):
  if "Log Returns" not in data.columns:
    data["Log Returns"] = np.log(data["Close"] / data["Close"].shift(1))
    data["Rolling STD"] = data["Log Returns"].rolling(window).std()