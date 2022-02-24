import csv
import json
import time
import re
import requests


def get_url(i):  # 实现翻页功能
    url = 'http://24.push2.eastmoney.com/api/qt/clist/get?pn=' + str(i) + '&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m%3A0+t%3A6%2Cm%3A0+t%3A80%2Cm%3A1+t%3A2%2Cm%3A1+t%3A23%2Cm%3A0+t%3A81+s%3A2048&fields=f1%2Cf2%2Cf3%2Cf4%2Cf5%2Cf6%2Cf7%2Cf8%2Cf9%2Cf10%2Cf12%2Cf13%2Cf14%2Cf15%2Cf16%2Cf17%2Cf18%2Cf20%2Cf21%2Cf23%2Cf24%2Cf25%2Cf22%2Cf11%2Cf62%2Cf128%2Cf136%2Cf115%2Cf152&_=1644666140714'
    return url


if __name__ == '__main__':
    csvfile = open('C:\py\stockbasic.csv', 'w+', encoding='utf8', newline='')
    writer = csv.writer(csvfile)
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'}
        # 前243页
        for i in range(243):
            time.sleep(1)
            url = get_url(i + 1)
            response = requests.get(url, headers=headers)
            # print(response.text)
            result = json.loads(response.text)
            result = result['data']['diff']

            for j in range(20):
                writer.writerow([result[j]['f12'], result[j]['f14']])

        # 最后一页
        url = get_url(244)
        response = requests.get(url, headers=headers)
        result = json.loads(response.text)
        result = result['data']['diff']
        for i in range(19):
            writer.writerow([result[i]['f12'], result[i]['f14']])

    finally:
        csvfile.close()
        print("success")
