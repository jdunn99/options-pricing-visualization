from charts.candlestick import CandlestickChart

class ChartFactory:
  @staticmethod
  def get_chart(type):
    if type == "candlestick":
      return CandlestickChart()
    else:
      raise ValueError(f"Unknown chart type {type}")