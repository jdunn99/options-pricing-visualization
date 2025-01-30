import streamlit as st
import plotly.graph_objects as go
from utils.data_handler import fetch_data
from charts.chart import ChartManager
from charts.pricing_chart import PricingChart
from indicators.moving_averages import MovingAverageIndicator

def base_layout(title: str):
  st.set_page_config(layout="wide")
  st.title(title)

def sidebar(title: str, figure: go.Figure):
  with st.sidebar:
    st.title(title)
    ticker = st.text_input(label="Ticker", placeholder="Ticker")
    if ticker:
      data = fetch_data(ticker)
      manager = ChartManager(data, figure)

      pricing_chart = PricingChart()
      manager.add_subchart(pricing_chart)
      short_mva = MovingAverageIndicator(name="Short MVA", key="Short")
      long_mva = MovingAverageIndicator(name="Long MVA", key="Long", window=50)
      # manager.data = short_mva.apply(manager.data)
      # manager.data = long_mva.apply(manager.data)

      # pricing_chart.add_indicator(short_mva)
      # pricing_chart.add_indicator(long_mva)

      manager.update_data(manager.data)

      return manager