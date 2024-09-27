import telebot
import json

def upload_file(message, channel_id):
    # Check if user wants to add a password
    bot.reply_to(message, "Do you want to add a password? (Y/N)")
    bot.register_next_step_handler(message, process_password_choice, channel_id)

def process_password_choice(message, channel_id):
    if message.text.lower() == 'y':
        bot.reply_to(message, "Please enter your password:")
        bot.register_next_step_handler(message, process_password, channel_id)
    elif message.text.lower() == 'n':
        store_file(message.document.file_id, channel_id)
        bot.reply_to(message, "File uploaded successfully without password.")
    else:
        bot.reply_to(message, "Invalid choice. Please type Y or N.")
        upload_file(message, channel_id)

def process_password(message, channel_id):
    password = message.text
    store_file(message.document.file_id, channel_id, password)
    bot.reply_to(message, "File uploaded successfully with password.")

def store_file(file_id, channel_id, password=None):
    # Logic to store file and password (if provided) to your storage
    pass
