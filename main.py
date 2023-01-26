import logging
from telegram.ext import Application, MessageHandler, filters
from handlers import save_pic, save_voice, save_audio

import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

def main():

    app = Application.builder().token(settings.API_KEY).build()

    app.add_handler(MessageHandler(filters.PHOTO, save_pic))
    app.add_handler(MessageHandler(filters.VOICE, save_voice))
    app.add_handler(MessageHandler(filters.AUDIO, save_audio))
    

    logging.info("Бот стартовал")

    app.run_polling()

if __name__ == '__main__':
    main()