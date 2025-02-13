import plotly.graph_objects as go
import streamlit as st
from charts.chart import Subchart

class PricingChart(Subchart):
  __name__ = "PricingChart"
  
  def __init__(self):
    st.session_state["PricingChart"]["ref"] = self

  def plot(self, figure, data):
    # indicators = st.session_state["PricingChart"]["indicators"]

    # for indicator in indicators.values():
    #   if indicator["active"]:
    #     indicator["ref"].apply()
    
    # data = st.session_state.data.dropna()  

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