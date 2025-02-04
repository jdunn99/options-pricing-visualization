import streamlit as st
from utils.data_handler import fetch_data
from components.layout import base_layout, sidebar
from plotly.subplots import make_subplots

title = "Stock Analysis"

if __name__ == "__main__":
  if "indicators"  not in st.session_state:
    st.session_state.indicators = {}

  figure = make_subplots(
    rows=3,
    cols=1,
    vertical_spacing=0.1,
    shared_xaxes=True,
    row_heights=[0.5, 0.25, 0.25]
  )

  base_layout(title)
  manager = sidebar(title, figure)
  if manager:
    manager.show()
