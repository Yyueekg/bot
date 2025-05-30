import telebot
import os

TOKEN = os.getenv("7080303366:AAFLr96fKgd_V-kLwP8NRd8b4F1Ucv9wvS4")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "أهلاً بك!")

bot.polling()
