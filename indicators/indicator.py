from abc import ABC, abstractmethod
import pandas as pd
import plotly.graph_objects as go

class Indicator(ABC):
  @abstractmethod
  def apply(self, data: pd.DataFrame):
    """Apply indicator logic and return the newly updated DataFrame
    """
    pass

  def plot(self, data: pd.DataFrame, figure: go.Figure):
    """Indicators handle their own plotting logic and are applied to a Chart.
    """
    pass