from indicators.indicator import Indicator
import pandas as pd
import plotly.graph_objects as go

class BollingerBandsIndicator(Indicator):
  def apply(self, data: pd.DataFrame):
    if 'Short' not in data.columns:
      data["Short"] = data["Close"].rolling(window=20).mean()
    data["STD"] = data["Close"].rolling(window=20).std()
    data["Upper Band"] = data["Short"] + (2 * data["STD"])
    data["Lower Band"] = data["Short"] - (2 * data["STD"])

  def plot(self, data: pd.DataFrame, figure: go.Figure):
    figure.add_trace(go.Scatter(
      x=data.index,
      y=data["Lower Band"],
      mode="lines",
      line=dict(color="black", width=1)
      ),
      row=1,
      col=1
    )

    figure.add_trace(go.Scatter(
        x=data.index,
        y=data["Upper Band"],
        mode="none",
        fillcolor="rgba(0, 0, 0, 0.07)",
        fill="tonexty"
        ),
        row=1,
        col=1
    )

    figure.add_trace(go.Scatter(
        x=data.index,
        y=data["Upper Band"],
        mode="lines",
        line=dict(color="black", width=1)
        ),
        row=1,
        col=1
    )