from telegram.ext import Updater, CommandHandler

def start(bot, update):
    update.message.reply_text('您好，我是summy专属的JarvisCat，我会代替coffeecaty对summy进行全方位照顾，如果你不是summy本人...你想看他俩秀恩爱我也没意见啊～～～～')

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))
def alarm(bot, job):
    """Function to send the alarm message"""
    bot.send_message(job.context, text='小熊起床啦！！！！～')


def set(bot, update, args, job_queue, chat_data):
    """Adds a job to the queue"""
    chat_id = update.message.chat_id
    try:
        # args[0] should contain the time for the timer in seconds
        due = int(args[0])
        if due < 0:
            update.message.reply_text('大猫慢慢，不是闪电侠，不能穿越时光。')
            return

        # Add job to queue
        job = job_queue.run_once(alarm, due, context=chat_id)
        chat_data['job'] = job

        update.message.reply_text('好的大熊，没问题大熊！')

    except (IndexError, ValueError):
        update.message.reply_text('请用/set 时间（秒）设置闹钟喵。')


def unset(bot, update, chat_data):
    """Removes the job if the user changed their mind"""

    if 'job' not in chat_data:
        update.message.reply_text('诶？你有让我叫你吗？？？')
        return

    job = chat_data['job']
    job.schedule_removal()
    del chat_data['job']

    update.message.reply_text('好的大熊！，你继续睡吧')


updater = Updater('465976826:AAGh1cIXxirgmsc9Wi6fb-4LrISRWCdkTzI')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('set', set))
updater.dispatcher.add_handler(CommandHandler('unset', unset))

updater.start_polling()
updater.idle()
