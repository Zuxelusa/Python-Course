import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler
from commands.base import start, player_profile_command
from handlers.player_profile import *

TOKEN = ""

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))

    player_profile_conv_handler = ConversationHandler(
        entry_points=[CommandHandler('player_profile', player_profile_command)],
        states={
            PLAYER_NAME_STATE: [MessageHandler(Filters.text, input_player_name_handler)],
            PLAYER_AGE_STATE: [MessageHandler(Filters.text, input_player_age_handler)],
            PLAYER_GENDER_STATE: [MessageHandler(Filters.text, input_player_gender_handler)]
        },
        fallbacks=[],
    )
    dispatcher.add_handler(player_profile_conv_handler)

    # dispatcher.add_handler(MessageHandler(Filters.text, input_player_name_handler))
    # dispatcher.add_handler(MessageHandler(Filters.text, input_player_age_handler))

    # # on non command i.e message - echo the message on Telegram
    # dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()
    print("BOT STARTED")
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.

    updater.idle()

if __name__ == '__main__':
    main()
