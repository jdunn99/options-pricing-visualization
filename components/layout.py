import streamlit as st
import plotly.graph_objects as go
from streamlit_js_eval import streamlit_js_eval
from utils.data_handler import fetch_data
from charts.chart import ChartManager
from charts.pricing_chart import PricingChart
from components.indicator_expander import IndicatorExpander
from components.volatility_expander import VolatilityExpander


def base_layout(title: str):
  st.set_page_config(layout="wide")
  st.markdown("""
                    <style>
                      .element-container:has(#button-after) + div button {
                        padding: 0!important;
                        font-size: 12px!important;
                        width: 90%;
                      }

                      .stHorizontalBlock div  {
                        font-size: 12px!important;
                        gap: 0;
                        flex: none;
                      }
                    </style>
                    """, unsafe_allow_html=True)
  st.title(title)

def sidebar(title: str, figure: go.Figure):
  with st.sidebar:
    st.title(title)
    ticker = st.text_input(label="Ticker", placeholder="Ticker")

    st.session_state.width = streamlit_js_eval(js_expressions='screen.width', key = 'SCR')
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