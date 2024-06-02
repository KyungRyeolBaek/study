import tkinter as tk
from tkinter import scrolledtext, Toplevel
from pykrx import stock
from datetime import datetime, timedelta
import threading
import pickle
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# 파일 경로
base_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_path, 'datas')
cache_file = os.path.join(data_path, 'stock_data_cache.pkl')
kospi200_cache = os.path.join(data_path, 'kospi200.pkl')

# 글로벌 변수로 그래프 캔버스 설정
graph_canvases = {}


def long_running_task(callback, per_threshold, div_threshold, ma_windows):
    result = fetch_and_process_stocks(per_threshold, div_threshold, ma_windows)
    callback(result)


def save_to_cache(data, settings):
    with open(cache_file, 'wb') as f:
        pickle.dump((data, settings), f)


def load_from_cache(settings):
    if os.path.exists(cache_file):
        with open(cache_file, 'rb') as f:
            cached_data, cached_settings = pickle.load(f)
            if cached_settings == settings:
                return cached_data
    return None


def save_kospi200_to_cache(kospi200, date):
    with open(kospi200_cache, 'wb') as f:
        pickle.dump((kospi200, date), f)


def load_kospi200_from_cache():
    if os.path.exists(kospi200_cache):
        with open(kospi200_cache, 'rb') as f:
            kospi200, cached_date = pickle.load(f)
            current_date = datetime.today().strftime("%Y%m%d")
            if cached_date == current_date:
                return kospi200
    return None


def fetch_kospi200(use_cache=True):
    current_date = datetime.today().strftime("%Y%m%d")
    if use_cache:
        kospi200 = load_kospi200_from_cache()
        if kospi200 is not None:
            return kospi200

    kospi200 = stock.get_index_portfolio_deposit_file("1028")
    save_kospi200_to_cache(kospi200, current_date)
    return kospi200


def fetch_and_process_stocks(per_threshold, div_threshold, ma_windows, use_cache=True):
    settings = (per_threshold, div_threshold, tuple(ma_windows))
    if use_cache:
        cached_data = load_from_cache(settings)
        if cached_data:
            return cached_data

    kospi200 = fetch_kospi200(use_cache)
    end_date = datetime.today().strftime("%Y%m%d")
    start_date = (datetime.today() - timedelta(days=365)).strftime("%Y%m%d")

    final_selected_stocks = []

    for code in kospi200:
        fundamental = stock.get_market_fundamental_by_date(start_date, end_date, code)
        if not fundamental.empty:
            if fundamental['PER'].mean() < per_threshold and fundamental['DIV'].mean() > div_threshold:
                ohlcv = stock.get_market_ohlcv_by_date(start_date, end_date, code)
                ohlcv['MA5'] = ohlcv['종가'].rolling(window=ma_windows[0]).mean()
                ohlcv['MA20'] = ohlcv['종가'].rolling(window=ma_windows[1]).mean()
                ohlcv['MA60'] = ohlcv['종가'].rolling(window=ma_windows[2]).mean()

                ohlcv['Middle Band'] = ohlcv['MA20']
                ohlcv['Upper Band'] = ohlcv['Middle Band'] + 2 * ohlcv['종가'].rolling(window=ma_windows[1]).std()
                ohlcv['Lower Band'] = ohlcv['Middle Band'] - 2 * ohlcv['종가'].rolling(window=ma_windows[1]).std()

                if ohlcv['MA5'].iloc[-1] > ohlcv['MA20'].iloc[-1] > ohlcv['MA60'].iloc[-1] and \
                   ohlcv['종가'].iloc[-1] < ohlcv['Middle Band'].iloc[-1] and \
                   ohlcv['종가'].iloc[-1] > ohlcv['Lower Band'].iloc[-1]:
                    final_selected_stocks.append(code)

    final_stock_names = [(code, stock.get_market_ticker_name(code)) for code in final_selected_stocks]
    save_to_cache(final_stock_names, settings)
    return final_stock_names


def show_stock_graph(stock_code, root):
    global graph_canvases
    end_date = datetime.today().strftime("%Y%m%d")
    start_date = (datetime.today() - timedelta(days=365)).strftime("%Y%m%d")
    df = stock.get_market_ohlcv_by_date(start_date, end_date, stock_code)

    graph_window = Toplevel(root)
    graph_window.title(f"Stock Graph - {stock.get_market_ticker_name(stock_code)}")
    figure = plt.Figure(figsize=(6, 5), dpi=100)
    ax = figure.add_subplot(111)
    df['종가'].plot(ax=ax)
    ax.set_title(f"{stock.get_market_ticker_name(stock_code)} 종가")

    canvas = FigureCanvasTkAgg(figure, graph_window)
    canvas.draw()
    canvas.get_tk_widget().pack()


def setup():
    global root
    root = tk.Tk()
    root.geometry("350x550")
    root.title("Stock Analysis Configuration")

    tk.Label(root, text="PER Threshold: (e.g., 10, recommended < 15):").pack()
    per_entry = tk.Entry(root)
    per_entry.pack()
    per_entry.insert(0, "10")

    tk.Label(root, text="DIV Threshold: (e.g., 2, recommended > 1.5%):").pack()
    div_entry = tk.Entry(root)
    div_entry.pack()
    div_entry.insert(0, "2")

    tk.Label(root, text="MA Windows (e.g., 5,20,60):").pack()
    ma_entry = tk.Entry(root)
    ma_entry.pack()
    ma_entry.insert(0, "5,20,60")

    result_text = scrolledtext.ScrolledText(root, height=10)
    result_text.pack()

    status_label = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
    status_label.pack(side=tk.BOTTOM, fill=tk.X)

    def on_submit():
        per_threshold = float(per_entry.get())
        div_threshold = float(div_entry.get())
        ma_windows = list(map(int, ma_entry.get().split(',')))
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.INSERT, "Processing...")
        status_label.config(text="Processing...")
        thread = threading.Thread(target=long_running_task, args=(lambda result: update_result(result, result_text, status_label), per_threshold, div_threshold, ma_windows))
        thread.start()

    def update_result(result, result_text, status_label):
        result_str = "\n".join([f"{code} {name}" for code, name in result])
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.INSERT, result_str)
        status_label.config(text="Ready")
        for stock_code, _ in result:
            show_stock_graph(stock_code, root)

    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.pack()

    root.mainloop()


if __name__ == "__main__":
    setup()
