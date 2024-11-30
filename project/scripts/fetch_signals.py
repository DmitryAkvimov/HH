import sys
import os
import argparse

# Добавляем путь к каталогу project в системный путь
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'project'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Импортируем необходимые библиотеки
from tradingview_ta import TA_Handler, Interval, Exchange
from project.utils.file_handler import save_to_json, save_to_csv

def fetch_tradingview_signals(symbol, exchange="Binance", screener="crypto", interval="1h"):
    """Получение сигналов TradingView для указанного символа."""
    try:
        analysis = TA_Handler(
            symbol=symbol,
            exchange=exchange,
            screener=screener,
            interval=interval
        ).get_analysis()

        result = {
            "summary": analysis.summary,
            "indicators": analysis.indicators
        }
        return result
    except Exception as e:
        print(f"Ошибка при получении сигналов: {e}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch TradingView signals")
    parser.add_argument("--symbol", type=str, required=True, help="Тикер символа (например, BTCUSDT)")
    parser.add_argument("--exchange", type=str, default="Binance", help="Биржа (по умолчанию Binance)")
    parser.add_argument("--interval", type=str, default="1h", help="Таймфрейм (по умолчанию 1h)")
    args = parser.parse_args()

    result = fetch_tradingview_signals(symbol=args.symbol, exchange=args.exchange, interval=args.interval)

    if result:
        save_to_json(result, filename=f"{args.symbol}_signals.json")
        save_to_csv(result, filename=f"{args.symbol}_signals.csv")
