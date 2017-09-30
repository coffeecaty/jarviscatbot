#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
import base
import love
import timer


def main():
    try:
       import config
    except ImportExcept:
       print('no config file')
       import sys
       sys.exit(0)
       config.token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    # from base
    dp.add_handler(CommandHandler("start", base.start))
    dp.add_handler(CommandHandler("help", base.help))
    dp.add_handler(CommandHandler("miao", base.miao))
    dp.add_handler(MessageHandler([Filters.text], base.message))
    dp.add_handler(CommandHandler("stc", base.stc))
    dp.add_handler(CommandHandler("sts", base.sts))

    # from love
    dp.add_handler(CommandHandler("love", love.love))
    dp.add_handler(CommandHandler("喜欢你", love.love))
    dp.add_handler(CommandHandler("我爱你", love.love))
    dp.add_handler(CommandHandler("爱你", love.love))
    dp.add_handler(CommandHandler("好喜欢你", love.love))

    # from timer
    dp.add_handler(CommandHandler("set", timer.set,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))
    dp.add_handler(CommandHandler("unset", timer.unset, pass_chat_data=True))
    


    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
