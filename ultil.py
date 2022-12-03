from vnstock import *
import datetime as dt
import pandas as pd
import numpy as np
from scipy.stats import norm

stock_ticker_close = 'Close'
dayOfYear = 252

def getStockMarketData(symbol , startDate, endDate):
  return stock_historical_data(symbol= symbol, start_date = startDate, end_date = endDate)

def get_stockmarket_data_realtime(symbol, startDate):
  endDate = dt.datetime.now().strftime("%Y-%m-%d")
  return stock_historical_data(symbol=symbol, start_date = startDate, end_date = endDate)

def get_stockmarket_data_attribute(startDate, atribute, list = []):
  result = {}
  for item in list :
    data = get_stockmarket_data_realtime(symbol=item, startDate = startDate)[atribute].values
    result[item]= data
  return result

def VaR():
  ticker = ['VCB', 'VIC', 'VHM', 'GAS']
  weights = np.array([.25, .3, .15, .3])
  initial_investment = 1000000
  data_attribute_close = get_stockmarket_data_attribute('2022-10-2', stock_ticker_close, ticker)
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

  return (initial_investment - cutoff1)/initial_investment

# a = VaR()
# print(a)

def Volatility():
  stockList = ['VCB']
  endDate = dt.datetime.now()
  startDate = endDate - dt.timedelta(days = 365)
  startDate = startDate.strftime("%Y-%m-%d")
  dataAttributeClose = get_stockmarket_data_attribute(startDate, stock_ticker_close, stockList)
  df = pd.DataFrame(dataAttributeClose)
  returns = df.pct_change()
  returns.shift(1)
  return (returns.std()*dayOfYear**0.5)*100
a = Volatility()
print(a.values)

def getListTicker():
  listTicker = listing_companies()
  return np.array(listTicker['ticker'])

