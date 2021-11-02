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

<<<<<<< Updated upstream
# Ture가 나와야 GPU가 작동 되는 중 !
from tensorflow.python.client import device_lib 
device_lib.list_local_devices() 
tf.test.is_gpu_available()

## 개인정보 관리 주의 -----------------------------------------------##
access = "naahaVSh29BJPu3pfBZPEWSyjsGwytkYiexmAuHR"
secret = "e0fJfTu1BjPnn35Qc2pAOheSn7xCOXIMxG0Dzluj"
=======
access = "fqrmAq1mNy7tSeRYHy7ZOYXcEKqcWm9KcHCh8y6X"
secret = "LrmFrIUqve88d3yCF1W8n9KGEZ3rP0GYxb5EMjlT"
>>>>>>> Stashed changes
myToken = "xoxb-1995417427669-2004663172180-7lt6OQoJLd2U5hbnMg8pirL9"
##-------------------------------------------------------------------##

upbit = pyupbit.Upbit(access, secret)
tickers = pyupbit.get_tickers('KRW')

# 모델 학습 함수
def model_train(train_size = 10, interval_time = 'minute60', data_limit = 300):
  tickers_count = 0

  for item in tickers:
    tickers_count += 1
    df = pyupbit.get_ohlcv(item, interval=interval_time, count=data_limit)
    # orderbook = pyupbit.get_orderbook(item)
    
    X = np.array([np.array(df.close.iloc[a:a+train_size]) for a in range(len(df) - train_size)])
    Y = np.array(df.close.iloc[train_size:])

    # 훈련, 테스트 셋 분리
    X_train, X_test, y_train, y_test = train_test_split(X, Y, train_size=0.80, test_size=0.20, random_state=2)

    ## model
    # 딥러닝 구조를 결정합니다(모델을 설정하고 실행하는 부분입니다).
    globals()['{}_model'.format(item)] = Sequential([
        BatchNormalization(),
        Dense(128, activation='relu'),
        Layer.Dropout(0.2),
        Dense(256, activation='relu'),
        Layer.Dropout(0.2),
        Dense(512, activation='relu'),
        Dense(1, activation='relu') # 분류할 방법에 따라 개수를 조정해야 합니다. 
    ])

    # overfitting을 방지하기 위해서 학습 중 early stop을 수행하기 위한 코드입니다.
    early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', min_delta=0, patience=10, verbose=1)

    # 딥러닝을 실행합니다.
    globals()['{}_model'.format(item)].compile(loss='mean_squared_error', # mean_squared_error # binary_crossentropy # mean_absolute_error # poisson
                  optimizer='adam', 
                  metrics=['accuracy']) 

    print('진행도 :', tickers_count, '/', len(tickers), '| item :', item, '')
    globals()['{}_model'.format(item)].fit(X_train, y_train, validation_data=(X_test,y_test), epochs=100, batch_size=train_size, verbose=0, callbacks=[early_stop])
    
  
# 구매할 코인 리스트 작성 함수
def buy_coin_list(train_size = 10, interval_time = 'minute60', data_limit = 10):
  percent_list = dict()
  tickers_count = 0

  for item in tickers:
    tickers_count += 1
    df = pyupbit.get_ohlcv(item, interval=interval_time, count=data_limit)
    pred_X = np.array([df.close.iloc[-train_size:]])
    pred = globals()['{}_model'.format(item)].predict(pred_X)
    percent_list[item] = ((pred[0][0] - df.close.iloc[-1]) / df.close.iloc[-1]) * 100
    print('진행도 :', tickers_count, '/', len(tickers), '| item :', item, '| Price :', df.close.iloc[-1], '| Pred :', pred[0][0], '| Percent :', round(percent_list[item]), '%')

  tmp = sorted(percent_list.items(), key=lambda x: x[1], reverse=True)
  print(tmp)

  buy_list = []
  for l in tmp:
    if 100 > l[1] > 0.01:
      # print(l)
      buy_list.append(l)

  return buy_list

earning_rate = pd.DataFrame(columns=['start', 'earning_rate'])
# 시작 금액 측정
# 코인 판매.
for item in tickers:
    coin = upbit.get_balance(item)
    if coin:
        upbit.sell_market_order(item, coin)
        time.sleep(0.21)
tmp = dict()
tmp['start'] = upbit.get_balance("KRW")

while True:
  try:
    model_train()
    print(earning_rate)
    # time.sleep(3601 - datetime.datetime.now().minute * 60 - datetime.datetime.now().second)

    # 코인 판매.
    for item in tickers:
      coin = upbit.get_balance(item)
      if coin:
        upbit.sell_market_order(item, coin)
        time.sleep(0.21)

    # 수익률 갱신
    tmp['earning_rate'] = round((upbit.get_balance('KRW') - tmp['start']) / tmp['start'] , 4) * 100
    earning_rate.loc[datetime.datetime.now().hour] = tmp
    
    # 수익률 csv 파일로 저장
    earning_rate.to_csv('./earning_rate.csv')
    
    # 시작 금액 갱신
    tmp['start'] = upbit.get_balance('KRW')

<<<<<<< Updated upstream
    buy_list = buy_coin_list()
    print(buy_list)

    # 코인 구매
    n = len(buy_list)
    buy_money = round(upbit.get_balance("KRW") / n) * 0.998
    for item in buy_list:
      upbit.buy_market_order(item[0], buy_money)
      time.sleep(0.21)
  except Exception as e:
    print(e)
    time.sleep(1)
=======

# tickers = pyupbit.get_tickers(fiat = 'KRW')
# print(tickers)

df = pyupbit.get_ohlcv("KRW-BTC")
print(df)

n = len(pyupbit.get_orderbook(coin_name)['orderbook_units'])
tmp = pyupbit.get_orderbook(coin_name)['orderbook_units']
ask = [(tmp[i]['ask_size'], tmp[i]['bid_size']) for i in range(n)]
# bid = [pyupbit.get_orderbook(coin_name)['orderbook_units'][i]['bid_size'] for i in range(14)]
print('매수잔량', ask)
# print('매도잔량', bid)
# print(pyupbit.get_orderbook(coin_name)['orderbook_units'][14]['bid_size'])

>>>>>>> Stashed changes
