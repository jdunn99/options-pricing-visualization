import plotly.graph_objects as pgo
from charts.chart import Chart

class CandlestickChart(Chart):
  def create_chart(self, ticker, data):
    figure = pgo.Figure()
    figure.add_trace(pgo.Candlestick(
      x = data.index, open=data["Open"], high=data["High"], low=data["Low"], close=data["Close"], name="Price",
    ))
    figure.update_layout(title=f"{ticker} Stock Analysis", xaxis_title = "Date", yaxis_title="Price", xaxis=dict(rangeslider=dict(visible=False)))
    figure.show()
