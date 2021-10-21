# pyupbit install
# !pip install pyupbit

# 필요 라이브러리 import
import time
import pyupbit
import datetime
import requests
import numpy as np
import pandas as pd

# 딥러닝을 구동하는 데 필요한 케라스 함수를 불러옵니다.
import keras
import tensorflow.keras.layers as Layer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, BatchNormalization, Conv2D, MaxPooling2D, Flatten

# 케라스 외의 필요한 라이브러리를 불러옵니다.
import tensorflow as tf
from sklearn.model_selection import train_test_split

# Ture가 나와야 GPU가 작동 되는 중 !
from tensorflow.python.client import device_lib 
device_lib.list_local_devices() 
tf.test.is_gpu_available()

## 개인정보 관리 주의 -----------------------------------------------##
access = "naahaVSh29BJPu3pfBZPEWSyjsGwytkYiexmAuHR"
secret = "e0fJfTu1BjPnn35Qc2pAOheSn7xCOXIMxG0Dzluj"
myToken = "xoxb-1995417427669-2004663172180-7lt6OQoJLd2U5hbnMg8pirL9"
##-------------------------------------------------------------------##

upbit = pyupbit.Upbit(access, secret)
tickers = pyupbit.get_tickers('KRW')

# 잔고가 있을 때 오르는 종목 사고, 내리면 팔고
# 30초 간격으로 확인
coin_dic = dict()
earning_rate = pd.DataFrame(data = [[0, 0, 0, 0]]*len(tickers), columns=['현재 구매액', '수익', '총 구매액', '수익률'], index=tickers)

for item in tickers:
  coin_dic[item] = pyupbit.get_current_price(item)

while True:
  buy_list = []
  print(earning_rate.sort_values(by = '수익률', axis = 0, ascending=False))
  time.sleep(60 - datetime.datetime.now().second)
  for item in tickers:
    current_price = pyupbit.get_current_price(item)
    margin = current_price - coin_dic[item]
    if margin > 0:
      coin_dic[item] = current_price
      buy_list.append(item)
    elif margin < 0:
      # 코인 판매.
      current_moeny = upbit.get_balance('KRW')
      coin = upbit.get_balance(item)
      if coin:
        upbit.sell_market_order(item, coin)
        tmp_money = upbit.get_balance('KRW')
        earning_rate['수익'][item] = tmp_moeny - current_moeny - earning_rate['현재 구매액'][item]
        earning_rate['현재 구매액'][item] = 0
        earning_rate['수익률'] = round(earning_rate['수익'] / earning_rate['총 구매액'] * 100, 2)
        # time.sleep(0.21)
        

  # 코인 구매
  if upbit.get_balance('KRW') > 1000:
     buy_money = upbit.get_balance('KRW') / len(buy_list) * 0.9994
     for item in buy_list:
       upbit.buy_market_order(item, buy_money)
       earning_rate['현재 구매액'][item] += buy_money
       earning_rate['총 구매액'][item] += buy_money
       time.sleep(0.21)