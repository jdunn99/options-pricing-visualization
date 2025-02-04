import plotly.graph_objects as go
import pandas as pd
from indicators.indicator import Indicator

class RSIIndicator(Indicator):
  def __init__(self, period=14):
    self.period = period
  
  def apply(self, data: pd.DataFrame):
    delta = data["Close"].diff()
    gain = delta.where(delta > 0, 0).rolling(window=self.period).mean()
    loss = -delta.where(delta < 0, 0).rolling(window=self.period).mean()
    rs = gain / loss

    data["RSI"] = 100 - (100 / (1 + rs))
   
  def plot(self, data: pd.DataFrame, figure: go.Figure):
    figure.add_trace(go.Scatter(
          x=data.index,
          y=[70] * len(data),
          name="Overbought",
          line=dict(dash="dash", color="red")
          ),
          row=2,
          col=1
      )

    figure.add_trace(go.Scatter(
        x=data.index,
        y=[30] * len(data),
        name="Oversold",
        line=dict(dash="dash", color="green", width=1)
        ),
        row=2,
        col=1
    )

    figure.add_trace(go.Scatter(
        x=data.index,
        y=data["RSI"],
        mode="lines",
        name="RSI",
        line=dict(color="aqua"),
        ),
        row=2,
        col=1
    )
    