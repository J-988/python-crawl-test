#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import re
import json
import time
import random
import csv
import datetime


# In[2]:


def getStockList():
    stockList = []
    f = open('C:/py/stockbasic.csv','r',encoding='utf8')
    f.seek(0)
    reader = csv.reader(f)
    for item in reader:
        stockList.append(item)
    f.close()
    return stockList


# In[3]:


def getYesterday(): #需要直接下载全部历史数据时调用这个函数
    today=datetime.date.today() 
    oneday=datetime.timedelta(days=1) 
    yesterday=today-oneday  
    yesterday=str(yesterday).replace('-','') 
    return yesterday


# In[4]:


def get_url(fcode,ydate):
    urlStart = 'http://quotes.money.163.com/service/chddata.html?code='
    urlEnd = '&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;VOTURNOVER;VATURNOVER'
    url=urlStart+fcode+'&end='+ydate+urlEnd
    return url


# In[5]:


if __name__ == '__main__':
    stockList=getStockList()
   #ydate=getYesterday()
    ydate='20220211'
    for s in stockList:
        time.sleep(random.random())
        code = str(s[0])
        #0：沪市；1：深市
        fcode=("0" if code.startswith('6') else "1") + code
        url = get_url(fcode,ydate)
        filepath ='C:/py/historydata/' + code + '.csv'
        #filepath ='D:/py/' + '601398' + '.csv'
        response = requests.get(url, stream=False)
        with open(filepath, mode='wb') as f:
            f.write(response.content)
    print('all done')

