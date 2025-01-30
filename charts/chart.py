import pandas as pd
import plotly.graph_objects as go
from abc import ABC, abstractmethod
import streamlit as st

class ChartManager:
  def __init__(self, data: pd.DataFrame, figure: go.Figure):
    self.data = data
    self.figure = figure 
    self.sub_charts = []

  def add_subchart(self, sub_chart):
    self.sub_charts.append(sub_chart)
  
  def update_data(self, new_data: pd.DataFrame):
    self.data = self.data.dropna()
    for sub_chart in self.sub_charts:
      sub_chart.plot(self.data, self.figure)

  def show(self):
    self.figure.update_layout(
        xaxis_title="Date",
        showlegend=False,
        yaxis_title="Price",
        xaxis=dict(rangeslider=dict(visible=False), ticks="inside", showticklabels=True),
        height=700,
        margin_t=40
    )
    st.plotly_chart(self.figure)
class Subchart(ABC):
  @abstractmethod
  def plot(self, data: pd.DataFrame, figure: go.Figure):
    pass  