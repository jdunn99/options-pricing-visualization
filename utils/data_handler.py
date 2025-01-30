import yfinance as yf
import pandas as pd

def read_csv(ticker: str):
  """Reads and parses a CSV file in chunks 

  Args:
    ticker: The stock symbol we are using as a filename.
  Returns:
    Pandas DataFrame of the parsed CSV on the given time period.
  """
  today = pd.Timestamp.now(tz="US/Eastern")
  stop = today - pd.Timedelta(days=365)
  data = []

  for chunk in pd.read_csv(f"./data/{ticker}_data.csv", chunksize=1000, parse_dates=["Date"], index_col="Date"):
    if chunk.index[0] > today:
      break

    filtered_data = chunk.loc[(chunk.index >= stop) & (chunk.index <= today)]
    data.append(filtered_data)
  
  return pd.concat(data)

def parse_to_csv(ticker: str):
  """Parses yfinance data to a CSV
  """
  history = yf.Ticker(ticker).history(period="max")
  history.to_csv(f"./data/{ticker}_data.csv")

  return read_csv(ticker)

def fetch_data(ticker: str):
  """Fetches data either by reading from CSV or requesting the Yahoo Finance API.

  CSV files hold the Max. We need to parse them accordingly to the period.

  Args:
    ticker: The stock symbol we are querying.
    period: The period which the data will be queried from.
  """
  try:
    return read_csv(ticker)
  except Exception as e:
    print(f"Could not find {ticker}_data.csv. Falling back to yfinance API. Error: {e}")
    return parse_to_csv(ticker)