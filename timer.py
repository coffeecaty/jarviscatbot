#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegram.ext import Updater, Job
from logprint import log

    
def alarm(bot, job):
    """Function to send the alarm message"""
    bot.send_message(job.context, text='小熊起床啦！！！！～')


def set(bot, update, args, job_queue, chat_data):
    """Adds a job to the queue"""
    chat_id = update.message.chat_id
    try:
       if len(args)==0:
        update.message.reply_text('请用/set 设置时间（秒 分 时 天，以空格分隔，可由后向前缺省）')  
       else:
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

    except (ValueError):
        update.message.reply_text('请用/set 设置时间（秒 分 时 天，以空格分隔，可由后向前缺省）')


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



