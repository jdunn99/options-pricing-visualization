from plotly.subplots import make_subplots
import streamlit as st

def init_state():
  if "active_charts" not in st.session_state:
    st.session_state.active_charts = []
  
  if "PricingChart" not in st.session_state:
    st.session_state["PricingChart"] = {
      "ref": None,
      "indicators": {}
    }

  if "RSIChart" not in st.session_state:
    st.session_state["RSIChart"] = {
      "ref": None,
      "indicators": {}
    }

  if "VolatilityChart" not in st.session_state:
    st.session_state["VolatilityChart"] = {
      "ref": None,
      "indicators": {}
    }

  if "OptionsChart" not in st.session_state:
    st.session_state["OptionsChart"] = {
      "ref": None,
      "models": {}
    }
  
  if "width" not in st.session_state:
    st.session_state.width = 0
    
  if "data" not in st.session_state:
    st.session_state.data = None

  if "period" not in st.session_state:
    st.session_state.period = 365

  if "ticker" not in st.session_state:
    st.session_state.ticker = ""