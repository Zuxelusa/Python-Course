import logging
from telegram import *
from telegram.ext import CallbackContext
from data_man import read_data_init
from handlers.handlers import OP_BUTTON_STATE, data


def start_command(update: Update, context: CallbackContext) -> int:
    logging.info(f"{update.effective_user.full_name} запустил команду start")
    read_data_init(update.effective_user.id, data)
    kb = [
        ["Операции с R числами"],
        ["Операции с C числами"],
    ]
    kb_reply_markup = ReplyKeyboardMarkup(kb, one_time_keyboard=True)
    update.message.reply_text("Выберите действие", reply_markup=kb_reply_markup)
    return OP_BUTTON_STATE
