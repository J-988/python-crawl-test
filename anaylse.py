#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY,date2num


# In[2]:


def get_data(code):
    names=['date','code','name','close','high','low','open','yestclose','zd','zdf','volume','turnover']
    hispath='D:/py/historydata/'+code+'.csv'
    recentpath='D:/py/stockdata/'+code+'real.csv'
    history = pd.read_csv(hispath,header=0,encoding='gbk',names=names,nrows=30) #first 30 减少数据读取时间和内存占用
    recent = pd.read_csv(recentpath,header=None,encoding='gbk',names=names)
    #history.head()
    recent=recent.iloc[::-1]  #recent用a写入新行在旧数据下，需要倒转
    #print(recent)
    df=pd.concat([recent,history])  #合并历史数据和每天定时爬的近期数据
    #df.head()
    df['date']=pd.to_datetime(df['date']) #将str日期转化为date日期
    #print(df['close'])
    df=df.set_index('date') #设置date为索引
    return df


# In[3]:


def drawstock(df):    
    df[['close','volume']].plot(secondary_y='volume',grid=True)
    plt.title('close and volume', fontsize='9')
    plt.show()


# In[4]:


def pandas_candlestick_ohlc(stock_data, otherseries=None):
    # 设置绘图参数，主要是坐标轴
    mondays = WeekdayLocator(MONDAY)
    alldays = DayLocator()
    dayFormatter = DateFormatter('%d')
 
    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.2)
    if stock_data.index[-1] - stock_data.index[0] < pd.Timedelta('730 days'):
        weekFormatter = DateFormatter('%b %d')
        ax.xaxis.set_major_locator(mondays)
        ax.xaxis.set_minor_locator(alldays)
    else:
        weekFormatter = DateFormatter('%b %d, %Y')
    ax.xaxis.set_major_formatter(weekFormatter)
    ax.grid(True)
 
    # 创建K线图
    stock_array = np.array(stock_data.reset_index()[['date','open','high','low','close']])
    stock_array[:,0] = date2num(stock_array[:,0])
    candlestick_ohlc(ax, stock_array, colorup = "red", colordown="green", width=0.6)
 
    # 可同时绘制其他折线图
    if otherseries is not None:
        for each in otherseries:
            plt.plot(stock_data[each], label=each)
        plt.legend()
 
    ax.xaxis_date()
    ax.autoscale_view()
    plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
    plt.show()


# In[5]:


def MA(df):
    df['close_mean5']=np.round(df['close'].rolling(window=5,center=False).mean(),2)
    df['close_mean20']=np.round(df['close'].rolling(window=20,center=False).mean(),2)
    pandas_candlestick_ohlc(df,['close_mean5','close_mean20'])


# In[6]:


if __name__ == '__main__':  
    code='000503' #以000503为例
    df=get_data(code)
    drawstock(df) #price and volume
    pandas_candlestick_ohlc(df) #k
    MA(df) #ma

