import telebot
import os

TOKEN = os.getenv("7764820620:AAE9_mad9CaCiQfpnUKGQgKcKeLjOiuS2_Y")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "أهلاً بك!")

bot.polling()
