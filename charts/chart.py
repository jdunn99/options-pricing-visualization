import pandas as pd
import plotly.graph_objects as go
from abc import ABC, abstractmethod
import streamlit as st

class ChartManager:
  def __init__(self, data: pd.DataFrame, figure: go.Figure, ticker: str):
    self.data = data
    self.figure = figure 
    self.sub_charts = []
    self.ticker = ticker

  def add_subchart(self, sub_chart):
    self.sub_charts.append(sub_chart)
  
  def render(self):
    self.data = self.data.dropna()
    for sub_chart in self.sub_charts:
      for indicator in sub_chart.indicators:
        indicator.apply(self.data)
        
    self.data = self.data.dropna()
    for sub_chart in self.sub_charts:
      sub_chart.plot(self.data, self.figure)
      for indicator in sub_chart.indicators:
        indicator.plot(self.data, self.figure)
       
  def show(self):
    self.figure.update_layout(
        # xaxis3_title="Date",
        yaxis1_title="Price",
        yaxis2_title="RSI",
        yaxis3_title="Volatility",
        xaxis=dict(rangeslider=dict(visible=False), ticks="inside", showticklabels=True),
        height=800 if st.session_state.width <= 1440 else 1080,
        margin_t=20
    )
    st.plotly_chart(self.figure)
class Subchart(ABC):
  @abstractmethod
  def plot(self, data: pd.DataFrame, figure: go.Figure):
    pass  