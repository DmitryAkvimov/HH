import json
import csv

def save_to_json(data, filename):
    """Сохранение данных в JSON файл."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Данные сохранены в {filename}")
    except Exception as e:
        print(f"Ошибка при сохранении в JSON: {e}")

def save_to_csv(data, filename):
    """Сохранение данных в CSV файл."""
    try:
        with open(filename, "w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            for key, value in data.items():
                writer.writerow([key, value])
        print(f"Данные сохранены в {filename}")
    except Exception as e:
        print(f"Ошибка при сохранении в CSV: {e}")
