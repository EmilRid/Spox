import yahoo_finance as yf 
from CandleStick import CandleStick

class Stock:

    def __init__(self, symbol):
        self.candles = []
        self.symbol = symbol

    def addCandle(self, candleDate, candleOpen, candleHigh, candleLow, candleClose):
        self.candles.append(CandleStick(candleDate, candleOpen, candleHigh, candleLow, candleClose, self))