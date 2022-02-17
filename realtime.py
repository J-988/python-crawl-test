#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import re
import json
import time
import random
import datetime
import csv


# In[2]:


def get_url(fcode):
    url='http://api.money.126.net/data/feed/'+fcode +'%2cmoney.api'
    return url


# In[3]:


def get_stocklist():
    stocklist = []
    file = open('C:/py/stockbasic.csv','r',encoding='utf8')
    try:
        file.seek(0)
        reader = csv.reader(file)
        for item in reader:
            stocklist.append(item)
    finally:
        file.close()
    return stocklist


# In[4]:


def get_savelist(result_list,code,name):
    today=datetime.date.today() 
    code=code 
    name=name
    Close=(result_list['price'] if 'price' in result_list.keys() else None) #闭市后爬取获取当前价格即为收盘价
    high=(result_list['high'] if 'high' in result_list.keys() else None) #防止键值不存在
    low=(result_list['low'] if 'low' in result_list.keys() else None)
    Open=(result_list['open'] if 'open' in result_list.keys() else None)
    yclose=(result_list['yestclose'] if 'yestclose' in result_list.keys() else None)
    zhangdie=((Close-yclose) if Close is not None and yclose is not None else None)
    zhangdiefu=None
    if zhangdie is not None and yclose is not None:
        if yclose != 0:
            zhangdiefu=zhangdie/yclose
    volume=(result_list['volume'] if 'volume' in result_list.keys() else None)
    turnover=(result_list['turnover'] if 'turnover' in result_list.keys() else None)
    save_list=[today,code,name,Close,high,low,Open,yclose,zhangdie,zhangdiefu,volume,turnover]
    return save_list 
    


# In[5]:


if __name__ == '__main__':      
    stocklist=get_stocklist()
    #print(stocklist)
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'}
    
    for s in stocklist:
        time.sleep(random.random())
        code = str(s[0])
        name=str(s[1])
        #code='601398'
        #name='工商银行'
        fcode =("0" if code.startswith('6') else "1") + code 
            #0：沪市；1：深市

        url=get_url(fcode)
        response=requests.get(url,headers=headers)

        content=re.findall(r'\((.*)\)', response.text)
        result_dict=json.loads(content[0])
        if result_dict: #判断今日此股有数据
            result_dict=result_dict[fcode]
            save_list=get_savelist(result_dict,code,name)
        else:
            save_list=[datetime.date.today(),code,name,None,None,None,None,None,None,None,None,None]
        filepath='C:/py/stockdata/' + code+'real' + '.csv'
        with open(filepath, mode='a',newline='') as f:
            writer=csv.writer(f)
            writer.writerow(save_list)
   
    print('all done')


# In[ ]:




