import logging

from t_bot.handlers import *

def start_command(update: Update, context: CallbackContext):
    logging.info(f"{update.effective_user.full_name} запустил команду start")
    update.message.reply_text(menu())
    print("тест комманд")
    return 1
