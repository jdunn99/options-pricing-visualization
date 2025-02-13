from charts.chart import Subchart
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
# from indicators.indicator import Indicator

class VolatilityChart(Subchart):
  def __init__(self, window=20):
    st.session_state["VolatilityChart"].ref = self
    self.window = window

  def plot(self, figure: go.Figure):
    data = st.session_state.data

    data.dropna(inplace=True)
    indicators = st.session_state["VolatilityChart"].indicators
    print(indicators)

    # figure.add_trace(go.Candlestick(
    #     x=data.index,
    #     open=data["Open"],
    #     close=data["Close"],
    #     high=data["High"],
    #     low=data["Low"],
    #   ),
    #   row=1,
    #   col=1
    # )


    return data