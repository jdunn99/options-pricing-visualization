import streamlit as st
from utils.data_handler import fetch_data
from components.layout import base_layout, sidebar
from plotly.subplots import make_subplots

title = "Stock Analysis"

if __name__ == "__main__":
  figure = make_subplots(
    rows=2,
    cols=1,
    vertical_spacing=0.1,
    shared_xaxes=True,
    row_heights=[0.75, 0.25]
  )

  base_layout(title)
  manager = sidebar(title, figure)
  if manager:
    manager.show()
