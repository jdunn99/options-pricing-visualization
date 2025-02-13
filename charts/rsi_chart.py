from charts.chart import Subchart
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

class RSIChart(Subchart):
  __name__ = "RSIChart"
  
  def __init__(self, period=14):
    self.period=period
    
  def calculate(self, data: pd.DataFrame):
    delta = data["Close"].diff()
    gain = delta.where(delta > 0, 0).rolling(window=self.period).mean()
    loss = -delta.where(delta < 0, 0).rolling(window=self.period).mean()
    rs = gain / loss

    data["RSI"] = 100 - (100 / (1 + rs))
    st.session_state.data = data.dropna()

  def plot(self, figure: go.Figure, data):

    self.calculate(data)

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

    