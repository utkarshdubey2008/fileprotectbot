
import telebot

def start_command(bot, message):
    welcome_message = "Welcome to the File Store Bot! 📁\n\n" \
                      "Use /help to see available commands."
    bot.reply_to(message, welcome_message)
