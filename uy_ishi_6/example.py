from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext

# States for the conversation
NAME, SURNAME, AGE, STUDY_PLACE, DISPLAY_INFO = range(5)

def start(update: Update, _: CallbackContext) -> int:
    update.message.reply_text("Hi there! Let's start. What's your name?")
    return NAME

def get_name(update: Update, _: CallbackContext) -> int:
    context = _.user_data
    context['name'] = update.message.text
    update.message.reply_text(f"Great! Hi, {context['name']}! What's your surname?")
    return SURNAME

def get_surname(update: Update, _: CallbackContext) -> int:
    context = _.user_data
    context['surname'] = update.message.text
    update.message.reply_text("Got it! How old are you?")
    return AGE

def get_age(update: Update, _: CallbackContext) -> int:
    context = _.user_data
    context['age'] = update.message.text
    update.message.reply_text("Nice! Where do you study?")
    return STUDY_PLACE

def get_study_place(update: Update, _: CallbackContext) -> int:
    context = _.user_data
    context['study_place'] = update.message.text
    update.message.reply_text("Thanks! Here's the information you provided:\n"
                              f"Name: {context['name']}\n"
                              f"Surname: {context['surname']}\n"
                              f"Age: {context['age']}\n"
                              f"Study Place: {context['study_place']}\n"
                              "Have a great day!")

    # Clear user_data after the conversation is finished
    _.user_data.clear()
    return ConversationHandler.END

def cancel(update: Update, _: CallbackContext) -> int:
    update.message.reply_text("Conversation canceled. Goodbye!")
    # Clear user_data after the conversation is canceled
    _.user_data.clear()
    return ConversationHandler.END

def main():
    # Replace 'YOUR_TOKEN' with your actual bot token
    updater = Updater("6054349441:AAFgiuGOxGJIKmPb4ZeX8bACM-nyIjWqRho")
    dispatcher = updater.dispatcher

    # Create the conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            NAME: [MessageHandler(Filters.text & ~Filters.command, get_name)],
            SURNAME: [MessageHandler(Filters.text & ~Filters.command, get_surname)],
            AGE: [MessageHandler(Filters.text & ~Filters.command, get_age)],
            STUDY_PLACE: [MessageHandler(Filters.text & ~Filters.command, get_study_place)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
