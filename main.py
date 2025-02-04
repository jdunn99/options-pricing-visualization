import streamlit as st
from components.layout import base_layout, sidebar
from plotly.subplots import make_subplots

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
  if "indicators"  not in st.session_state:
    st.session_state.indicators = {}

  if "titles" not in st.session_state:
    st.session_state.titles = ("Candlestick", "", "")

  if "period" not in st.session_state:
    st.session_state.period = 365

  figure = make_subplots(
    rows=3,
    cols=1,
    vertical_spacing=0.1,
    shared_xaxes=True,
    subplot_titles=st.session_state.titles,
    row_heights=[0.6, 0.2, 0.2]
  )

  base_layout(title)
  manager = sidebar(title, figure)

  if manager:

    if st.session_state.period is not 1:
      today_close = manager.data["Close"].iloc[-1]
      yesterday_close = manager.data["Close"].iloc[-2]
      diff = today_close - yesterday_close
      percent_change = (abs(diff) / ((today_close + yesterday_close) / 2)) * 100

      r_diff = round(diff, 2)
      r_pc = f"({round(percent_change, 2)})%"

      n = f":red[{r_diff} {r_pc}]" if diff < 0 else f":green[+{r_diff} {r_pc}]"

      st.subheader(f"Market Summary - {manager.ticker} {n}")
    else:
      st.subheader(f"Market Summary - {manager.ticker}")

    keys = periods.keys()
    col1, _ = st.columns([1, 3])
    
    st.markdown('<span id="test"></span>', unsafe_allow_html=True)
    cols = col1.columns(len(keys))

    for i, key in enumerate(keys):
      with cols[i]:
        st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)
        st.button(key, use_container_width=True, type="primary" if st.session_state.period == periods[key] else "secondary", on_click=set_state, args=[key])

  if manager:
    manager.show()
