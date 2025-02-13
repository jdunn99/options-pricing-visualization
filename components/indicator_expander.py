import streamlit as st
from indicators.moving_averages import MovingAverageIndicator
from components.indicator_checkbox import set_state

indicators = ["Bollinger Bands"]

def set_moving_averages_state():
  temp = st.session_state["PricingChart"]["indicators"]
  print(temp)

  if "Short MVA" in temp:
    print(temp["Short MVA"])
    temp["Short MVA"]["active"] = False
    # setattr(temp["Short MVA"][""], "active", False)
    # setattr(temp["Long MVA"], "active", False)
  else:
    temp["Short MVA"] = {
      "ref": MovingAverageIndicator(name="Short MVA", key="Short" ),
      "active": True
    }

    temp["Long MVA"] = {
      "ref": MovingAverageIndicator(name="Long MVA", key="Long", window=50),
      "active": True
    }
  
  st.session_state["PricingChart"]["indicators"] = temp

class IndicatorExpander:
  def __init__(self):
    with st.expander("Indicators", True):
      st.checkbox("Moving Averages", on_change=set_moving_averages_state)
      for indicator in indicators:
        st.checkbox(indicator, on_change=set_state, args=[indicator, "PricingChart"])