from vnstock import *
import datetime as dt
import pandas as pd
import numpy as np
from scipy.stats import norm

stock_ticker_close = 'Close'
dayOfYear = 252
alpha_95 = 0.05
alpha_99 = 0.01

def getStockMarketData(symbol , startDate, endDate):
  return stock_historical_data(symbol= symbol, start_date = startDate, end_date = endDate)

def get_stockmarket_data_realtime(symbol, startDate):
  endDate = dt.datetime.now().strftime("%Y-%m-%d")
  return stock_historical_data(symbol=symbol, start_date = startDate, end_date = endDate)

def get_stockmarket_data_attribute(startDate, attribute, list = []):
  result = {}
  for item in list :
    data = get_stockmarket_data_realtime(symbol=item, startDate = startDate)[attribute].values
    result[item]= data
  return result

def get_single_stockmarket_data_attribute(startDate, attribute, item):
  data = get_stockmarket_data_realtime(symbol=item, startDate = startDate)[attribute].values
  return data

def VaR( startDate='', alpha = 0.05, ticker =''):
  data_attribute_close = get_single_stockmarket_data_attribute(startDate, stock_ticker_close, ticker)
  df = pd.DataFrame(data_attribute_close)
  returns = df.pct_change()
  avg_rets = returns.mean()
  std_dev = returns.std()
  return norm.ppf(alpha, avg_rets, std_dev)


def VaRList(startDate = '', listTickers = [], listWeights = []):
  listWeights = np.array(listWeights)
  initial_investment = 1000000
  data_attribute_close = get_stockmarket_data_attribute(startDate, stock_ticker_close, listTickers)
  df = pd.DataFrame.from_dict(data_attribute_close)
  returns = df.pct_change()
  returns.tail()
  cov_matrix = returns.cov()

  avg_rets = returns.mean()

  port_mean = avg_rets.dot(listWeights)

  port_stdev = np.sqrt(listWeights.T.dot(cov_matrix).dot(listWeights))

  mean_investment = (1 + port_mean) * initial_investment

  stdev_investment = initial_investment * port_stdev

  conf_level1 = 0.05

  cutoff1 = norm.ppf(conf_level1, mean_investment, stdev_investment)

  return float((initial_investment - cutoff1)/initial_investment)

def Volatility(ticker = ''):
  stock = []
  stock.append(ticker)
  endDate = dt.datetime.now()
  startDate = endDate - dt.timedelta(days = 365)
  startDate = startDate.strftime("%Y-%m-%d")
  dataAttributeClose = get_stockmarket_data_attribute(str(startDate), stock_ticker_close, stock)
  df = pd.DataFrame.from_dict(dataAttributeClose)
  returns = df.pct_change()
  returns.shift(1)
  return float((returns.std()))


def getListTicker():
  listTicker = listing_companies()
  return np.array(listTicker['ticker'])



