from utils.data_handler import get_data
from charts.chart_factory import ChartFactory
import pandas as pd

if __name__ == "__main__":
  data = get_data(["VTI","VXUS", "BND"], start="2024-01-01", end="2025-01-01")
  candlestick = ChartFactory.get_chart("candlestick")

  for ticker, df in data.items():
    print(df.head)
    candlestick.create_chart(ticker, data=df)
