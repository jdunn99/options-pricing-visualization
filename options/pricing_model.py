from abc import ABC, abstractmethod
import pandas as pd
import plotly.graph_objects as go

class PricingModel(ABC):
  def __init__(self, expiration=30):
    self.expiration=expiration

  @abstractmethod
  def apply_model(self, S, K, T, R, sigma, option, n=None):
    pass

  @abstractmethod
  def calculate_price(self, data: pd.DataFrame):
    """Calculates the option price for the Model.
    """
    pass

  @abstractmethod
  def plot(self, data: pd.DataFrame, figure: go.Figure):
    """Models handle their own plotting logic and are applied to a Chart.
    """
    pass
