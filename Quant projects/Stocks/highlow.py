import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from scipy.signal import argrelextrema
from collections import deque
from datetime import timedelta

class HLBacktester():
    def __init__(self, symbol, start, end):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.get_data()

    def get_data(self):
        ticker = self.symbol
        yfObj = yf.Ticker(ticker)
        self.data = yfObj.history(start=self.start, end=self.end)
        self.data['local_max'] = self.data['Close'][
            (self.data['Close'].shift(1) < self.data['Close']) &
            (self.data['Close'].shift(-1) < self.data['Close'])
        ]
        self.data['local_min'] = self.data['Close'][
            (self.data['Close'].shift(1) > self.data['Close']) &
            (self.data['Close'].shift(-1) > self.data['Close'])
        ]
        return self.data

    def getHigherLows(self, data: np.array, order=5, K=2):
        """
        Finds consecutive higher lows in price pattern.
        Must not be exceeded within the number of periods indicated by the width 
        parameter for the value to be confirmed.
        K determines how many consecutive lows need to be higher.
        """
        low_idx = argrelextrema(data, np.less, order=order)[0]
        lows = data[low_idx]
        extrema = []
        ex_deque = deque(maxlen=K)
        for i, idx in enumerate(low_idx):
            if i == 0:
                ex_deque.append(idx)
                continue
            if lows[i] < lows[i-1]:
                ex_deque.clear()
            ex_deque.append(idx)
            if len(ex_deque) == K:
                extrema.append(list(ex_deque)) 
        return extrema

    def getLowerHighs(self, data: np.array, order=5, K=2):
        """
        Finds consecutive lower highs in price pattern.
        Must not be exceeded within the number of periods indicated by the width 
        parameter for the value to be confirmed.
        K determines how many consecutive highs need to be lower.
        """
        high_idx = argrelextrema(data, np.greater, order=order)[0]
        highs = data[high_idx]
        extrema = []
        ex_deque = deque(maxlen=K)
        for i, idx in enumerate(high_idx):
            if i == 0:
                ex_deque.append(idx)
                continue
            if highs[i] > highs[i-1]:
                ex_deque.clear()
            ex_deque.append(idx)
            if len(ex_deque) == K:
                extrema.append(list(ex_deque))
        return extrema

    def getHigherHighs(self, data: np.array, order=5, K=2):
        """
        Finds consecutive higher highs in price pattern.
        Must not be exceeded within the number of periods indicated by the width 
        parameter for the value to be confirmed.
        K determines how many consecutive highs need to be higher.
        """
        high_idx = argrelextrema(data, np.greater, order=order)[0]
        highs = data[high_idx]
        extrema = []
        ex_deque = deque(maxlen=K)
        for i, idx in enumerate(high_idx):
            if i == 0:
                ex_deque.append(idx)
                continue
            if highs[i] < highs[i-1]:
                ex_deque.clear()
            ex_deque.append(idx)
            if len(ex_deque) == K:
                extrema.append(list(ex_deque))
        return extrema

    def getLowerLows(self, data: np.array, order=5, K=2):
        """
        Finds consecutive lower lows in price pattern.
        Must not be exceeded within the number of periods indicated by the width 
        parameter for the value to be confirmed.
        K determines how many consecutive lows need to be lower.
        """
        low_idx = argrelextrema(data, np.less, order=order)[0]
        lows = data[low_idx]
        extrema = []
        ex_deque = deque(maxlen=K)
        for i, idx in enumerate(low_idx):
            if i == 0:
                ex_deque.append(idx)
                continue
            if lows[i] > lows[i-1]:
                ex_deque.clear()
            ex_deque.append(idx)
            if len(ex_deque) == K:
                extrema.append(list(ex_deque))
        return extrema

    def show(self):
        import matplotlib.pyplot as plt
        from matplotlib.lines import Line2D
        from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY

        colors = ['black', 'green', 'blue', 'red', 'orange'] 

        data = self.data 
        close = data['Close'].values
        dates = data.index

        order = 5
        K = 2

        hh = self.getHigherHighs(close, order, K)
        hl = self.getHigherLows(close, order, K)
        ll = self.getLowerLows(close, order, K)
        lh = self.getLowerHighs(close, order, K)

        plt.figure(figsize=(15, 8))
        plt.plot(data['Close'])
        _ = [plt.plot(dates[i], close[i], c=colors[1]) for i in hh]
        _ = [plt.plot(dates[i], close[i], c=colors[2]) for i in hl]
        _ = [plt.plot(dates[i], close[i], c=colors[3]) for i in ll]
        _ = [plt.plot(dates[i], close[i], c=colors[4]) for i in lh]

        _ = [plt.scatter(dates[i[-1]], close[i[-1]], 
                         c=colors[1], marker='^', s=100) for i in hh]
        _ = [plt.scatter(dates[i[-1]], close[i[-1]], 
                         c=colors[2], marker='^', s=100) for i in hl]
        _ = [plt.scatter(dates[i[-1]], close[i[-1]], 
                         c=colors[3], marker='v', s=100) for i in ll]
        _ = [plt.scatter(dates[i[-1]], close[i[-1]], 
                         c=colors[4], marker='v', s=100) for i in lh]

        plt.xlabel('Date')
        plt.ylabel('Price ($)')
        plt.title(f'Potential Divergence Points for {self.symbol} Closing Price')

        legend_elements = [
            Line2D([0], [0], color=colors[0], label='Close'),
            Line2D([0], [0], color=colors[1], label='Higher Highs'),
            Line2D([0], [0], color='w', 
                   marker='^', markersize=10, markerfacecolor=colors[1],
                   label='Higher High Confirmation'),
            Line2D([0], [0], color=colors[2], label='Higher Lows'),
            Line2D([0], [0], color='w', 
                   marker='^', markersize=10, markerfacecolor=colors[2],
                   label='Higher Lows Confirmation'),
            Line2D([0], [0], color=colors[3], label='Lower Lows'),
            Line2D([0], [0], color='w', 
                   marker='v', markersize=10, markerfacecolor=colors[3],
                   label='Lower Lows Confirmation'),
            Line2D([0], [0], color=colors[4], label='Lower Highs'),
            Line2D([0], [0], color='w', 
                   marker='v', markersize=10, markerfacecolor=colors[4],
                   label='Lower Highs Confirmation')
        ]

        plt.legend(handles=legend_elements)
        plt.show()
        
