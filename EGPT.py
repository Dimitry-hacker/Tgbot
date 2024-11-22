import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import google.generativeai as genai

# Настройка Google Gemini
genai.configure(api_key="AIzaSyDLbWp7CH8dsMSBBZ5ZSeP98AwQtUUJfds")  # Замените на ваш API-ключ
model = genai.GenerativeModel("gemini-1.5-flash")

# Логирование
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Функция для команды /gemini
async def gemini_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Получаем текст от пользователя после команды
        user_input = " ".join(context.args)
        if not user_input:
            await update.message.reply_text("Salom men EGPT 2.0 Savolngiz bolsa yozing!")
            return

        # Отправляем запрос в Google Gemini
        response = model.generate_content(user_input)

        # Отправляем результат пользователю
        await update.message.reply_text(response.text)
    except Exception as e:
        logger.error(f"Ошибка при обработке команды /gemini: {e}")
        await update.message.reply_text("Произошла ошибка при запросе к Google Gemini.")

# Основная функция запуска бота
def main():
    # Ваш Telegram API токен
    TELEGRAM_API_TOKEN = "7772081707:AAGvbdjIpw7SGdVrCzBnFIp9l9cCwx-paTU"  # Замените на ваш токен

    # Создаем приложение
    application = ApplicationBuilder().token(TELEGRAM_API_TOKEN).build()

    # Добавляем обработчик команды /gemini
    application.add_handler(CommandHandler("gemini", gemini_command))

    # Запускаем бота
    application.run_polling()

if __name__ == "__main__":
    main()
