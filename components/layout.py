import streamlit as st
import plotly.graph_objects as go
from utils.data_handler import fetch_data
from charts.chart import ChartManager
from charts.pricing_chart import PricingChart

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
      manager.update_data(manager.data)

      return manager