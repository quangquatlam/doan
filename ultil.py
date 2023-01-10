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

def get_stockmarket_data_attribute(startDate, endDate, attribute, list = []):
  result = {}
  for item in list :
    data = stock_historical_data(symbol=item, start_date = startDate, end_date = endDate)[attribute].values
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
  return round(df['returns'].quantile(alpha)*100,2)

def CVaRHistorical(startDate='', alpha = 0.05, ticker =''):
  data_attribute_close = get_single_stockmarket_data_attribute(startDate, stock_ticker_close, ticker)
  df = pd.DataFrame(data_attribute_close)
  df['returns'] = df.pct_change()
  df = df.dropna()
  df.sort_values('returns', inplace = True, ascending =  True)
  VaRResult = df['returns'].quantile(0.05)
  VaRSmall = df[df['returns'] < VaRResult]
  CVaR = VaRSmall['returns'].mean()
  CVaR = round(CVaR*100,2)
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

def viewChartVarDraw(stocks=[], startDate=''):
  df = pd.DataFrame()
  listdata = get_stockmarket_data_realtime(symbol=stocks[0], startDate = startDate)
  df = pd.DataFrame(index=listdata['TradingDate'], columns=stocks)
  for item in stocks :
    listdata = get_stockmarket_data_realtime(symbol=item, startDate = startDate)
    df[item] = listdata['Close'].to_list()
  df.plot()
  plt.ylabel('Close')
  plt.title('Biểu đồ biến động giá của các cổ phiếu')
  plt.show()

def VaRList(startDate = '', endDate = '', listTickers = [], listWeights = [], alpha = 0.05):
  listWeights = np.array(listWeights)
  initial_investment = 1000000
  data_attribute_close = get_stockmarket_data_attribute(startDate, endDate, stock_ticker_close, listTickers)
  df = pd.DataFrame.from_dict(data_attribute_close)
  returns = df.pct_change()
  returns = returns.tail()
  cov_matrix = returns.cov()

  avg_rets = returns.mean() #gia dong cua trung binh cua moi co phieu

  port_mean = avg_rets.dot(listWeights) #loi nhuan trung binh cua danh muc dau tu tong the

  port_stdev = np.sqrt(listWeights.T.dot(cov_matrix).dot(listWeights))

  mean_investment = (1 + port_mean) * initial_investment

  stdev_investment = initial_investment * port_stdev

  conf_level1 = alpha

  cutoff1 = norm.ppf(conf_level1, mean_investment, stdev_investment)

  var = (initial_investment - cutoff1)/initial_investment

  var = var * 100

  var = round(var,2)
  return var

def Volatility(ticker= '', startDate= '', endDate = '', day=0):
  values = getStockMarketData(ticker , startDate, endDate)['Close'].values
  df = pd.DataFrame.from_dict(values)
  returns = df.pct_change()
  returns = returns.std()
  returns = returns*np.sqrt(day)
  return float(round(returns*100,2))

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
  title = "Biểu đồ chứng khoán của mã " + ticker + " từ ngày "+ dateTimeStart + " đến " + dateTimeEnd
  fig.update_layout(title={ 'text': title, 'x': 0.5})
  fig.show()

#allVar(95)
def calculateAllHNXVar95():
  listData = pd.read_csv('data/HNX.csv')
  dic_varAll = {}
  for data in listData['Ticker'].values:
    kq = VaRHistorical('2021-10-10', 0.05, data)
    dic_varAll[data] = kq
  df = pd.DataFrame(list(dic_varAll.items()), columns=['Ticker', 'VaR95'])
  df = df.sort_values(by=['VaR95'],ascending=False)
  df = df.reset_index(drop=True)
  df.to_csv('data/VaR95_HNX.csv')

def calculateAllHSXVar95():
  listData = pd.read_csv('data/HSX.csv')
  dic_varAll = {}
  for data in listData['Ticker'].values:
    kq = VaRHistorical('2021-10-10', 0.05, data)
    dic_varAll[data] = kq
  df = pd.DataFrame(list(dic_varAll.items()), columns=['Ticker', 'VaR95'])
  df = df.sort_values(by=['VaR95'],ascending=False)
  df = df.reset_index(drop=True)
  df.to_csv('data/VaR95_HSX.csv')

#allVar(99)
def calculateAllHNXVar99():
  listData = pd.read_csv('data/HNX.csv')
  dic_varAll = {}
  for data in listData['Ticker'].values:
    kq = VaRHistorical('2021-10-10', 0.01, data)
    dic_varAll[data] = kq
  df = pd.DataFrame(list(dic_varAll.items()), columns=['Ticker', 'VaR99'])
  df = df.sort_values(by=['VaR99'],ascending=False)
  df = df.reset_index(drop=True)
  df.to_csv('data/VaR99_HNX.csv')

def calculateAllHSXVar99():
  listData = pd.read_csv('data/HSX.csv')
  dic_varAll = {}
  for data in listData['Ticker'].values:
    kq = VaRHistorical('2021-10-10', 0.01, data)
    dic_varAll[data] = kq
  df = pd.DataFrame(list(dic_varAll.items()), columns=['Ticker', 'VaR99'])
  df = df.sort_values(by=['VaR99'],ascending=False)
  df = df.reset_index(drop=True)
  df.to_csv('data/VaR99_HSX.csv')

#all CVaR(95):
def calculateAllHNXCVar95():
  listData = pd.read_csv('data/HNX.csv')
  dic_varAll = {}
  for data in listData['Ticker'].values:
    kq = CVaRHistorical('2021-10-10', 0.05, data)
    dic_varAll[data] = kq
  df = pd.DataFrame(list(dic_varAll.items()), columns=['Ticker', 'CVaR95'])
  df = df.sort_values(by=['CVaR95'],ascending=False)
  df = df.reset_index(drop=True)
  df.to_csv('data/CVaR95_HNX.csv')

def calculateAllHSXCVar95():
  listData = pd.read_csv('data/HSX.csv')
  dic_varAll = {}
  for data in listData['Ticker'].values:
    kq = CVaRHistorical('2021-10-10', 0.05, data)
    dic_varAll[data] = kq
  df = pd.DataFrame(list(dic_varAll.items()), columns=['Ticker', 'CVaR95'])
  df = df.sort_values(by=['CVaR95'],ascending=False)
  df = df.reset_index(drop=True)
  df.to_csv('data/CVaR95_HSX.csv')

def calculateAllHNXCVar99():
  listData = pd.read_csv('data/HNX.csv')
  dic_varAll = {}
  for data in listData['Ticker'].values:
    kq = CVaRHistorical('2021-10-10', 0.01, data)
    dic_varAll[data] = kq
  df = pd.DataFrame(list(dic_varAll.items()), columns=['Ticker', 'CVaR99'])
  df = df.sort_values(by=['CVaR99'],ascending=False)
  df = df.reset_index(drop=True)
  df.to_csv('data/CVaR99_HNX.csv')

def calculateAllHSXCVar99():
  listData = pd.read_csv('data/HSX.csv')
  dic_varAll = {}
  for data in listData['Ticker'].values:
    kq = CVaRHistorical('2021-10-10', 0.01, data)
    dic_varAll[data] = kq
  df = pd.DataFrame(list(dic_varAll.items()), columns=['Ticker', 'CVaR99'])
  df = df.sort_values(by=['CVaR99'],ascending=False)
  df = df.reset_index(drop=True)
  df.to_csv('data/CVaR99_HSX.csv')
# calculateAllHSXCVar99()

def calculateAllHSXVolality():
  listData = pd.read_csv('data/HSX.csv')
  dic_varAll = {}
  currentTime = dt.datetime.now().strftime("%Y-%m-%d")
  for data in listData['Ticker'].values:
    kq = Volatility(data, '2021-10-10','2022-10-10',252)
    dic_varAll[data] = kq
  df = pd.DataFrame(list(dic_varAll.items()), columns=['Ticker', 'Volality'])
  df = df.sort_values(by=['Volality'],ascending=False)
  df = df.reset_index(drop=True)
  df.to_csv('data/HSX_volality.csv')
# calculateAllHSXVolality()

def calculateAllHNXVolality():
  listData = pd.read_csv('data/HNX.csv')
  dic_varAll = {}
  currentTime = dt.datetime.now().strftime("%Y-%m-%d")
  for data in listData['Ticker'].values:
    kq = Volatility(data, '2021-10-10','2022-10-10',252)
    dic_varAll[data] = kq
  df = pd.DataFrame(list(dic_varAll.items()), columns=['Ticker', 'Volality'])
  df = df.sort_values(by=['Volality'],ascending=False)
  df = df.reset_index(drop=True)
  df.to_csv('data/HNX_volality.csv')
# calculateAllHNXVolality()

def VolatilityChar(ticker= '', startDate= '', endDate = ''):
  values = getStockMarketData(ticker , startDate, endDate)
  df = pd.DataFrame.from_dict(values)
  print(df)
  df['Volatility'] = df['Close'].pct_change()
  df = df.tail(df.shape[0] -1)
  plt.plot(df["TradingDate"],df['Volatility'])
  plt.title('Volality '+ ticker)
  plt.legend('Volatity')
  plt.show()
# VolatilityChar('ACB', '2021-01-01', '2022-02-02')