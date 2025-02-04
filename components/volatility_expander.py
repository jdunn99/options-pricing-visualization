import streamlit as st
# from components.indicator_expander import set_state
from components.indicator_checkbox import set_state

indicators = ["Rolling Log STDev", "Annualized Volatility", "EWMA"]

class VolatilityExpander:
  def __init__(self):
    with st.expander("Volatiltiy", True):
      for indicator in indicators:
        st.checkbox(indicator, on_change=set_state, args=[indicator])
