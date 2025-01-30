from charts.chart import Subchart
import pandas as pd
import plotly.graph_objects as go

class PricingChart(Subchart):
  def __init__(self):
    self.indicators = []

  def plot(self, data: pd.DataFrame, figure: go.Figure):
    print(f"Plotting {data}")
    figure.add_trace(go.Candlestick(
      x=data.index,
      open=data["Open"],
      close=data["Close"],
      high=data["High"],
      low=data["Low"],
      name="Price",
      ),
      row=1,
      col=1
    )