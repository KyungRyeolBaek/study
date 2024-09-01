import pandas as pd
import numpy as np
import yfinance as yf
from pykrx import stock
from datetime import datetime, timedelta

def get_stock_data(ticker, interval, start_date, end_date):
    # 주식 데이터 불러오기 (1분 단위 데이터)
    df = yf.download(ticker, start=start_date, end=end_date, interval=interval)
    return df

def apply_moving_average_strategy(df, short_window, long_window):
    # 이동 평균 계산
    df['Short_MA'] = df['Close'].rolling(window=short_window).mean()
    df['Long_MA'] = df['Close'].rolling(window=long_window).mean()

    # 매수/매도 신호 생성
    df['Signal'] = 0
    df.loc[df.index[short_window:], 'Signal'] = np.where(df['Short_MA'][short_window:] > df['Long_MA'][short_window:], 1, 0)
    df['Position'] = df['Signal'].diff()

    return df

def apply_other_strategy(df, window):
    # 단순 이동 평균 전략 예시
    df['MA'] = df['Close'].rolling(window=window).mean()

    # 매수/매도 신호 생성
    df['Signal'] = 0
    df.loc[df.index[window:], 'Signal'] = np.where(df['Close'][window:] > df['MA'][window:], 1, 0)
    df['Position'] = df['Signal'].diff()

    return df

def buy_shares(capital, close_price):
    # 원금의 1%만 사용하여 주식을 매수하는 함수
    purchase_amount = capital * 1  # 원금의 1%
    shares_to_buy = purchase_amount // close_price
    new_capital = capital - shares_to_buy * close_price
    return shares_to_buy, new_capital

def backtest_strategy(df, strategy_func, *args):
    # 초기 자본 설정
    initial_capital = float(1000000.0)
    shares = 0
    capital = initial_capital

    # 전략 적용
    df = strategy_func(df, *args)

    # 거래 내역 저장
    trades = []

    for i in range(len(df)):
        if df['Position'].iloc[i] == 1:  # 매수 신호
            shares_to_buy, capital = buy_shares(capital, df['Close'].iloc[i])
            shares += shares_to_buy
            trades.append(('Buy', df.index[i], df['Close'].iloc[i], shares_to_buy, capital))
        elif df['Position'].iloc[i] == -1 and shares > 0:  # 매도 신호
            capital += shares * df['Close'].iloc[i]
            trades.append(('Sell', df.index[i], df['Close'].iloc[i], shares, capital))
            shares = 0

    # 최종 자본 계산
    final_capital = capital + shares * df['Close'].iloc[-1]
    total_profit = final_capital - initial_capital
    return_rate = (final_capital - initial_capital) / initial_capital * 100

    return final_capital, trades, total_profit, return_rate

if __name__ == "__main__":
    # 주식 티커, 기간 설정 (최근 30일 내)
    ticker = "AAPL"  # Apple Inc.
    interval = "1m"  # 1분 단위 데이터

    # 현재 날짜를 기준으로 최근 7일 범위 설정
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    
    # 데이터 불러오기
    df = get_stock_data(ticker, interval, start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"))

    if df.empty:
        print("No data fetched for the given date range. Please check the ticker symbol and date range.")
    else:
        # 이동 평균 교차 전략 적용
        short_window = 40
        long_window = 100
        final_capital, trades, total_profit, return_rate = backtest_strategy(df, apply_moving_average_strategy, short_window, long_window)

        print(f"Initial Capital: 1000000.0")
        print(f"Final Capital: {final_capital}")
        print(f"Total Profit: {total_profit}")
        print(f"Return Rate: {return_rate}%")
        print("Trades (Moving Average Strategy):")
        # for trade in trades:
        #     if trade[0] == 'Buy':
        #         print(f"{trade[0]}: Date: {trade[1]}, Price: {trade[2]}, Shares: {trade[3]}, Remaining Capital: {trade[4]}")
        #     elif trade[0] == 'Sell':
        #         print(f"{trade[0]}: Date: {trade[1]}, Price: {trade[2]}, Shares: {trade[3]}, Remaining Capital: {trade[4]}")

        # 다른 전략 적용 (예시)
        window = 50
        final_capital, trades, total_profit, return_rate = backtest_strategy(df, apply_other_strategy, window)

        print(f"Initial Capital: 1000000.0")
        print(f"Final Capital: {final_capital}")
        print(f"Total Profit: {total_profit}")
        print(f"Return Rate: {return_rate}%")
        print("Trades (Other Strategy):")
        # for trade in trades:
        #     if trade[0] == 'Buy':
        #         print(f"{trade[0]}: Date: {trade[1]}, Price: {trade[2]}, Shares: {trade[3]}, Remaining Capital: {trade[4]}")
        #     elif trade[0] == 'Sell':
        #         print(f"{trade[0]}: Date: {trade[1]}, Price: {trade[2]}, Shares: {trade[3]}, Remaining Capital: {trade[4]}")
