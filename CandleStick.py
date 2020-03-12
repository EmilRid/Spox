import yahoo_finance as yf

class CandleStick:

    def __init__(self, candleDate, candleOpen, candleHigh, candleLow, candleClose, currentStock):
        self.candleDate = candleDate
        self.candleOpen = candleOpen
        self.candleHigh = candleHigh 
        self.candleLow = candleLow 
        self.candleClose = candleClose 
        self.currentStock = currentStock

        self.currentStock.candles.append(CandleStick)
