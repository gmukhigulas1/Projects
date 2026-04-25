import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class SMABacktester():
    def __init__(self,symbol,SMA_S,SMA_L,start,end):
        self.symbol=symbol
        self.SMA_S = SMA_S
        self.SMA_L = SMA_L
        self.start=start
        self.end=end
        self.results=None
        self.get_data()

    def get_data(self):
        df=yf.download(self.symbol,start=self.start,end=self.end)
        data=df.Close.copy()
        data["Returns"]=np.log(data[self.symbol].div(data[self.symbol].shift(1)))
        data['SMA_S']=data[self.symbol].rolling(self.SMA_S).mean()
        data['SMA_L']=data[self.symbol].rolling(self.SMA_L).mean()
        data.dropna(inplace=True)
        self.data2 = data

        return data

    def test_results(self):
        data = self.data2.copy().dropna()
        data['position']=np.where(data["SMA_S"]>data["SMA_L"], 1,-1)
        data["strategy"]= data['Returns']*data.position.shift(1)
        data.dropna(inplace=True)
        data["returnsB&H"]=data.Returns.cumsum().apply(np.exp)
        data["strategy_returns"]=data.strategy.cumsum().apply(np.exp)
        perf=data["strategy_returns"].iloc[-1] #last element
        outperf=perf-data["returnsB&H"].iloc[-1] #last element
        self.results = data
        
        ret=np.exp(data['strategy'].sum())
        std=data['strategy'].std()*np.sqrt(252)
    
        return perf, outperf

    def plot_results(self):
        if self.results is None:
            print("Run the test")
        else:
            title="{} | SMA_S{} | SMA_L{}".format(self.symbol, self.SMA_S, self.SMA_L)
            self.results[["returnsB&H","strategy_returns"]].plot(title = title, figsize=(12,8))
        