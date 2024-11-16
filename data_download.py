# Модуль data_download.py:
# Отвечает за загрузку данных об акциях.
# Содержит функции для извлечения данных об акциях из интернета и расчёта скользящего среднего.

import yfinance as yf


# Функция fetch_stock_data(ticker, period): Получает исторические данные об акциях для указанного тикера и временного
# периода. Возвращает DataFrame с данными.
def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


# Функция add_moving_average(data, window_size): Добавляет в DataFrame колонку со скользящим средним, рассчитанным на
# основе цен закрытия.
def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data

# Функция calculate_and_display_average_price(data):
# вычисляет и выводит среднюю цену закрытия акций за заданный период. Функция принимает DataFrame и вычисляет среднее
# значение колонки 'Close'. Результат выводится в консоль.
def calculate_and_display_average_price(data):
    data_Average_Close = data['Close'].mean()
    return data_Average_Close