from indicators.indicator import Indicator
import plotly.graph_objects as go
import streamlit as st

class MovingAverageIndicator(Indicator):
  def __init__(self, name:str, key: str, window=20):
    self.key = key
    self.window = window
    self.name = name

  def apply(self):
    data = st.session_state.data
    data[self.key] = data['Close'].rolling(window=self.window).mean()
    st.session_state.data = data.dropna()

  def plot(self,figure):
    figure.add_trace(go.Scatter(
      x = st.session_state.data.index,
      y = st.session_state.data[self.key],
      name = self.name,
      mode="lines",
      line=dict(width=1)
      ),
      row=1,
      col=1
    )