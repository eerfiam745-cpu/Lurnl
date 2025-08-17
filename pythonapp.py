import os
import telebot

API_TOKEN = os.getenv('8015402761:AAE7otsbjkfNJd6g07eFqFiWPHh_NvvkSBk')  # Read token from environment
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
use /stripe to check\
""")

if __name__ == '__main__':
    print("Bot is running!")
    bot.infinity_polling()
