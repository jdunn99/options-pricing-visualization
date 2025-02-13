import pandas as pd
import plotly.graph_objects as go
import numpy as np
from indicators.indicator import Indicator
from utils.calculate_log_returns import calculate_log_returns

class RollingStdDevIndicator(Indicator):
  def __init__(self, window=20):
    self.window=window
  
  def apply(self, data: pd.DataFrame):
    calculate_log_returns(data, self.window)

  def plot(self, data: pd.DataFrame, figure: go.Figure):
    figure.add_trace(go.Scatter(
      x=data.index,
      y=data["Rolling STD"],
      mode="lines",
      name="Rolling STD",
      ),
      row=3,
      col=1
    )

class AnnualizedVolatilityIndicator(Indicator):
  def __init__(self, window=20):
    self.window=window
  
  def apply(self, data: pd.DataFrame):
    calculate_log_returns(data, self.window)
    data["Annualized Volatility"] = data["Rolling STD"] * np.sqrt(252)

  def plot(self, data: pd.DataFrame, figure: go.Figure):
    figure.add_trace(go.Scatter(
      x=data.index,
      y=data["Annualized Volatility"],
      mode="lines",
      name="Annualized Volatility",
      ),
      row=3,
      col=1
    )

class EWMAIndicator(Indicator):
  def __init__(self, span=20):
    self.span = span

  def apply(self):
    calculate_log_returns(data, self.span)
    data["EWMA"] = data["Log Returns"].ewm(span=self.span).std()

  def plot(self, data:pd.DataFrame, figure: go.Figure):
    figure.add_trace(go.Scatter(
          x=data.index,
          y=data["EWMA"],
          mode="lines",
          name="EWMA",
          ),
          row=3,
          col=1
        )
    