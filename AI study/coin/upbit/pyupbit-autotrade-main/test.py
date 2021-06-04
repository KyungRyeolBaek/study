import time
import pyupbit
import datetime
import requests
import numpy as np

access = "naahaVSh29BJPu3pfBZPEWSyjsGwytkYiexmAuHR"
secret = "e0fJfTu1BjPnn35Qc2pAOheSn7xCOXIMxG0Dzluj"
myToken = "xoxb-1995417427669-2004663172180-7lt6OQoJLd2U5hbnMg8pirL9"
slack_channel = "#trade"
coin_name = "KRW-BTC"


upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-BTC 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회

tickers = pyupbit.get_tickers()

print(tickers)