import sys
import os
import json
from fetch_historical import fetch_historical_data
from fetch_signals import fetch_tradingview_signals

# Определяем путь к корневой директории проекта
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from project.utils.file_handler import save_to_json, save_to_csv

# Путь к конфигурации
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../data/config.json")
with open(CONFIG_PATH) as config_file:
    config = json.load(config_file)

# Путь для сохранения сигналов
DATA_DIR = os.path.join(os.path.dirname(__file__), "../data")
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
SIGNALS_FILE = os.path.join(DATA_DIR, "signals.json")

def save_signals_to_file(signals, symbol, interval):
    """Сохраняет сигналы в файл JSON."""
    try:
        # Если файл существует, загрузить текущие данные
        if os.path.exists(SIGNALS_FILE):
            with open(SIGNALS_FILE, "r", encoding="utf-8") as file:
                all_signals = json.load(file)
        else:
            all_signals = {}

        # Добавить или обновить сигналы
        if symbol not in all_signals:
            all_signals[symbol] = {}
        all_signals[symbol][interval] = signals

        # Записать данные обратно в файл
        with open(SIGNALS_FILE, "w", encoding="utf-8") as file:
            json.dump(all_signals, file, ensure_ascii=False, indent=4)
        print(f"Сигналы для {symbol} ({interval}) сохранены в файл.")
    except Exception as e:
        print(f"Ошибка при сохранении сигналов: {e}")

def main():
    # Список символов для анализа
    symbols = config["symbols"]
    intervals = config["timeframes"]
    
    for symbol in symbols:
        print(f"\nСбор исторических данных для {symbol}...")
        for interval in intervals:
            fetch_historical_data(symbol, interval)
        
        print(f"\nПолучение сигналов TradingView для {symbol}...")
        for interval in intervals:
            signals = fetch_tradingview_signals(symbol, interval)
            print(f"Сигналы для {symbol} ({interval}): {signals}")
            
            # Сохранение сигналов в файл
            save_signals_to_file(signals, symbol, interval)

if __name__ == "__main__":
    main()
