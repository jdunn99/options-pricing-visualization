from indicators.indicator import Indicator
import pandas as pd
import plotly.graph_objects as go

class MovingAverageIndicator(Indicator):
  def __init__(self, name:str, key: str, window=20):
    self.key = key
    self.window = window
    self.name = name

  def apply(self, data: pd.DataFrame):
    data[self.key] = data['Close'].rolling(window=self.window).mean()

  def plot(self, data, figure):
     figure.add_trace(go.Scatter(
        x = data.index,
        y = data[self.key],
        name = self.name,
        mode="lines",
        line=dict(width=1)
        ),
        row=1,
        col=1
      )