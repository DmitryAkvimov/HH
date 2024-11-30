import ccxt
import pandas as pd
import time
import json
import os

# Загрузка конфигурации
config_path = os.path.join("data", "config.json")
with open(config_path, "r") as f:
    config = json.load(f)

# Инициализация биржи
exchange = ccxt.binance({
    'apiKey': config["api_key"],
    'secret': config["secret_key"],
})


def fetch_historical_data(symbol, timeframe, since=None, limit=1000):
    """
    Получение исторических данных через CCXT.
    :param symbol: Тикер (например, 'BTC/USDT')
    :param timeframe: Таймфрейм (например, '1d', '4h')
    :param since: Начало (timestamp в мс)
    :param limit: Количество свечей за раз
    :return: DataFrame
    """
    all_data = []
    while True:
        try:
            candles = exchange.fetch_ohlcv(symbol, timeframe, since, limit)
            if not candles:
                break
            all_data.extend(candles)
            since = candles[-1][0] + 1
            time.sleep(exchange.rateLimit / 1000)
        except Exception as e:
            print(f"Ошибка: {e}")
            break

    # Конвертация данных в DataFrame
    df = pd.DataFrame(all_data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df
