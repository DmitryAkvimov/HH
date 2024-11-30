from fetch_signals import fetch_tradingview_signals
from fetch_historical import fetch_historical_data

def merge_signals_and_data(symbol):
    """
    Объединяет сигналы TradingView и исторические данные в одну структуру.
    """
    signals = fetch_tradingview_signals(symbol)
    historical_data = fetch_historical_data(symbol)

    # Добавляем данные индикаторов в исторические данные
    historical_data["ema_9"] = signals.get("ema_9", None)
    historical_data["macd"] = signals.get("macd", None)
    historical_data["macd_signal"] = signals.get("macd_signal", None)
    historical_data["rsi"] = signals.get("rsi", None)

    return historical_data

if __name__ == "__main__":
    # Тестируем функцию с символом BTC/USDT
    test_symbol = "BTC/USDT"
    merged_data = merge_signals_and_data(test_symbol)
    print(f"Объединенные данные для {test_symbol}:")
    print(merged_data.head())
