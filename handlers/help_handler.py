import telebot

def help_command(message):
    help_text = """
    Available Commands:
    /start - Welcome message
    /help - List available commands
    /stats - Show upload statistics
    /broadcast - Broadcast messages to users
    /ban @username duration - Ban a user from uploading files
    """
    bot.reply_to(message, help_text)
