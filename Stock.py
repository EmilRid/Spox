from CandleStick import CandleStick
import requests, json


class Stock:

    def __init__(self, symbol):
        self.candles = []
        self.symbol = symbol

    def getData(self, range, interval):
        request = requests.get(
            "https://query1.finance.yahoo.com/v8/finance/chart/{self.symbol}?range={range}&interval={interval}".format(**locals()))
        # Gathers candle info (high, low etc.) The person who made this json sucks :)
        data = request.json()['chart']['result'][0]['indicators']['quote'][0]
        print(json.dumps(data, indent=4))
        count = 0
        for candle in data["open"]:
            self.addCandle(data["open"][count], data["high"]
                           [count], data["low"][count], data["close"][count])
            count += 1

        for c in self.candles:
            if c == CandleStick:
                self.candles.remove(c)

        for candle in self.candles:
            print(candle.getData())

        # Removes last candle if it's a weird candle
        if self.candles[-1].candleOpen == self.candles[-1].candleClose and self.candles[-1].candleHigh == self.candles[-1].candleLow:
            self.candles.remove(self.candles[-1])

    def addCandle(self, candleOpen, candleHigh, candleLow, candleClose):
        self.candles.append(CandleStick(
            candleOpen, candleHigh, candleLow, candleClose, self))

    def engulfingCheck(self):
        if self.candles[-2].candleClose > self.candles[-2].candleOpen and self.candles[-1].candleClose < self.candles[-2].candleOpen:
            print("Bullish engulfing")
        elif self.candles[-2].candleOpen > self.candles[-2].candleClose and self.candles[-1].candleClose > self.candles[-2].candleOpen:
            print("Bearish engulfing")
        else:
            print("No engulfing")