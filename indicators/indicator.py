import plotly.graph_objects as go
from abc import ABC, abstractmethod

class Indicator(ABC):
  @abstractmethod
  def apply(self):
    """Apply indicator logic and return the newly updated DataFrame
    """
    pass

  @abstractmethod
  def plot(self, figure: go.Figure):
    """Indicators handle their own plotting logic and are applied to a Chart.
    """
    pass