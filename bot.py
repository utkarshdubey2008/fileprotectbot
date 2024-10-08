import telebot
from config import TOKEN, CHANNEL_ID  # Importing credentials from config.py
from plugins.file_management import upload_file
from plugins.user_management import manage_user
from plugins.password_protection import check_password
from plugins.stats import update_stats
from plugins.premium_plans import show_plans
from handlers.start_handler import start_command
from handlers.help_handler import help_command
from handlers.stats_handler import stats_command
from handlers.broadcast_handler import broadcast_command
from handlers.ban_handler import ban_user

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    start_command(bot, message)  # Pass the bot instance

@bot.message_handler(commands=['help'])
def handle_help(message):
    help_command(bot, message)  # Pass the bot instance

@bot.message_handler(commands=['stats'])
def handle_stats(message):
    stats_command(bot, message)  # Pass the bot instance

@bot.message_handler(commands=['broadcast'])
def handle_broadcast(message):
    broadcast_command(bot, message)  # Pass the bot instance

@bot.message_handler(commands=['ban'])
def handle_ban(message):
    ban_user(bot, message)  # Pass the bot instance

@bot.message_handler(content_types=['document'])
def handle_file_upload(message):
    upload_file(message, CHANNEL_ID)

bot.polling()
