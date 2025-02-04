import streamlit as st
from indicators.bollinger_bands import BollingerBandsIndicator
from indicators.rsi import RSIIndicator
from indicators.volatility import AnnualizedVolatilityIndicator, EWMAIndicator, RollingStdDevIndicator

indicators = {
  "Rolling Log STDev": RollingStdDevIndicator,
  "Annualized Volatility": AnnualizedVolatilityIndicator,
  "EWMA": EWMAIndicator,
  "RSI": RSIIndicator,
  "Bollinger Bands": BollingerBandsIndicator,
}

def set_state(indicator):
  temp = st.session_state.indicators
  titles = st.session_state.titles
  if indicator in temp:
    obj = temp[indicator] 
    del obj
    del temp[indicator]

    if indicator == "RSI":
      st.session_state.titles = ("Candlestick", "", titles[2])
    else:
      st.session_state.titles = ("Candlestick", titles[1], "")
  else:
    temp[indicator] = indicators[indicator]()
    if indicator == "RSI":
      st.session_state.titles = ("Candlestick", "RSI", titles[2])
    else:
      st.session_state.titles = ("Candlestick", titles[1], "Volatility")
  st.session_state.indicators = temp