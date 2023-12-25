import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from pykrx import stock
import pandas as pd

class StockSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("StockSystem.ui", self)
        self.pushButton.clicked.connect(self.search_stocks)

    def search_stocks(self):
        per_threshold = float(self.lineEdit.text())
        div_threshold = float(self.lineEdit_2.text())

        tickers = stock.get_market_ticker_list(market="KOSPI")
        selected_stocks = []

        for ticker in tickers:
            df = stock.get_market_ohlcv_by_date("20220101", "20221231", ticker)
            df_fundamental = stock.get_market_fundamental_by_ticker("20221231", market="KOSPI")

            if ticker in df_fundamental.index:
                per = df_fundamental.loc[ticker, "PER"]
                div = df_fundamental.loc[ticker, "DIV"]
                if per >= per_threshold and div >= div_threshold:
                    # Calculate moving averages
                    df['MA5'] = df['종가'].rolling(window=5).mean()
                    df['MA20'] = df['종가'].rolling(window=20).mean()
                    df['MA60'] = df['종가'].rolling(window=60).mean()

                    # Check for positive arrangement
                    if df['MA5'][-1] > df['MA20'][-1] > df['MA60'][-1]:
                        # Calculate Bollinger Bands
                        df['MA20'] = df['종가'].rolling(window=20).mean()
                        df['stddev'] = df['종가'].rolling(window=20).std()
                        df['lower_band'] = df['MA20'] - (2 * df['stddev'])
                        df['upper_band'] = df['MA20'] + (2 * df['stddev'])

                        # Check if the current price is between the middle and lower band
                        if df['lower_band'][-1] < df['종가'][-1] < df['MA20'][-1]:
                            selected_stocks.append((ticker, stock.get_market_ticker_name(ticker)))

        # Display the selected stocks
        self.textEdit.clear()
        for ticker, name in selected_stocks:
            self.textEdit.append(f"{ticker}: {name}")

app = QApplication(sys.argv)
window = StockSystem()
window.show()
sys.exit(app.exec_())
