#!/usr/bin/env python
# -*- coding: utf-8 -*-

from logprint import log


def alarm(bot, job):
    """Function to send the alarm message"""
    bot.send_message(job.context, text='大熊起床啦！')


def timer(bot, update, args, job_queue, user_data):
    """Adds a job to the queue"""
    log(update)
    chat_id = update.message.from_user.id
    if len(args) == 0:
        update.message.reply_text('请用正确的格式设置提醒参数，具体请参考/help timer）')
    else:
        try:
                # args[0] should contain the time for the timer in seconds
                while len(args) < 4:
                    args.append('0')
                due = int(args[0]) + 60 * (int(args[1]) + 60 *
                                           (int(args[2]) + 24 * int(args[3])))
                if due < 0:
                    update.message.reply_text('小猫慢慢，不是闪电侠，不能穿越时光。')
                    return

                # Add job to queue
                job = job_queue.run_once(alarm, due, context=chat_id)
                user_data['job'] = job

                update.message.reply_text('好的大熊，没问题大熊！')

        except (ValueError):
            update.message.reply_text('请用/set 设置时间（秒 分 时 天，以空格分隔，可由后向前缺省）')


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
