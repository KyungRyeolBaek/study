from pykrx import stock
# import pandas as pd
from datetime import datetime, timedelta


# 1. 코스피 200 지수의 구성 종목 리스트 구하기
print('Starting Step 1')
kospi200 = stock.get_index_portfolio_deposit_file("1028")  # 코스피 200 지수 코드

# 2. 해당 주식들의 OHLCV와 펀더멘털 지표 구하기
print('Starting Step 2')
end_date = datetime.today().strftime("%Y%m%d")  # 오늘 날짜
start_date = (datetime.today() - timedelta(days=365)).strftime("%Y%m%d")  # 1년 전 날짜

ohlcv_data = {}
fundamental_data = {}
for code in kospi200:
    ohlcv_data[code] = stock.get_market_ohlcv_by_date(start_date, end_date, code)
    fundamental_data[code] = stock.get_market_fundamental_by_date(start_date, end_date, code)

# 3. PER과 DIV를 기준으로 추천 종목 고르기
print('Starting Step 3')
recommended_stocks = []
for code in kospi200:
    df = fundamental_data[code]
    if not df.empty:
        # PER과 DIV 조건에 맞는지 확인 (예: PER < 10, DIV > 2%)
        if df['PER'].mean() > 10 and df['DIV'].mean() > 2:
            recommended_stocks.append(code)

# 4. 이동평균선과 5. 볼린저 밴드 계산
print('Starting Step 4')
final_selected_stocks = []
for code in recommended_stocks:
    df = ohlcv_data[code]

    # 이동평균선 계산
    df['MA5'] = df['종가'].rolling(window=5).mean()
    df['MA20'] = df['종가'].rolling(window=20).mean()
    df['MA60'] = df['종가'].rolling(window=60).mean()

    # 볼린저 밴드 계산
    df['Middle Band'] = df['종가'].rolling(window=20).mean()
    df['Upper Band'] = df['Middle Band'] + 2 * df['종가'].rolling(window=20).std()
    df['Lower Band'] = df['Middle Band'] - 2 * df['종가'].rolling(window=20).std()

    # 이동평균선 정배열 및 볼린저 밴드 조건 확인
    if df['MA5'][-1] > df['MA20'][-1] > df['MA60'][-1] and \
       df['종가'][-1] < df['Middle Band'][-1] and \
       df['종가'][-1] > df['Lower Band'][-1]:
        final_selected_stocks.append(code)

# 6. 최종 종목 리스트 출력
print('Starting Last Step')
final_stock_names = [(code, stock.get_market_ticker_name(code)) for code in final_selected_stocks]
print("추천 종목 리스트:")
for code, name in final_stock_names:
    print(f"{code} {name}")
