#!/usr/bin/env python
# -*- coding: utf-8 -*-
from logprint import log
from datetime import timedelta
import user_date

def start(bot, update):
    log(update)
    if user_date.me.user_list.inornot(update.message.chat_id):
        update.message.reply_text('欢迎回来，我的大猫~0w0')
    elif user_date.love.user_list.inornot(update.message.chat_id):
        update.message.reply_text('你好，我最爱的summy，我是你的专属小猫，我会辅助coffeecaty照顾你，说出你的需求，我会尽量满足。小猫还小，会的很少，请有耐心的慢慢教小猫长大哦~')
    else:
        if update.message.first_name is not None:
            update.message.reply_text(
                '您好，' + update.message.from_user.first_name + '，我是辅助coffeecaty照顾summy的专属小猫，虽然也提供一些其他服务，但基本上你通过我只能...看caty秀恩爱啊~~~')
        else:
            update.message.reply_text(
                '您好，@' + update.message.from_user.username + '，我是辅助coffeecaty照顾summy的专属小猫，虽然也提供一些其他服务，但基本上你通过我只能...看caty秀恩爱啊~~~')

def miao(bot, update):
    log(update)
    update.message.reply_text('喵？')

def stc(bot, update, args):
    log(update)
    if len(args) > 0:
        message = ''
        for n in args:
            message = message + n + ' '
        update.message.reply_text('已成功为您留言给coffeecaty')
        bot.sendMessage(user_date.me.user_list.list[0], text='from:@' + update.message.from_user.username + ':' + message + '(at ' + str(
            update.message.date + timedelta(hours=8)) + 'UTC+8:00)')
    else:
        update.message.reply_text('你怎么比小猫还笨！你都没留言我怎么帮你转达。0w0')


def sts(bot, update, args):
    log(update)
    if len(args) > 0:
        message = ''
        for n in args:
            message = message + n + ' '
        update.message.reply_text('已成功为您留言给summy')
        bot.sendMessage(user_date.love.user_list.list[0],
                        text='from:@' + update.message.from_user.username + ':' + message + '(at ' + str(
                            update.message.date + timedelta(hours=8)) + 'UTC+8:00)')
    else:
        update.message.reply_text('你怎么比小猫还笨！你都没留言我怎么帮你转达。0w0')


def repeat(bot, update, args):
    log(update)
    if len(args) == 0:
        update.message.reply_text('你怎么比小猫还笨！你都没说话我怎么重复。0w0')
    elif len(args) == 1:
        message = args[0] + '\n' + args[0] + '\n' + args[0]
        update.message.reply_text(message)
    else:
        try:
            time = int(args[-1])
            args = args[:-1]
        except (ValueError):
            time = 3
        if time < 1:
            update.message.reply_text('1后面是2，1前面是？（掰猫爪爪')
        else:
            n, text = 1, args[0]
            while n < len(args):
                text = text + ' ' + args[n]
                n = n + 1
            message = text + ('\n' + text) * (time - 1)
            update.message.reply_text(message)

def talk(bot, update):
    log(update)
    if user_date.me.user_list.inornot(update.message.chat_id):
        bot.sendMessage(user_date.love.user_list.list[0], text=update.message.text)
    elif user_date.love.user_list.inornot(update.message.chat_id):
        bot.sendMessage(user_date.me.user_list.list[0], text=update.message.text)
        if '喜欢' in update.message.text or 'love' in update.message.text or '爱' in update.message.text:
            bot.sendMessage(update.message.chat_id, text='小猫也爱大熊！最爱大熊了！！',
                            reply_to_message_id=update.message.message_id)
        else:
            bot.sendMessage(update.message.chat_id, text='小猫虽然听不懂你在说什么，但是小猫爱大熊！小猫会问问大猫怎么回答你的！',reply_to_message_id=update.message.message_id)
    else:
        bot.sendMessage(update.message.chat_id, text='小猫听不懂你在说什么，小猫只会爱大熊！如果你想给coffeecaty或者summyxy留言，请使用/stc（say to coffeecaty）或者/sts（say to summyxy）',
                        reply_to_message_id=update.message.message_id)
