import os
import telebot
from stripe import stripe_payment  # Ensure this module exists locally

API_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')  # Read token from environment
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['stripe'])
def handle_stripe(message):
    stripe_payment(message, bot)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
use /stripe to check\
""")

if __name__ == '__main__':
    print("Bot is running!")
    bot.infinity_polling()
