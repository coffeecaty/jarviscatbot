#!/usr/bin/env python
# -*- coding: utf-8 -*-


from telegram.ext import Updater, CommandHandler, Job
import logging
import timer
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    
    update.message.reply_text('您好，我是summy专属的JarvisCat，我会代替coffeecaty对summy进行全方位照顾，如果你不是summy本人...你想看他俩秀恩爱我也没意见啊～～～～')

def help(bot, update):
    import helptest
    update.message.reply_text(helptest.help)

def miao(bot, update):
    
    update.message.reply_text('喵？')
    
def love(bot, update):
    
    update.message.reply_text('我也爱大熊！')
def unknow(bot,update):
    bot.sendMessage(update.message.chat_id, text='小猫虽然听不懂你在说什么，但是我爱大熊！', reply_to_message_id=update.message.message_id)


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))


def main():
    try:
       import config
    except ImportExcept:
       print('no config file')
       import sys
       sys.exit(0)
    updater = Updater(config.token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("miao", miao))
    dp.add_handler(CommandHandler("love", love))
    dp.add_handler(CommandHandler("喜欢你", love))
    dp.add_handler(CommandHandler("我爱你", love))
    dp.add_handler(CommandHandler("爱你", love))
    dp.add_handler(CommandHandler("好喜欢你", love))
    dp.add_handler(CommandHandler("set", timer.set,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))
    dp.add_handler(CommandHandler("unset", timer.unset, pass_chat_data=True))
    dp.add_handler(MessageHandler([Filters.text], unknow))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
