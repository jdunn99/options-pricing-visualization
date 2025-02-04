import yfinance as yf
import pandas as pd

def read_csv(ticker: str, period):
  """Reads and parses a CSV file in chunks 

  Args:
    ticker: The stock symbol we are using as a filename.
  Returns:
    Pandas DataFrame of the parsed CSV on the given time period.
  """
  today = pd.Timestamp.now(tz="US/Eastern")
  stop = today - pd.Timedelta(days=period)
  print(today, stop)
  data = []

  if period == -1:
    return pd.read_csv(f"./data/{ticker}_data.csv", parse_dates=["Date"], index_col="Date")

  for chunk in pd.read_csv(f"./data/{ticker}_data.csv", chunksize=500, parse_dates=["Date"], index_col="Date"):


    filtered_data = chunk.loc[(chunk.index >= stop) & (chunk.index <= today)]
    data.append(filtered_data)
  
  result = pd.concat(data)
  return result

def parse_to_csv(ticker: str):
  """Parses yfinance data to a CSV

  TODO: Handle errors for tickers that don't exist
  """
  print("AYO")
  history = yf.Ticker(ticker).history(period="max")
  print("HISTORY:", history)

  if history.empty:
    raise ValueError(f"Invalid ticker {ticker}")

  history.to_csv(f"./data/{ticker}_data.csv")

def fetch_data(ticker: str, period=365):
  """Fetches data either by reading from CSV or requesting the Yahoo Finance API.

  CSV files hold the Max. We need to parse them accordingly to the period.

  Args:
    ticker: The stock symbol we are querying.
    period: The period which the data will be queried from.
  """
  try:
    return read_csv(ticker, period)
  except Exception as e:
    print(f"Could not find {ticker}_data.csv. Falling back to yfinance API. Error: {e}")
    parse_to_csv(ticker)
    return read_csv(ticker, period)