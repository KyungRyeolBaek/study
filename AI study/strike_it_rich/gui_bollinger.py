import os
import json
import pickle
import threading
import tkinter as tk
from pykrx import stock
import matplotlib.pyplot as plt
from tkinter import Toplevel, messagebox
from datetime import datetime, timedelta
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# 파일 경로
base_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_path, 'datas')
if not os.path.exists(data_path):
    os.makedirs(data_path)
cache_file = os.path.join(data_path, 'stock_data_cache.pkl')
kospi200_cache = os.path.join(data_path, 'kospi200.pkl')
purchased_file = os.path.join(data_path, 'purchased_stocks.json')

# 글로벌 변수로 그래프 캔버스 설정
graph_canvases = {}


def long_running_task(callback, thresholds, show_bollinger):
    result = fetch_and_process_stocks(thresholds, show_bollinger)
    callback(result, show_bollinger)


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


def fetch_and_process_stocks(thresholds, show_bollinger, use_cache=True):
    settings = tuple(thresholds.values()) + (show_bollinger,)
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
            per_mean = fundamental['PER'].mean()
            pbr_mean = fundamental['PBR'].mean()
            eps_mean = fundamental['EPS'].mean()
            bps_mean = fundamental['BPS'].mean()

            # Safely get DIV data with a default value if it's missing
            div_mean = fundamental['DIV'].mean() if 'DIV' in fundamental.columns else 0

            if bps_mean != 0:
                roe_mean = (eps_mean / bps_mean) * 100
            else:
                roe_mean = 0

            if (per_mean < thresholds['PER'] and
                pbr_mean < thresholds['PBR'] and
                roe_mean > thresholds['ROE'] and
                eps_mean > thresholds['EPS'] and
                div_mean > thresholds['DIV']):
                ohlcv = stock.get_market_ohlcv_by_date(start_date, end_date, code)

                if show_bollinger:
                    ohlcv['Middle Band'] = ohlcv['종가'].rolling(window=20).mean()
                    ohlcv['Upper Band'] = ohlcv['Middle Band'] + 2 * ohlcv['종가'].rolling(window=20).std()
                    ohlcv['Lower Band'] = ohlcv['Middle Band'] - 2 * ohlcv['종가'].rolling(window=20).std()

                    if (ohlcv['종가'].iloc[-1] < ohlcv['Middle Band'].iloc[-1] and
                        ohlcv['종가'].iloc[-1] > ohlcv['Lower Band'].iloc[-1]):
                        final_selected_stocks.append((code, stock.get_market_ticker_name(code), per_mean, pbr_mean, roe_mean, eps_mean, div_mean))
                else:
                    ohlcv['MA5'] = ohlcv['종가'].rolling(window=5).mean()
                    ohlcv['MA20'] = ohlcv['종가'].rolling(window=20).mean()
                    ohlcv['MA60'] = ohlcv['종가'].rolling(window=60).mean()

                    if (ohlcv['MA5'].iloc[-1] > ohlcv['MA20'].iloc[-1] > ohlcv['MA60'].iloc[-1]):
                        final_selected_stocks.append((code, stock.get_market_ticker_name(code), per_mean, pbr_mean, roe_mean, eps_mean, div_mean))

    save_to_cache(final_selected_stocks, settings)
    return final_selected_stocks


def show_stock_graph(stock_code, root, show_bollinger, position='center'):
    global graph_canvases
    end_date = datetime.today().strftime("%Y%m%d")
    start_date = (datetime.today() - timedelta(days=365)).strftime("%Y%m%d")
    df = stock.get_market_ohlcv_by_date(start_date, end_date, stock_code)

    graph_window = Toplevel(root)
    if position == 'bottom_right':
        position_window(graph_window, 800, 600, position='bottom_right')
    else:
        position_window(graph_window, 800, 600)
    graph_window.title(f"Stock Graph - {stock.get_market_ticker_name(stock_code)}")
    figure = plt.Figure(figsize=(8, 6), dpi=100)
    ax = figure.add_subplot(111)
    df['종가'].plot(ax=ax, label='Close Price', alpha=0.7)  # 투명도 설정
    if show_bollinger:
        df['Middle Band'] = df['종가'].rolling(window=20).mean()
        df['Upper Band'] = df['Middle Band'] + 2 * df['종가'].rolling(window=20).std()
        df['Lower Band'] = df['Middle Band'] - 2 * df['종가'].rolling(window=20).std()
        df[['Middle Band', 'Upper Band', 'Lower Band']].plot(ax=ax, alpha=0.3)  # 투명도 설정
        ax.legend()

    ax.set_title(f"{stock.get_market_ticker_name(stock_code)} 종가")

    canvas = FigureCanvasTkAgg(figure, graph_window)
    canvas.draw()
    canvas.get_tk_widget().pack()


def load_purchased_stocks():
    if os.path.exists(purchased_file):
        with open(purchased_file, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def save_purchased_stock(stock_code):
    purchased_stocks = load_purchased_stocks()
    end_date = datetime.today().strftime("%Y%m%d")
    start_date = (datetime.today() - timedelta(days=7)).strftime("%Y%m%d")  # 최근 일주일 데이터로 변경
    df = stock.get_market_ohlcv_by_date(start_date, end_date, stock_code)
    if df.empty or '종가' not in df.columns:
        messagebox.showerror("Error", f"Failed to fetch data for stock {stock_code}.")
        return
    purchase_price = float(df['종가'].iloc[-1])  # Convert to float to avoid numpy types
    purchase_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    stock_info = {"code": stock_code, "purchase_price": purchase_price, "purchase_time": purchase_time}
    purchased_stocks.append(stock_info)
    with open(purchased_file, 'w') as f:
        json.dump(purchased_stocks, f, indent=4)
    messagebox.showinfo("Success", f"Stock {stock_code} purchased successfully at {purchase_price} on {purchase_time}.")


def sell_stock(stock_code, frame, purchased_window):
    purchased_stocks = load_purchased_stocks()
    stock_info = next((item for item in purchased_stocks if item["code"] == stock_code), None)
    if stock_info:
        end_date = datetime.today().strftime("%Y%m%d")
        start_date = (datetime.today() - timedelta(days=7)).strftime("%Y%m%d")  # 최근 일주일 데이터로 변경
        df = stock.get_market_ohlcv_by_date(start_date, end_date, stock_code)
        if df.empty or '종가' not in df.columns:
            messagebox.showerror("Error", f"Failed to fetch data for stock {stock_code}.")
            return
        sell_price = float(df['종가'].iloc[-1])  # Convert to float to avoid numpy types
        sell_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        purchase_price = stock_info["purchase_price"]
        profit = sell_price - purchase_price
        profit_percentage = (profit / purchase_price) * 100

        purchased_stocks.remove(stock_info)
        with open(purchased_file, 'w') as f:
            json.dump(purchased_stocks, f, indent=4)

        frame.destroy()  # Remove the frame containing the sold stock

        messagebox.showinfo("Success", f"Stock {stock_code} sold successfully at {sell_price} on {sell_time}.\nProfit: {profit} ({profit_percentage:.2f}%)")

        purchased_window.destroy()  # Close the purchased stocks window

        # Refresh the purchased stocks window
        view_purchased_stocks(root)
    else:
        messagebox.showwarning("Warning", f"Stock {stock_code} is not in the purchased list.")


def position_window(window, width, height, position='center'):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    if position == 'top_right':
        x = screen_width - width - 50  # 50 for some margin
        y = 50  # 50 for some margin
    elif position == 'bottom_right':
        x = screen_width - width - 50  # 50 for some margin
        y = screen_height - height - 50  # 50 for some margin
    else:
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")


def view_purchased_stocks(root):
    purchased_stocks = load_purchased_stocks()
    if not purchased_stocks:
        messagebox.showinfo("Info", "No stocks purchased yet.")
        return

    purchased_window = Toplevel(root)
    position_window(purchased_window, 1000, 800, position='top_right')
    purchased_window.title("Purchased Stocks")
    for stock_info in purchased_stocks:
        stock_code = stock_info["code"]
        stock_name = stock.get_market_ticker_name(stock_code)
        frame = tk.Frame(purchased_window)
        frame.pack(fill=tk.X, pady=5)

        label = tk.Label(frame, text=f"{stock_code} {stock_name} (Purchased at {stock_info['purchase_price']} on {stock_info['purchase_time']})", font=("Helvetica", 12))
        label.pack(side=tk.LEFT, padx=5)

        button = tk.Button(frame, text="Sell", command=lambda stock_code=stock_code, frame=frame: sell_stock(stock_code, frame, purchased_window), font=("Helvetica", 12))
        button.pack(side=tk.RIGHT, padx=5)

        # Show the stock graph in the same frame
        show_stock_graph(stock_code, frame, show_bollinger=True, position='bottom_right')


def setup():
    global root
    root = tk.Tk()
    root.geometry("800x900")
    root.title("Stock Analysis Configuration")

    labels_and_entries = [
        ("PER Threshold: (e.g., 10, recommended < 15):", "10"),
        ("PBR Threshold: (e.g., 1, recommended < 1):", "1"),
        ("ROE Threshold: (e.g., 15, recommended > 15%):", "15"),
        ("EPS Threshold: (e.g., 2, recommended > 2):", "2"),
        ("DIV Threshold: (e.g., 2, recommended > 2%):", "2")
    ]

    entries = {}
    for label_text, default_value in labels_and_entries:
        tk.Label(root, text=label_text, font=("Helvetica", 12)).pack(pady=5)
        entry = tk.Entry(root, font=("Helvetica", 12), width=10)
        entry.pack(pady=5)
        entry.insert(0, default_value)
        entries[label_text.split()[0]] = entry

    show_bollinger_var = tk.BooleanVar()
    tk.Checkbutton(root, text="Show Bollinger Bands", variable=show_bollinger_var, font=("Helvetica", 12)).pack(pady=5)

    result_frame = tk.Frame(root)
    result_frame.pack(pady=10, fill=tk.BOTH, expand=True)

    result_canvas = tk.Canvas(result_frame)
    result_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(result_frame, orient="vertical", command=result_canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill="y")

    result_canvas.configure(yscrollcommand=scrollbar.set)
    result_canvas.bind("<Configure>", lambda e: result_canvas.configure(scrollregion=result_canvas.bbox("all")))

    result_content = tk.Frame(result_canvas)
    result_canvas.create_window((0, 0), window=result_content, anchor="nw")

    status_label = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W, font=("Helvetica", 12))
    status_label.pack(side=tk.BOTTOM, fill=tk.X)

    def on_submit():
        thresholds = {key: float(entry.get()) for key, entry in entries.items()}
        show_bollinger = show_bollinger_var.get()
        for widget in result_content.winfo_children():
            widget.destroy()
        status_label.config(text="Processing...")
        thread = threading.Thread(target=long_running_task, args=(lambda result, show_bollinger=show_bollinger: update_result(result, result_content, status_label, show_bollinger), thresholds, show_bollinger))
        thread.start()

    def update_result(result, result_content, status_label, show_bollinger):
        for code, name, per, pbr, roe, eps, div in result:
            frame = tk.Frame(result_content)
            frame.pack(fill=tk.X, pady=5)

            label = tk.Label(frame, text=f"{code} {name} (PER: {per:.2f}, PBR: {pbr:.2f}, ROE: {roe:.2f}%, EPS: {eps:.2f}, DIV: {div:.2f}%)", font=("Helvetica", 12))
            label.pack(side=tk.LEFT, padx=5)

            button = tk.Button(frame, text="Buy", command=lambda code=code: save_purchased_stock(code), font=("Helvetica", 12))
            button.pack(side=tk.RIGHT, padx=5)

        status_label.config(text="Ready")

    submit_button = tk.Button(root, text="Submit", command=on_submit, font=("Helvetica", 12), padx=20, pady=10)
    submit_button.pack(pady=20)

    view_purchased_button = tk.Button(root, text="View Purchased Stocks", command=lambda: view_purchased_stocks(root), font=("Helvetica", 12), padx=20, pady=10)
    view_purchased_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    setup()
