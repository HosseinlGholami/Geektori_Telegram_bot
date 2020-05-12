from telegram.ext import (Updater, InlineQueryHandler,Filters,
                          CommandHandler ,ConversationHandler,MessageHandler)

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)


INSERT_BUY_ID, MAKE_SURE, PHOTO_RECIVING = range(3)



def start(update, context):
    txt="Hello " + update.effective_chat.first_name + "\nYou are talking to Geektori team \n,if you bought استیکر طرح دلخواه , pleas insert your Buy-ID?" 
    update.message.reply_text(txt)
    return INSERT_BUY_ID


def InsertBuyID(update, context):
    reply_keyboard = [["Yes","No"]]
    user = update.message.from_user
    txt='Are you sure   -'+ update.message.text + '-    is your Buy-ID'
    update.message.reply_text(txt,
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
   
    logger.info("Buy-ID %s: %s", user.first_name, update.message.text)
    return MAKE_SURE

def MakeSure(update, context):
    user = update.message.from_user
    txt="Now Please Send Your Picture , the better way is to send it as file "
    logger.info(" %s is  %s ,sure", user.first_name, update.message.text)
    update.message.reply_text(txt, reply_markup=ReplyKeyboardRemove() )
    return PHOTO_RECIVING


    
def PhotoFileReciving(update, context):
    try:
        obj=context.bot.getFile(file_id=update.message.document.file_id)
        obj.download(update.effective_chat.first_name +'.png')
        update.message.reply_text('Thanks for Sending me this picture, we will prepare and send it ASP ')
    except Exception as e:
        print(str(e))
    return ConversationHandler.END

def PhotoReciving(update, context):
    try:
        print("mamad ")
        photo_file = update.message.photo[-1].get_file()
        photo_file.download(update.effective_chat.first_name +'.png')
        update.message.reply_text('Thanks for Sending me this picture, we will prepare and send it ASP ')
    except Exception as e:
        print(str(e))
    return ConversationHandler.END



def cancel(update, context):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END




def han(update , context):
    han=''
    context.bot.send_message(chat_id=update.effective_chat.id,text=dir(han))




def main():
    Geektori_bot_token='1251228456:AAGiftOnmBKgC4GlPHRNzkssaTD1XTVOGBY'
    updater = Updater(Geektori_bot_token, use_context=True)
        # Get the dispatcher to register handlers
    dp = updater.dispatcher


# Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            INSERT_BUY_ID: [MessageHandler(Filters.text, InsertBuyID)],

            MAKE_SURE:[MessageHandler(Filters.regex('^(Yes|No)$'), MakeSure)] ,

            PHOTO_RECIVING: [
                MessageHandler(filters=Filters.document, callback=PhotoFileReciving,
                             pass_chat_data=True,pass_user_data= True),
                MessageHandler(filters=Filters.photo, callback=PhotoReciving,
                             pass_chat_data=True,pass_user_data= True),
                CommandHandler('cancel', cancel)
                ]

        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    
    
    # dp.add_handler(MessageHandler(filters=Filters.photo, callback=han,
    #                          pass_chat_data=True,pass_user_data= True)
    #                          )
    dp.add_handler(conv_handler)

    # log all errors
    dp.add_error_handler(error)
    # Start the Bot
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

import logging
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

if __name__ == '__main__':
    main()



























# import requests
# import re


# def get_url():
#     contents = requests.get('https://random.dog/woof.json').json()    
#     url = contents['url']
#     return url

# def get_image_url():
#     allowed_extension = ['jpg','jpeg','png']
#     file_extension = ''
#     while file_extension not in allowed_extension:
#         url = get_url()
#         file_extension = re.search("([^.]*)$",url).group(1).lower()
#     return url

# def bop(bot, update):
#     url = get_image_url()
#     chat_id = update.message.chat_id
#     bot.send_photo(chat_id=chat_id, photo=url)
#     print("\n\n\n\n")









