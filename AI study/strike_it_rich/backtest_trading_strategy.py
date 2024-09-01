import pandas as pd
import numpy as np
import yfinance as yf
from pykrx import stock
from datetime import datetime, timedelta

def get_stock_data(ticker, interval, start_date, end_date):
    # 주식 데이터 불러오기
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

def buy_shares(capital, close_price):
    # 원금의 1%만 사용하여 주식을 매수하는 함수
    purchase_amount = capital * 0.01  # 원금의 1%
    shares_to_buy = purchase_amount // close_price
    new_capital = capital - shares_to_buy * close_price
    return shares_to_buy, new_capital

def backtest_all_stocks(kospi200, interval, start_date, end_date, short_window, long_window):
    initial_capital = 1000000.0  # 초기 자본 설정
    capital = initial_capital
    total_shares = {}
    trades = []

    for ticker in kospi200:
        try:
            ticker_yahoo = ticker + ".KS"  # 야후 파이낸스 형식에 맞게 변환
            df = get_stock_data(ticker_yahoo, interval, start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"))

            if not df.empty:
                df = apply_moving_average_strategy(df, short_window, long_window)
                total_shares[ticker] = 0  # 각 종목별 보유 주식 수 초기화

                for i in range(len(df)):
                    if df['Position'].iloc[i] == 1:  # 매수 신호
                        shares_to_buy, capital = buy_shares(capital, df['Close'].iloc[i])
                        total_shares[ticker] += shares_to_buy
                        trades.append(('Buy', ticker, df.index[i], df['Close'].iloc[i], shares_to_buy, capital))
                    elif df['Position'].iloc[i] == -1 and total_shares[ticker] > 0:  # 매도 신호
                        capital += total_shares[ticker] * df['Close'].iloc[i]
                        trades.append(('Sell', ticker, df.index[i], df['Close'].iloc[i], total_shares[ticker], capital))
                        total_shares[ticker] = 0

        except Exception as e:
            print(f"Error processing {ticker}: {e}")

    # 최종 자본 계산
    final_capital = capital
    for ticker in kospi200:
        try:
            ticker_yahoo = ticker + ".KS"
            df = get_stock_data(ticker_yahoo, interval, start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"))
            if not df.empty and total_shares[ticker] > 0:
                final_capital += total_shares[ticker] * df['Close'].iloc[-1]  # 남은 주식을 마지막 종가로 계산
        except Exception as e:
            print(f"Error calculating final capital for {ticker}: {e}")

    total_profit = final_capital - initial_capital
    return_rate = (total_profit / initial_capital) * 100

    return final_capital, total_profit, return_rate, trades

if __name__ == "__main__":
    # KOSPI 200 종목 가져오기
    kospi200 = stock.get_index_portfolio_deposit_file("1028")
    interval = "1h"  # 1시간 단위 데이터
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)  # 30일 기간
    
    short_window = 40
    long_window = 100

    final_capital, total_profit, return_rate, trades = backtest_all_stocks(kospi200, interval, start_date, end_date, short_window, long_window)

    print(f"Initial Capital: 1000000.0")
    print(f"Final Capital: {round(final_capital, 1)}")
    print(f"Total Profit: {round(total_profit, 1)}")
    print(f"Return Rate: {round(return_rate, 1)}%")
    print("Trades:")
    for trade in trades:
        if trade[0] == 'Buy':
            print(f"{trade[0]}: Ticker: {trade[1]}, Date: {trade[2]}, Price: {trade[3]}, Shares: {trade[4]}, Remaining Capital: {trade[5]}")
        elif trade[0] == 'Sell':
            print(f"{trade[0]}: Ticker: {trade[1]}, Date: {trade[2]}, Price: {trade[3]}, Shares: {trade[4]}, Remaining Capital: {trade[5]}")
