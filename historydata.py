

import requests
import re
import json
import time
import csv
import datetime


def get_stocklist():
    stocklist = []
    f = open('C:/py/stockbasic.csv', 'r', encoding='utf8')
    f.seek(0)
    reader = csv.reader(f)
    for item in reader:
        stocklist.append(item)
    f.close()
    return stocklist


def get_yesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday=today-oneday  
    yesterday=str(yesterday).replace('-','') 
    return yesterday


def get_url(fcode, ydate):
    urlstart = 'http://quotes.money.163.com/service/chddata.html?code='
    urlend = '&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;VOTURNOVER;VATURNOVER'
    url = urlstart+fcode+'&end='+ydate+urlend
    return url


if __name__ == '__main__':
    stocklist=get_stocklist()
    #ydate=get_yesterday()
    ydate = '20220211'
    for s in stocklist:
        time.sleep(1)
        code = str(s[0])
        #0：沪市；1：深市
        fcode = ("0" if code.startswith('6') else "1") + code
        url = get_url(fcode,ydate)
        filepath ='C:/py/historydata/' + code + '.csv'
        #filepath ='D:/py/' + '601398' + '.csv'
        response = requests.get(url, stream=False)
        with open(filepath, mode='wb') as f:
            f.write(response.content)
    print('all done')

