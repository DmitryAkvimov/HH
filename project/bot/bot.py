from telegram import Update, Bot
from telegram.ext import CommandHandler, CallbackContext, Updater
from project.scripts.fetch_signals import fetch_tradingview_signals

TELEGRAM_TOKEN = "7388407520:AAGv83e-BjKQ6qC8IPD6xH2wjFt1-KzLw5c"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Отправьте /signal SYMBOL для получения сигналов.")

def signal(update: Update, context: CallbackContext):
    symbol = context.args[0] if context.args else "BTCUSDT"
    result = fetch_tradingview_signals(symbol=symbol)
    if result:
        message = f"Сигналы для {symbol}:\nРекомендация: {result['summary']['RECOMMENDATION']}\n"
        update.message.reply_text(message)
    else:
        update.message.reply_text("Не удалось получить сигналы. Попробуйте еще раз.")

def main():
    updater = Updater(TELEGRAM_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("signal", signal))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
