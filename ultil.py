from vnstock import *
import datetime as dt
import pandas as pd
import numpy as np
from scipy.stats import norm
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from matplotlib import pyplot as plt

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

def VaRHistorical( startDate='', alpha = 0.05, ticker =''):
  data_attribute_close = get_single_stockmarket_data_attribute(startDate, stock_ticker_close, ticker)
  df = pd.DataFrame(data_attribute_close)
  df['returns'] = df.pct_change()
  df = df.dropna()
  df.sort_values('returns', inplace = True, ascending =  True)
  return round(df['returns'].quantile(alpha),3)

def CVaRHistorical(startDate='', alpha = 0.05, ticker =''):
  data_attribute_close = get_single_stockmarket_data_attribute(startDate, stock_ticker_close, ticker)
  df = pd.DataFrame(data_attribute_close)
  df['returns'] = df.pct_change()
  df = df.dropna()
  df.sort_values('returns', inplace = True, ascending =  True)
  VaRResult = df['returns'].quantile(0.05)
  VaRSmall = df[df['returns'] < VaRResult]
  CVaR = VaRSmall['returns'].mean()
  CVaR = round(CVaR,3)
  return CVaR

def drawCharVar(startDate='', ticker =''):
  data_attribute_close = get_single_stockmarket_data_attribute(startDate, stock_ticker_close, ticker)
  df = pd.DataFrame(data_attribute_close)
  df['returns'] = df.pct_change()
  df = df.dropna()
  df.sort_values('returns', inplace = True, ascending =  True)
  VaRResult = df['returns'].quantile(0.05)
  VaRBig = df[df['returns'] > VaRResult]
  VaRSmall = df[df['returns'] <= VaRResult]
  CVaR = VaRSmall['returns'].mean()
  plt.figure(figsize = (11,7))
  plt.hist(VaRBig['returns'], bins=20)
  plt.hist(VaRSmall['returns'], bins=10)
  plt.axvline(VaRResult, color='red', linestyle='solid')
  plt.axvline(CVaR, color='red', linestyle='dashed')
  plt.xlabel('Returns')
  plt.ylabel('Frequency')
  plt.legend(['VaR for Specified Alpha as a Return',
            'CVaR for Specified Alpha as a Return',
            'Historical Returns Distribution', 
            'Returns < VaR'])
  plt.show()

def VaRList(startDate = '', listTickers = [], listWeights = [], alpha = 0.05):
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

  conf_level1 = alpha

  cutoff1 = norm.ppf(conf_level1, mean_investment, stdev_investment)

  var = (initial_investment - cutoff1)/initial_investment

  var = round(var,2)
  return var

def CVaRList(startDate = '', listTickers = [], listWeights = []):
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

  VaR = initial_investment - cutoff1/initial_investment

  return float((initial_investment - cutoff1)/initial_investment)

def Volatility(ticker = ''):
  stock = []
  stock.append(ticker)
  endDate = dt.datetime.now()
  startDate = endDate - dt.timedelta(days0 = 365)
  startDate = startDate.strftime("%Y-%m-%d")
  dataAttributeClose = get_stockmarket_data_attribute(str(startDate), stock_ticker_close, stock)
  df = pd.DataFrame.from_dict(dataAttributeClose)
  returns = df.pct_change()
  returns.shift(1)
  return float(returns.std())

def Draw(ticker='', dateTimeStart = '', dateTimeEnd = ''):
  data = getStockMarketData(ticker, dateTimeStart, dateTimeEnd)

  fig = make_subplots(specs = [[{'secondary_y': True}]])
  data['diff'] = data['Close'] - data['Open']
  data.loc[data['diff'] >= 0, 'color'] = 'green'
  data.loc[data['diff'] < 0, 'color'] = 'red'

  fig.add_trace(go.Candlestick(x = data['TradingDate'],
                                open= data['Open'],
                                high= data['High'],
                                low= data['Low'],
                                close= data['Close'], name= 'Price'))
  fig.add_trace(go.Bar(x = data['TradingDate'], y = data['Volume'], name ='Volume',marker={'color': data['color']}), secondary_y= True)
  fig.update_layout(title={ 'text': 'Đồ thị của', 'x': 0.5})
  fig.show()



