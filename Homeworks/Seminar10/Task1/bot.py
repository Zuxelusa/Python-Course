from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler

from commands import start_command
from get_token import get_telegram_token
from handlers.handlers import *
import logging

logging.basicConfig(level=logging.INFO, filename=f"{__name__}.log", filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s")
logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")

TOKEN = get_telegram_token()

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram

    calc_conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start_command)],
        states={
            OP_BUTTON_STATE: [MessageHandler(Filters.regex(r"R|C"), op_select_handler)],
            NUM_A_STATE: [CallbackQueryHandler(num_a_input)],
            NUM_B_STATE: [MessageHandler(Filters.text, num_b_input)],
            RESULT_STATE: [MessageHandler(Filters.text, result_output)],
        },
        fallbacks=[],
    )
    dispatcher.add_handler(calc_conv_handler)

    # Start the Bot
    updater.start_polling()
    print("BOT STARTED")
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.

    updater.idle()

if __name__ == '__main__':
    main()

