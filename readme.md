```python
卓识基金数据测评项目B

设计思路及框架：

1.东方财富网行情页获取a股股票代码和名称

2.网易接口爬取历史数据，存入csv，网易实时接口获取当天数据，存入实时数据csv。

2.部署服务器，运行一次历史数据爬取，解析后存储（历史数据csv中时间倒叙，不容易插入新值，后续实时数据建立新的实时数据csv）。
  之后每天定时设定爬取解析每日数据，存储到新的csv中，用a写入，时间正序。

3.用jupyter调取数据，整合历史和实时，进行基本分析。


stocktest.py
爬股票代码

historydata.py
爬历史数据

realtime.py
爬实时数据

anaylse.py
分析数据
```