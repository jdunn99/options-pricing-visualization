import pandas as pd
import plotly.graph_objects as go
from abc import ABC, abstractmethod
import streamlit as st

class ChartManager:
  def __init__(self, figure: go.Figure):
    self.figure = figure
    self.subcharts = []

  def add_subchart(self, subchart):
    self.subcharts.append(subchart)

  def show(self):
    self.figure.update_layout(
        # xaxis3_title="Date",
        yaxis1_title="Price",
        yaxis2_title="RSI",
        yaxis3_title="Volatility",
        yaxis4_title="Options",
        xaxis=dict(rangeslider=dict(visible=False), ticks="inside", showticklabels=True),
        height=800 if st.session_state.width <= 1440 else 1080,
        margin_t=20
    )
    st.plotly_chart(self.figure)

  def render(self):
    active = []
    for subchart in self.subcharts:
      name = subchart.__name__
      indicators = st.session_state[name]["indicators"]
      for _, indicator in indicators.items():
        if indicator["active"]:
          active.append(indicator["ref"])
          indicator["ref"].apply()
    
    data = st.session_state.data.dropna()
    print(st.session_state.data)

    for subchart in self.subcharts:
      subchart.plot(self.figure, data)

    for a in active:
      print(a)
      a.plot(self.figure)

class Subchart(ABC):
  @abstractmethod
  def plot(self, figure: go.Figure):
    pass  