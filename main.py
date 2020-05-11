from telegram.ext import (Updater, InlineQueryHandler,Filters,
                          CommandHandler ,ConversationHandler,MessageHandler)

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)


GENDER, PHOTO, LOCATION, BIO = range(4)


def start(update, context):
    reply_keyboard = [['آره', 'نه']]
    txt="سلام این بات گیکتوری عه ، ما از احمد یه درخاست داریم نظر شما چیه ؟ "
    update.message.reply_text(txt,
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return GENDER


def gender(update, context):
    user = update.message.from_user
    txt="نظر شما هم محترمه ،یه عکس از این آقا احمد برا ما میفرستید ؟ اگر نه که /skip  بزنیم دیگه"
    logger.info("Gender of %s: %s", user.first_name, update.message.text)
    update.message.reply_text(txt, reply_markup=ReplyKeyboardRemove() )

    return PHOTO


def photo(update, context):
    user = update.message.from_user
    photo_file = update.message.photo[-1].get_file()
    photo_file.download(user.first_name +'.jpg')
    logger.info("Photo of %s: %s", user.first_name, 'user_photo.jpg')
    update.message.reply_text('جووووون جه جیگری هستی تو ، حالا یه لوکیشت بده ببینم کچایی اگر تمیدی هم  /skip کن')

    return LOCATION


def skip_photo(update, context):
    user = update.message.from_user
    logger.info("User %s did not send a photo.", user.first_name)
    update.message.reply_text('من شرط میبندم خوب چیزی هستی ، ولی حالا چس کن عکس نده ، یه لوکیشن بده ببینم کوجایی ؟/skip.')

    return LOCATION


def location(update, context):
    user = update.message.from_user
    user_location = update.message.location
    logger.info("Location of %s: %f / %f", user.first_name, user_location.latitude,
                user_location.longitude)
    update.message.reply_text('جوووون تکون نخور الان میام خدمتت ، یه جمله بکو یادگاری به ذهنم بسپارم ')

    return BIO


def skip_location(update, context):
    user = update.message.from_user
    logger.info("User %s did not send a location.", user.first_name)
    update.message.reply_text('شما از چیه ما میترسی که لوکیشن نمیدی بهمون ؟ ، یه جمله بکو یادگاری به ذهنم بسپارم')

    return BIO


def bio(update, context):
    user = update.message.from_user
    logger.info("Bio of %s: %s", user.first_name, update.message.text)
    update.message.reply_text('جوووون تشکر از شما ، برای دادن این اطلاعات مفیدتون ')

    return ConversationHandler.END


def cancel(update, context):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

    

def main():
    Geektori_bot_token='1251228456:AAGiftOnmBKgC4GlPHRNzkssaTD1XTVOGBY'
    updater = Updater(Geektori_bot_token, use_context=True)
        # Get the dispatcher to register handlers
    dp = updater.dispatcher


# Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            GENDER: [MessageHandler(Filters.regex('^(نه|آره)$'), gender)],

            PHOTO: [MessageHandler(Filters.photo, photo),
                    CommandHandler('skip', skip_photo)],

            LOCATION: [MessageHandler(Filters.location, location),
                       CommandHandler('skip', skip_location)],

            BIO: [MessageHandler(Filters.text, bio)]
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

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



























import requests
import re


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def bop(bot, update):
    url = get_image_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    print("\n\n\n\n")









