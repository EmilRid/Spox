class CandleStick:

    def __init__(self, candleOpen, candleHigh, candleLow, candleClose, currentStock):
        self.candleOpen = candleOpen
        self.candleHigh = candleHigh 
        self.candleLow = candleLow 
        self.candleClose = candleClose 
        self.currentStock = currentStock

        self.currentStock.candles.append(CandleStick)

    def getData(self):
        return self.candleOpen, self.candleHigh, self.candleLow, self.candleClose, self.currentStock