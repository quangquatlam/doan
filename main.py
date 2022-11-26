from vnstock import *
a=listing_companies()
b=ticker_overview('VNI')
print(b)
from vnstock import *
df =  stock_historical_data(symbol='GMD', 
                            start_date="2021-01-01", 
                            end_date='2022-02-25')
print(df.head())