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
  if indicator in temp:
    obj = temp[indicator] 
    del obj
    del temp[indicator]
  else:
    temp[indicator] = indicators[indicator]()
  st.session_state.indicators = temp
