#5438059188:AAHWyQXtJ8pi9mlboX2edVjrzqvwiXXoaas
import telebot

token = '5438059188:AAHWyQXtJ8pi9mlboX2edVjrzqvwiXXoaas'

bot = telebot.TeleBot(token, parse_mode=True)

@bot.message_handler(commands=['start', 'help', 'hi'])
def send_welcome(message):
    bot.reply_to(message, 'Привет!')

@bot.message_handler(func=lambda message:True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()