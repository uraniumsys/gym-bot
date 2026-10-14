import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get('BOT_TOKEN')
APP_URL = 'https://gym-mini-app-six.vercel.app'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🌐 Открыть приложение", web_app={'url': APP_URL})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        'Добро пожаловать в gym***\n\n'
        'Здесь ты найдёшь:\n'
        '• Программы тренировок\n'
        '• Отслеживание прогресса\n'
        '• AI-советы по технике\n\n'
        'Нажми кнопку ниже, чтобы начать 👇',
        reply_markup=reply_markup
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Используй кнопку "Открыть приложение" для доступа к тренировкам.\n\n'
        'Если есть вопросы — пиши!'
    )

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
