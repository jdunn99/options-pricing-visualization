import streamlit as st
from indicators.moving_averages import MovingAverageIndicator
from components.indicator_checkbox import set_state

indicators = ["RSI", "Bollinger Bands"]

def set_moving_averages_state():
  temp = st.session_state.indicators

  if "Short MVA" in temp:
    short_obj = temp["Short MVA"]
    long_obj = temp["Long MVA"]

    del short_obj
    del long_obj

    del temp["Short MVA"]
    del temp["Long MVA"]
  else:
    temp["Short MVA"] = MovingAverageIndicator(name="Short MVA", key="Short")
    temp["Long MVA"] = MovingAverageIndicator(name="Long MVA", key="Long", window=50)

class IndicatorExpander:
  def __init__(self):
    with st.expander("Indicators", True):
      st.checkbox("Moving Averages", on_change=set_moving_averages_state)
      for indicator in indicators:
        st.checkbox(indicator, on_change=set_state, args=[indicator])