from vnstock import *
import datetime as dt
import pandas as pd
import numpy as np
from scipy.stats import norm

def get_stockmarket_data(symbol , start_date, end_date):
  return stock_historical_data(symbol= symbol, start_date = start_date, end_date = end_date)

def get_stockmarket_data_realtime(symbol, start_date):
  end_date = dt.datetime.now().strftime("%Y-%m-%d")
  return stock_historical_data(symbol=symbol, start_date = start_date, end_date = end_date)

def get_stockmarket_data_attribute(start_date, atribute, list = []):
  result = {}
  for item in list :
    data = get_stockmarket_data_realtime(symbol=item, start_date = start_date)[atribute].values
    result[item]= data
  return result

def VaR():
  ticker = ['VCB', 'VIC', 'VHM', 'GAS']
  weights = np.array([.25, .3, .15, .3])
  initial_investment = 1000000
  data_attribute_close = get_stockmarket_data_attribute('2022-10-2','Close', ticker)
  df = pd.DataFrame(data_attribute_close)
  returns = df.pct_change()
  returns.tail()

  cov_matrix = returns.cov()

  avg_rets = returns.mean()

  port_mean = avg_rets.dot(weights)

  port_stdev = np.sqrt(weights.T.dot(cov_matrix).dot(weights))

  mean_investment = (1 + port_mean) * initial_investment

  stdev_investment = initial_investment * port_stdev

  conf_level1 = 0.05

  cutoff1 = norm.ppf(conf_level1, mean_investment, stdev_investment)

  return initial_investment - cutoff1
a = VaR()

print (a)