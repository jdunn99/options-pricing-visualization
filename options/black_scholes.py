import numpy as np
import pandas as pd
import plotly.graph_objects as go
from scipy.stats import norm
from options.pricing_model import PricingModel
from utils.calculate_log_returns import calculate_log_returns

class BlackScholesModel(PricingModel):

  def __init__(self, log_period=20, expiration=30):
    self.log_period = log_period
    self.expiration = expiration

  def apply_model(self, S, K, T, R, sigma, option):
    d1 = (np.log(S/K) + (R + (sigma ** 2)/2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option == "put":
      d1 = -d1
      d2 = -d2

    weighted_strike = K * np.exp(-R * T) * norm.cdf(d2)
    weighted_stock = S * norm.cdf(d1)

    return weighted_strike - weighted_stock if option == "put" else weighted_stock - weighted_strike 
  
  def calculate_price(self, data: pd.DataFrame):
    T = self.expiration / 252
    calculate_log_returns(data, self.log_period)
    data["Annualized Volatility"] = data["Rolling STD"] * np.sqrt(252)
    print(data["Close"])

    data.loc[:, "Call BS"] = data.apply(
      lambda row: self.apply_model(
        row["Close"],
        row["Close"] + 1,
        T,
        0.03,
        row["Annualized Volatility"],
        option="call"
      ),
      axis=1
    )

    data.loc[:, "Put BS"] = data.apply(
      lambda row: self.apply_model(
        row["Close"],
        row["Close"] + 1,
        T,
        0.03,
        row["Annualized Volatility"],
        option="put"
      ),
      axis=1
    )
    
  def plot(self, data: pd.DataFrame, figure: go.Figure):
    figure.add_trace(go.Scatter(
      x=data.index,
      y=data["Call BS"],
      mode="lines",
      name="Call BS",
      ),
      row=4,
      col=1
    )

    figure.add_trace(go.Scatter(
      x=data.index,
      y=data["Put BS"],
      mode="lines",
      name="Put BS",
      ),
      row=4,
      col=1
    )