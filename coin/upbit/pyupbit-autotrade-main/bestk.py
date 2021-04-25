import pyupbit
import numpy as np
import time


tickers = pyupbit.get_tickers(fiat="KRW")

def get_ror(coin_name, k=0.5):
    fee = 0.05
    df = pyupbit.get_ohlcv(coin_name, count=7)
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    df['ror'] = np.where(df['high'] > df['target'],
                         df['close'] / df['target'] - fee,
                         1)

    ror = df['ror'].cumprod()[-2]
    return ror


hi_k = []
for i in tickers:
    highk = []
    for k in np.arange(0.1, 1.0, 0.1):
        ror = get_ror(i, k)
        # print(i+" %.1f %f" % (k, ror))
        highk.append([ror, k])
    # print(i[4:] + ' ' + str(max(highk)[1]))
    hi_k.append([max(highk), i[4:]])
    time.sleep(0.7)
print(max(hi_k))
