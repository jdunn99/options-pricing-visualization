import streamlit as st
from streamlit_js_eval import streamlit_js_eval
from plotly.subplots import make_subplots
from components.layout import base_layout, sidebar
import streamlit.components.v1 as components
from utils.init_state import init_state
from utils.data_handler import fetch_data
from charts.chart import ChartManager
from charts.pricing_chart import PricingChart
from charts.rsi_chart import RSIChart
from components.indicator_expander import IndicatorExpander

title = "Stock Analysis"

periods = {
  "1D": 1,
  "5D": 5,
  "1M": 29,
  "6M": 174,
  "1Y": 365,
  "5Y": 1825,
  "MAX": -1
}

def set_state(key):
  st.session_state.period = periods[key]

if __name__ == "__main__":
  base_layout(title)
  init_state()
  figure = make_subplots(
    rows=4,
    cols=1,
    vertical_spacing=0.08,
    shared_xaxes=True,
    row_heights=[0.7, 0.1, 0.1, 0.1] if not st.session_state.width or st.session_state.width <= 1400 else [0.7, 0.1, 0.1, 0.1]
  )

  st.session_state.ticker = st.text_input("ticker") 
  if st.session_state.ticker:
    st.session_state.data = fetch_data()

  st.write(st.session_state)

  if st.session_state.data is not None:
    manager = ChartManager(figure)
    manager.add_subchart(PricingChart())
    manager.add_subchart(RSIChart())
    manager.render()

    IndicatorExpander()
    manager.show()



  # st.session_state.ticker = st.text_input("ticker") 
  # if st.session_state.ticker:
  #   st.session_state.data = fetch_data()

  # st.write(st.session_state)

  # # manager = sidebar(title, figure)

  # if st.session_state.data is not None:
  #   if st.session_state.period is not 1:
  #     today_close = st.session_state.data["Close"].iloc[-1]
  #     yesterday_close = st.session_state.data["Close"].iloc[-2]
  #     diff = today_close - yesterday_close
  #     percent_change = (abs(diff) / ((today_close + yesterday_close) / 2)) * 100

  #     r_today = round(today_close, 2)
  #     r_diff = round(diff, 2)
  #     r_pc = f"({round(percent_change, 2)})%"

  #     n = f":red[{r_diff} {r_pc}]" if diff < 0 else f":green[+{r_diff} {r_pc}]"

  #     st.subheader(f"Market Summary - {st.session_state.ticker} ${r_today} {n}")
  #   else:
  #     st.subheader(f"Market Summary - {st.session_state.ticker} ${r_today}")

  #   keys = periods.keys()
  #   col1, _ = st.columns([1, 1 if st.session_state.width <= 1440 else 2])
    
  #   st.markdown('<span id="test"></span>', unsafe_allow_html=True)
  #   cols = col1.columns(len(keys))
  #   st.write(st.session_state.width)

  #   for i, key in enumerate(keys):
  #     with cols[i]:
  #       st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)
  #       st.button(key, use_container_width=True, type="primary" if st.session_state.period == periods[key] else "secondary", on_click=set_state, args=[key])


  #   test = Arkansas()
  #   test.plot()

  #   st.session_state.figure.update_layout(
  #     yaxis1_title="Price",
  #     yaxis2_title="RSI",
  #     yaxis3_title="Volatility",
  #     yaxis4_title="Options",
  #     xaxis=dict(rangeslider=dict(visible=False), ticks="inside", showticklabels=True),
  #     height=800 if st.session_state.width <= 1440 else 1080,
  #     margin_t=20
  #   )

  #   st.session_state.figure.for_each_trace(
  #     lambda trace: trace.update(visible=True) if trace.name == "Chicken" else ()
  #   )

    

  #   st.plotly_chart(st.session_state.figure)
  # # if manager:
  # #   manager.show()
