import streamlit as st
import plotly.graph_objects as go
from utils.data_handler import fetch_data
from charts.chart import ChartManager
from charts.pricing_chart import PricingChart
from components.indicator_expander import IndicatorExpander
from components.volatility_expander import VolatilityExpander


def base_layout(title: str):
  st.set_page_config(layout="wide")
  st.title(title)

def sidebar(title: str, figure: go.Figure):
  with st.sidebar:
    st.title(title)
    ticker = st.text_input(label="Ticker", placeholder="Ticker")
    if ticker:

      data = fetch_data(ticker, st.session_state.period)
      manager = ChartManager(data, figure, ticker)

      pricing_chart = PricingChart()
      manager.add_subchart(pricing_chart)

      indicators = st.session_state.indicators
      for _, cn in indicators.items():
        pricing_chart.add_indicator(cn)

      IndicatorExpander()
      VolatilityExpander()
      manager.render()

      return manager