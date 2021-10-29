# pyupbit install
# !pip install pyupbit

# 필요 라이브러리 import
from functools import total_ordering
import time
import pyupbit
import datetime
import requests
import numpy as np
import pandas as pd

# # 딥러닝을 구동하는 데 필요한 케라스 함수를 불러옵니다.
# import keras
# import tensorflow.keras.layers as Layer
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, BatchNormalization, Conv2D, MaxPooling2D, Flatten

# # 케라스 외의 필요한 라이브러리를 불러옵니다.
# import tensorflow as tf
# from sklearn.model_selection import train_test_split

# # Ture가 나와야 GPU가 작동 되는 중 !
# from tensorflow.python.client import device_lib 
# device_lib.list_local_devices() 
# tf.test.is_gpu_available()

## 개인정보 관리 주의 -----------------------------------------------##
access = "naahaVSh29BJPu3pfBZPEWSyjsGwytkYiexmAuHR"
secret = "e0fJfTu1BjPnn35Qc2pAOheSn7xCOXIMxG0Dzluj"
myToken = "xoxb-1995417427669-2004663172180-7lt6OQoJLd2U5hbnMg8pirL9"
##-------------------------------------------------------------------##

upbit = pyupbit.Upbit(access, secret)
tickers = pyupbit.get_tickers('KRW')

# 거래량 급증시 매수량, 매도량 비교
# 매수량이 매도량보다 많을 시 구매
# 매도량이 매수량보다 많을 시 판매

# 코인 판매.
# for item in tickers:
#     coin = upbit.get_balance(item)
#     if coin:
#         upbit.sell_market_order(item, coin)
#         time.sleep(0.21)
#     time.sleep(0.03)

# test = tickers[0]
# print(test)
# time.sleep(61 - datetime.datetime.now().second)
# print(pyupbit.get_ohlcv(test, interval='minute1', count=3))
# print(pyupbit.get_orderbook(test)['total_ask_size'])
# print(pyupbit.get_orderbook(test)['total_bid_size'])
# print(pyupbit.get_orderbook(test))

# 수익률 저장
def save_earning_rate(df):
    earning_rate = df.sort_values(by = '수익률', axis = 0, ascending=False)
    print(earning_rate)
    # 수익률 csv 파일로 저장
    earning_rate.to_csv('./earning_rate.csv')

구매한코인가격 = dict()
수익률 = pd.DataFrame(data = [[0, 0, 0, 0]]*len(tickers), columns=['구매가격', '수익', '총구매액', '수익률'], index=tickers)

while True:
    print(구매한코인가격)
    save_earning_rate(수익률)
    time.sleep(61 - datetime.datetime.now().second)

    for item in tickers:
        거래량 = pyupbit.get_ohlcv(item, interval='minute1', count=3)['volume']
        if 거래량[0]*5 < 거래량[1]:
            매도량 = pyupbit.get_orderbook(item)['total_ask_size']
            매수량 = pyupbit.get_orderbook(item)['total_bid_size']
            현재보유액 = upbit.get_balance('KRW')
            if (매도량*5 < 매수량) and (현재보유액 > 8000):
                구매할금액 = 현재보유액 * 0.70
                upbit.buy_market_order(item, 구매할금액)
                구매한가격 = pyupbit.get_current_price(item)
                구매한코인가격[item] = 구매한가격
                수익률['구매가격'][item] = 구매한가격
                수익률['총구매액'][item] += 구매한가격
                print('종목 :', item, '거래량 :', 거래량[0], 거래량[1], '매도량 :', 매도량, '매수량 :', 매수량)
        coin = upbit.get_balance(item)
        if coin:
            매도량 = pyupbit.get_orderbook(item)['total_ask_size']
            매수량 = pyupbit.get_orderbook(item)['total_bid_size']
            현재가 = pyupbit.get_current_price(item)
            if item in 구매한코인가격:
                if 매도량 > 매수량 and 현재가 > (구매한코인가격[item]*1.0005):
                    upbit.sell_market_order(item, coin)
                    수익률['수익'][item] += 현재가 - 수익률['구매가격'][item]
                    수익률['수익률'][item] = round(수익률['수익'][item] / 수익률['총구매액'][item] * 100, 2)
                    수익률['구매가격'][item] = 0
                    print('종목 :', item, '판매가 :', 현재가)
                    del 구매한코인가격[item]
        



# coin_dic = dict()


# # 코인 판매.
# for item in tickers:
#     coin_dic[item] = pyupbit.get_current_price(item)
#     coin = upbit.get_balance(item)
#     if coin:
#         upbit.sell_market_order(item, coin)
#         time.sleep(0.21)
#     time.sleep(0.03)

# while True:
#   buy_list = []
#   time.sleep(60 - datetime.datetime.now().second)
#   for item in tickers:
#     current_price = pyupbit.get_current_price(item)
#     time.sleep(0.03)
#     margin = (current_price - coin_dic[item]) / current_price
#     if margin > 0.00:
#       coin_dic[item] = current_price
#       buy_list.append(item)
#     elif margin < -0.00:
#       # 코인 판매.
#       current_moeny = upbit.get_balance('KRW')
#       coin = upbit.get_balance(item)
#       if coin:
#         upbit.sell_market_order(item, coin)
#         tmp_money = upbit.get_balance('KRW')
#         earning_rate['수익'][item] = tmp_money - current_moeny - earning_rate['현재 구매액'][item]
#         earning_rate['현재 구매액'][item] = 0
#         earning_rate['수익률'] = round(earning_rate['수익'] / earning_rate['총 구매액'] * 100, 2)
#         save_earning_rate(earning_rate)
#         # time.sleep(0.21)
#       coin_dic[item] = current_price
#     else:
#       coin_dic[item] = current_price

#   # 코인 구매
#   if (upbit.get_balance('KRW') > 1000) and len(buy_list):
#     buy_money = upbit.get_balance('KRW') / len(buy_list) * 0.70
#     for item in buy_list:
#       upbit.buy_market_order(item, buy_money)
#       earning_rate['현재 구매액'][item] += buy_money
#       earning_rate['총 구매액'][item] += buy_money
#       time.sleep(0.21)
#     save_earning_rate(earning_rate)
