import logging

from telegram import *
from telegram.ext import CallbackContext, ConversationHandler
from data_man import save_data


(
    OP_BUTTON_STATE,
    NUM_A_STATE,
    NUM_B_STATE,
    RESULT_STATE
) = range(4)

data = {
    "user_name": "",
    "num_a": 0,
    "num_b": 0,
    "op": "",
    "num_type": float
}


def op_select_handler(update: Update, context: CallbackContext):
    text = update.message.text
    if "R" in text:
        data["num_type"] = float
    elif "C" in text:
        data["num_type"] = complex
    save_data(update.effective_user.id, data)
    logging.info(f"{update.effective_user.full_name} выбрал тип данных {data['num_type']}.")

    ops = [
        [InlineKeyboardButton("a + b", callback_data="+")], [InlineKeyboardButton("a * b", callback_data="*")],
        [InlineKeyboardButton("a - b", callback_data="-")], [InlineKeyboardButton("a / b", callback_data="/")],
    ]

    kb_inline = InlineKeyboardMarkup(ops)
    update.message.reply_text("Выберите операцию ", reply_markup=kb_inline)
    return NUM_A_STATE


def num_a_input(update: Update, context: CallbackContext) -> None:
    # data = read_data(update.effective_user.id)
    text = update.callback_query.data
    logging.info(f"{update.effective_user.full_name} выбрал операцию {text}.")
    data["op"] = text
    save_data(update.effective_user.id, data)
    update.callback_query.message.edit_text("Введите число a ")
    return NUM_B_STATE


def num_b_input(update: Update, context: CallbackContext) -> None:
    # data = read_data(update.effective_user.id)
    text = update.message.text
    data["num_a"] = data["num_type"](text)
    save_data(update.effective_user.id, data)
    logging.info(f"{update.effective_user.full_name} ввел значение для А {text}.")
    update.message.reply_text("Введите число b ")
    return RESULT_STATE


def result_output(update: Update, context: CallbackContext) -> int:
    # data = read_data(update.effective_user.id)
    text = update.message.text
    data["num_b"] = data["num_type"](text)
    save_data(update.effective_user.id, data)
    logging.info(f"{update.effective_user.full_name} ввел значение для B {text}.")
    num_a = data["num_a"]
    num_b = data["num_b"]
    data['result'] = str(eval(f"{num_a} {data['op']} {num_b}"))
    logging.info(f"{update.effective_user.full_name} получил результат {data['result']}.")
    update.message.reply_text(data['result'])
    return ConversationHandler.END
