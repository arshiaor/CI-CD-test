from telegram import *
from telegram.ext import *
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from queue import Queue

ADMIN_ID = 861322139  # Replace with real admin chat ID
PSEUDO_ADMIN_ID = 987654321  # Replace with real pseudo admin chat ID

bot = telegram.Bot(token='6793190047:AAHUarBmSzZLHwtkMqBpIUDWdZWTdZf3lj4')


def start(update, context):
    user_id = update.message.chat_id
    if user_id == ADMIN_ID:
        keyboard = [[InlineKeyboardButton("Command 1", callback_data='command1')],
                    [InlineKeyboardButton("Command 2", callback_data='command2')]]
    elif user_id == PSEUDO_ADMIN_ID:
        keyboard = [[InlineKeyboardButton("Command 1", callback_data='command1')]]
    else:
        update.message.reply_text("Sorry you are not authorized to use this bot.")
        return

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)


def button(update, context):
    query = update.callback_query
    if query.data == 'command1':
        bot.send_message(chat_id=query.message.chat_id, text="Executing Command 1")
    elif query.data == 'command2':
        bot.send_message(chat_id=query.message.chat_id, text="Executing Command 2")


def main():
    updater = Updater('6793190047:AAHUarBmSzZLHwtkMqBpIUDWdZWTdZf3lj4',Queue())

    # Create dispatcher and add handlers
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))

    # Start polling
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()