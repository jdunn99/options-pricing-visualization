import streamlit as st
import plotly.graph_objects as go
from streamlit_js_eval import streamlit_js_eval
from utils.data_handler import fetch_data
from charts.chart import ChartManager
from charts.pricing_chart import PricingChart
# from charts.rsi_chart import RSIChart
# from charts.volatility_chart import VolatilityChart
# from components.indicator_expander import IndicatorExpander
# from components.volatility_expander import VolatilityExpander
# from options.black_scholes import BlackScholesModel
from indicators.bollinger_bands import BollingerBandsIndicator


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
                        min-width: 24px;
                      }
                    </style>
                    """, unsafe_allow_html=True)
  st.title(title)


m = {
  "Bollinger Bands": BollingerBandsIndicator
}

def temp(name):
  st.session_state.chart_state["PricingChart"]["indicators"][name] = m[name]()

def sidebar(title: str, figure: go.Figure):
  with st.sidebar:
    st.title(title)
    ticker = st.text_input(label="Ticker", placeholder="Ticker")

    st.session_state.width = streamlit_js_eval(js_expressions='screen.width', key = 'SCR')
    if ticker:

      st.session_state.chart_state["data"] = fetch_data(ticker, st.session_state.period)
      manager = ChartManager(data, figure, ticker)

      st.write(st.session_state.chart_state)
      st.checkbox("Test", on_change=temp, args=["Bollinger Bands"])
      # rsi_chart = RSIChart()
      # manager.add_subchart(pricing_chart)
      # manager.add_subchart(rsi_chart)


      # indicators = st.session_state.indicators
      # for _, cn in indicators.items():
      #   pricing_chart.add_indicator(cn)

      # pricing_chart.add_indicator(bs)
      # bs.calculate_price(data)
      # bs.plot(data, figure)

      # IndicatorExpander()
      # VolatilityExpander()
      # manager.render()

      return manager