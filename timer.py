from telegram.ext import Updater, Job
from logprint import log

    
def alarm(bot, job):
    """Function to send the alarm message"""
    bot.send_message(job.context, text='小熊起床啦！！！！～')


def set(bot, update, args, job_queue, chat_data):
    """Adds a job to the queue"""
    log(update)
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
    log(update)
    if 'job' not in chat_data:
        update.message.reply_text('诶？你有让我叫你吗？？？')
        return

    job = chat_data['job']
    job.schedule_removal()
    del chat_data['job']

    update.message.reply_text('好的大熊！你继续睡吧')



