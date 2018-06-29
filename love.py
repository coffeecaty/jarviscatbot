#!/usr/bin/env python
# -*- coding: utf-8 -*-

from logprint import log
import config,user_date

def missingyou(bot, job):
    """Function to send the alarm message"""
    bot.send_message(job.context, text='大熊大熊，你都好久没理我啦T T，配小猫玩好不好好不好好不好～')
    bot.sendMessage(user_date.alluser.chat_id('@'+config.keyuser),'报告大猫,我撩了一下小熊0.0')



def reset(bot, update, job_queue, user_data):
    """Adds a job to the queue"""
    try:
        chat_id = user_date.love.user_list.list[0]
    except IndexError:
        return
    if 'alone' not in user_data:
        continue
    else:
        alone = user_data['alone']
        alone.schedule_removal()
        del user_data['alone']
        time=24*3600
        # Add job to queue
        alone = job_queue.run_once(missingyou, time, context=chat_id)
                user_data['job'] = job

                update.message.reply_text('好的大熊，没问题大熊！')


def untimer(bot, update, user_data):
    """Removes the job if the user changed their mind"""
    log(update)
    if 'job' not in user_data:
        update.message.reply_text('诶？你有让我叫你吗？？？')
        return

    job = user_data['job']
    job.schedule_removal()
    del user_data['job']

    update.message.reply_text('好的大熊！你继续睡吧')
