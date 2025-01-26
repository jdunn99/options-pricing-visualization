import yfinance as yf
import pandas as pd

def fetch_to_csv(ticker, start, end):
  df = yf.download(ticker, start, end)
  df.to_csv(f"./data/{ticker}_data.csv")

  # I am re-reading from the CSV because yfinance DataFrame has a mismatch so I am avoiding too many manipulations for simpliciy.
  return pd.read_csv(f"./data/{ticker}_data.csv", index_col=0, parse_dates=True)


def fetch_data(ticker, start, end):
  """Fetches data either by reading from CSV or fetching with yfinance
  """
  try:
    return pd.read_csv(f"./data/{ticker}_data.csv", index_col=0, parse_dates=True)
  except Exception as e:
    print(f"Error: {e}")
    return fetch_to_csv(ticker, start, end)

def get_data(tickers, start, end):
  data = {}
  for ticker in tickers:
    data[ticker] = fetch_data(ticker, start, end)
  return data