import ccxt
import pandas as pd
import json
import os

# Загружаем конфигурацию из data/config.json
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../data/config.json")
with open(CONFIG_PATH) as config_file:
    config = json.load(config_file)

def fetch_historical_data(symbol, timeframe="1h", limit=500):
    """
    Получает исторические данные OHLCV для указанного символа.
    """
    exchange = ccxt.binance()
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    return df

if __name__ == "__main__":
    # Тестируем функцию с символом BTC/USDT
    test_symbol = "BTC/USDT"
    data = fetch_historical_data(test_symbol)
    print(f"Исторические данные для {test_symbol}:")
    print(data.head())
