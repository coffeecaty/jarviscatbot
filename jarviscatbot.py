#!/usr/bin/env python
# -*- coding: utf-8 -*-


from telegram.ext import Updater, CommandHandler, Job
import logging

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
    
def alarm(bot, job):
    """Function to send the alarm message"""
    bot.send_message(job.context, text='小熊起床啦！！！！～')


def set(bot, update, args, job_queue, chat_data):
    """Adds a job to the queue"""
    chat_id = update.message.chat_id
    try:
        # args[0] should contain the time for the timer in seconds
        while len(args)<4:
            args.append('0')
        due = int(args[0])+60*(int(args[1])+60*(int(args[2])+24*int(args[3])))
        if due < 0:
            update.message.reply_text('大猫慢慢，不是闪电侠，不能穿越时光。')
            return

        # Add job to queue
        job = job_queue.run_once(alarm, due, context=chat_id)
        chat_data['job'] = job

        update.message.reply_text('好的大熊，没问题大熊！')

    except (IndexError, ValueError):
        update.message.reply_text('请用/set 设置时间（秒 分 时 天，以空格分隔，可有后向前缺省）')


def unset(bot, update, chat_data):
    """Removes the job if the user changed their mind"""

    if 'job' not in chat_data:
        update.message.reply_text('诶？你有让我叫你吗？？？')
        return

    job = chat_data['job']
    job.schedule_removal()
    del chat_data['job']

    update.message.reply_text('好的大熊！你继续睡吧')


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
    dp.add_handler(CommandHandler("set", set,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))
    dp.add_handler(CommandHandler("unset", unset, pass_chat_data=True))

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
