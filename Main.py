from CandleStick import *
from Stock import * 


apple = Stock("BTC-USD")
apple.getData("2h", "1h")
apple.engulfingCheck()