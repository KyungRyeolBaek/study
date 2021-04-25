import time
import pyupbit
import datetime
import requests
import numpy as np

access = "naahaVSh29BJPu3pfBZPEWSyjsGwytkYiexmAuHR"
secret = "e0fJfTu1BjPnn35Qc2pAOheSn7xCOXIMxG0Dzluj"
myToken = "xoxb-1995417427669-2004663172180-Oj2xZsGX3U6tKQqc03fb0U7h"

slack_channel = "#trade"
coin = "EMC2"
coin_name = "KRW-"+ coin

def get_ror(k=0.5):
    fee = 0.05
    df = pyupbit.get_ohlcv(coin_name, count=7)
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    df['ror'] = np.where(df['high'] > df['target'],
                         df['close'] / df['target'] - fee,
                         1)

    ror = df['ror'].cumprod()[-2]
    return ror

def post_message(token, channel, text):
    """슬랙 메시지 전송"""
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_ma15(ticker):
    """15일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=15)
    ma15 = df['close'].rolling(15).mean().iloc[-1]
    return ma15

def get_balance(coin):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == coin:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print(coin +" autotrade start")
# 시작 메세지 슬랙 전송
post_message(myToken, slack_channel, coin + " autotrade start")

while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time(coin_name)
        end_time = start_time + datetime.timedelta(days=1)
        print(now)
        if start_time < now < end_time - datetime.timedelta(seconds=10):
            highk = []
            for k in np.arange(0.1, 1.0, 0.1):
                ror = get_ror(k)
                highk.append([ror, k])
            time.sleep(1)
            target_price = get_target_price(coin_name, max(highk)[1])
            ma15 = get_ma15(coin_name)
            current_price = get_current_price(coin_name)
            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order(coin_name, krw*0.9995)
                    post_message(myToken, slack_channel, coin+" buy : " +str(buy_result))

        else:
            btc = get_balance(coin)
            if btc > 0.00008:
                sell_result = upbit.sell_market_order(coin_name, btc*0.9995)
                post_message(myToken, slack_channel, coin+" sell : " +str(sell_result))
        time.sleep(1)
    except Exception as e:
        print(e)
        post_message(myToken, slack_channel, e)
        time.sleep(1)