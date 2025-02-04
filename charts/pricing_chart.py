from charts.chart import Subchart
import pandas as pd
import plotly.graph_objects as go
from indicators.indicator import Indicator

class PricingChart(Subchart):
  def __init__(self):
    self.indicators = []
    
  def add_indicator(self, indicator: Indicator):
    self.indicators.append(indicator)

  def plot(self, data: pd.DataFrame, figure: go.Figure):
    figure.add_trace(go.Candlestick(
      x=data.index,
      open=data["Open"],
      close=data["Close"],
      high=data["High"],
      low=data["Low"],
      ),
      row=1,
      col=1
    )
