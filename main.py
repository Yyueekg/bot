import os
import telebot

TOKEN = os.getenv("7080303366:AAFLr96fKgd_V-kLwP8NRd8b4F1Ucv9wvS4")
print("TOKEN IS:", TOKEN)  # ← هذا مؤقتًا لنتأكد في الـ logs

bot = telebot.TeleBot(TOKEN)

# مثال:
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك!")

bot.polling()
