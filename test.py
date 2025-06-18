import telebot

TOKEN = '7583421284:AAGfL-TLKq33z4hhkPdLNcbGdv1PWHZMaKM'
bot = telebot.TeleBot(TOKEN) 

#@bot.message_handler(commands=['start'])
#def send_welcome(message):
#    bot.reply_to(message, "Привет! Я бот Фаёза")
    
#@bot.message_handler(commands=['help'])
#def help_command(message):
#    bot.send_message(message.chat.id, "Вот что я умею:\n/start — запуск\n/help — помощь\n/info — обо мне")
#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
#    bot.reply_to(message, message.text)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я твой бот. Напиши /help для списка команд.")

# Команда /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    help_text = (
        "/start - Запустить бота\n"
        "/help - Показать помощь\n"
        "/info - Информация о боте\n"
        "/about - Обо мне"
    )
    bot.send_message(message.chat.id, help_text)

# Команда /info
@bot.message_handler(commands=['info'])
def handle_info(message):
    bot.send_message(message.chat.id, "Этот бот создан на Python с использованием библиотеки Telebot.")

# Команда /about
@bot.message_handler(commands=['about'])
def handle_about(message):
    bot.send_message(message.chat.id, "Я простой Telegram-бот, который умеет отвечать на команды.")

# Обработка обычных сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, f"Ты написал: {message.text}")

bot.polling()