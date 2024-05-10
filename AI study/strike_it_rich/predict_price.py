import numpy as np
# import pandas as pd
import tensorflow as tf
from pykrx import stock
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from sklearn.preprocessing import MinMaxScaler


# 종목 코드와 날짜 설정
stock_code = "033780"  # 삼성전자 예시
end_date = datetime.today().strftime("%Y%m%d")
start_date = (datetime.today() - timedelta(days=365)).strftime("%Y%m%d")

# OHLCV 데이터 가져오기
ohlcv = stock.get_market_ohlcv_by_date(fromdate=start_date, todate=end_date, ticker=stock_code)

# 펀더멘털 지표 가져오기
fundamental = stock.get_market_fundamental_by_date(fromdate=start_date, todate=end_date, ticker=stock_code)

# 데이터 준비
data = ohlcv['종가'].values.reshape(-1, 1)
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data)


# LSTM에 입력할 데이터 형태로 변환
def create_dataset(data, look_back=1):
    X, Y = [], []
    for i in range(len(data) - look_back - 1):
        a = data[i:(i + look_back), 0]
        X.append(a)
        Y.append(data[i + look_back, 0])
    return np.array(X), np.array(Y)


look_back = 5
X, Y = create_dataset(scaled_data, look_back)

# 훈련 데이터와 테스트 데이터 분리 (예: 최근 20% 데이터를 테스트 데이터로 사용)
train_size = int(len(X) * 0.8)
test_size = len(X) - train_size
trainX, testX = X[0:train_size], X[train_size:len(X)]
trainY, testY = Y[0:train_size], Y[train_size:len(Y)]

# LSTM 모델 구성 및 학습
model = tf.keras.models.Sequential([
    tf.keras.layers.LSTM(50, return_sequences=True, input_shape=(look_back, 1)),
    tf.keras.layers.LSTM(50),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(trainX, trainY, epochs=100, batch_size=1, verbose=2)

# 내일부터 일주일간 주가 예측
to_predict = scaled_data[-look_back:]
predicted_price = model.predict(np.array([to_predict]))
predicted_price = scaler.inverse_transform(predicted_price)  # 예측된 값을 원래 스케일로 변환

print("예측된 가격:", predicted_price)

# 실제 가격과 예측 가격 비교를 위한 데이터 준비
trainPredict = model.predict(trainX)
testPredict = model.predict(testX)
trainPredict = scaler.inverse_transform(trainPredict)
testPredict = scaler.inverse_transform(testPredict)
trainY = scaler.inverse_transform([trainY])
testY = scaler.inverse_transform([testY])

# 시각화
plt.plot(data, label='Actual Price')
plt.plot(np.append(trainPredict, testPredict), label='Predicted Price')
plt.legend()
plt.show()
