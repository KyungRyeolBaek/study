from pykrx import stock
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
    fundamental_data[code] = stock.get_market_fundamental_by_date(start_date, end_date, code)
    if not fundamental_data[code].empty:
        # PER과 DIV 조건에 맞는지 확인 (예: PER < 10, DIV > 2%)
        if fundamental_data[code]['PER'].mean() < 10 and fundamental_data[code]['DIV'].mean() > 2:
            ohlcv_data[code] = stock.get_market_ohlcv_by_date(start_date, end_date, code)

# 3. 추천 종목 리스트에서 추가 조건 확인 및 이동평균선, 볼린저 밴드 계산
print('Starting Step 3 and 4')
final_selected_stocks = []
for code, df in ohlcv_data.items():
    df['MA5'] = df['종가'].rolling(window=5).mean()
    df['MA20'] = df['종가'].rolling(window=20).mean()
    df['MA60'] = df['종가'].rolling(window=60).mean()

    df['Middle Band'] = df['MA20']  # 중간 볼린저 밴드는 20일 이동평균선
    df['Upper Band'] = df['Middle Band'] + 2 * df['종가'].rolling(window=20).std()
    df['Lower Band'] = df['Middle Band'] - 2 * df['종가'].rolling(window=20).std()

    if df['MA5'].iloc[-1] > df['MA20'].iloc[-1] > df['MA60'].iloc[-1] and \
       df['종가'].iloc[-1] < df['Middle Band'].iloc[-1] and \
       df['종가'].iloc[-1] > df['Lower Band'].iloc[-1]:
        final_selected_stocks.append(code)

# 6. 최종 종목 리스트 출력
print('Starting Last Step')
final_stock_names = [(code, stock.get_market_ticker_name(code)) for code in final_selected_stocks]
print("추천 종목 리스트:")
for code, name in final_stock_names:
    print(f"{code} {name}")
