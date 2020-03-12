import yahoo_finance as yf 
import datetime as dt
import pandas as pd 
import pandas_datareader.data as web 
from CandleStick import CandleStick
from Stock import Stock 

start = dt.datetime(2018, 1, 1)
end = dt.datetime(2019, 12, 31)

df = web.DataReader("BTC-USD", "yahoo", start, end)

print(start, end)
df.to_csv("df.csv")
