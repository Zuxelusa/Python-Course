from telegram import Update, ForceReply
from telegram.ext import CallbackContext

from handlers.player_profile import PLAYER_NAME_STATE


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    print(f"{user.full_name} подключился!")
    update.message.reply_text(f"Привет, {user.full_name}!\nСписок команд:\n/player_profile")

def player_profile_command(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("Введите имя: ")

    return PLAYER_NAME_STATE
