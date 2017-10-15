#!/usr/bin/env python
# -*- coding: utf-8 -*-
from logprint import log
from datetime import timedelta
import user_date,helpdoc,user_command


def start(bot, update):
    log(update)
    if user_date.me.user_list.inornot(update.message.chat_id):
        update.message.reply_text('欢迎回来，我的大猫~0w0')
    elif user_date.love.user_list.inornot(update.message.chat_id):
        update.message.reply_text(
            '你好，我最爱的summy，我是你的专属小猫，我会辅助coffeecaty照顾你，说出你的需求，我会尽量满足。小猫还小，会的很少，请有耐心的慢慢教小猫长大哦~')
    else:
        if update.message.from_user.first_name is not None:
            update.message.reply_text(
                '您好，' +
                update.message.from_user.first_name +
                '，我是辅助coffeecaty照顾summy的专属小猫，虽然也提供一些其他服务，但基本上你通过我只能...看caty秀恩爱啊~~~')
        else:
            update.message.reply_text(
                '您好，@' +
                update.message.from_user.username +
                '，我是辅助coffeecaty照顾summy的专属小猫，虽然也提供一些其他服务，但基本上你通过我只能...看caty秀恩爱啊~~~')


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
        bot.sendMessage(
            user_date.me.user_list.list[0],
            text='from:@' +
            update.message.from_user.username +
            ':' +
            message +
            '(at ' +
            str(
                update.message.date +
                timedelta(
                    hours=8)) +
            'UTC+8:00)')
    else:
        update.message.reply_text('你怎么比小猫还笨！你都没留言我怎么帮你转达。0w0')


def sts(bot, update, args):
    log(update)
    if len(args) > 0:
        message = ''
        for n in args:
            message = message + n + ' '
        update.message.reply_text('已成功为您留言给summy')
        bot.sendMessage(
            user_date.love.user_list.list[0],
            text='from:@' +
            update.message.from_user.username +
            ':' +
            message +
            '(at ' +
            str(
                update.message.date +
                timedelta(
                    hours=8)) +
            'UTC+8:00)')
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
    if '喜欢' in update.message.text or 'love' in update.message.text or '爱' in update.message.text:
        if user_date.love.user_list.inornot(update.message.chat_id):
            bot.sendMessage(update.message.chat_id, text='小猫也爱大熊！最爱大熊了！！',
                            reply_to_message_id=update.message.message_id)
            bot.sendMessage(
                user_date.me.user_list.list[0],
                text=update.message.text)
        elif user_date.me.user_list.inornot(update.message.chat_id):
            bot.sendMessage(update.message.chat_id, text='小猫知道大猫最爱大熊了！！',
                            reply_to_message_id=update.message.message_id)
            bot.sendMessage(
                user_date.love.user_list.list[0],
                text=update.message.text)
        else:
            bot.sendMessage(
                update.message.chat_id,
                text='你喜欢谁和小猫我没什么关系，小猫只爱大熊！',
                reply_to_message_id=update.message.message_id)
    elif '使用帮助' in update.message.text:
        bot.sendMessage(update.message.chat_id, text='小猫正在替你寻找使用帮助，不要着急哦',
                        reply_to_message_id=update.message.message_id)
        for n in user_date.date_group:
            if n.name in update.message.text:
                helpdoc.help(bot, update,[n.name])
                return
        helpdoc.help(bot, update, ['base'])
    elif '申请权限' in update.message.text:
        bot.sendMessage(update.message.chat_id, text='小猫正在替你发送你的申请，不要着急哦',
                        reply_to_message_id=update.message.message_id)
        for n in user_date.for_group:
            if n.name in update.message.text:
                user_command.apply(bot, update, [n.name])
    elif '屏蔽消息' in update.message.text:
        bot.sendMessage(update.message.chat_id, text='小猫正在替你处理你的要求，不要着急哦',
                        reply_to_message_id=update.message.message_id)
        for n in user_date.for_group:
            if n.name in update.message.text:
                user_command.mute(bot, update, [n.name])
    elif '解除屏蔽' in update.message.text:
        bot.sendMessage(update.message.chat_id, text='小猫正在替你处理你的要求，不要着急哦',
                        reply_to_message_id=update.message.message_id)
        for n in user_date.for_group:
            if n.name in update.message.text:
                user_command.unmute(bot, update, [n.name])
    elif '调戏' in update.message.text:
        bot.sendMessage(update.message.chat_id, text='调戏小猫小心被小猫咬死哦V_V',
                        reply_to_message_id=update.message.message_id)
    else:
        if user_date.me.user_list.inornot(update.message.chat_id):
            bot.sendMessage(
                user_date.love.user_list.list[0],
                text=update.message.text)
        elif user_date.love.user_list.inornot(update.message.chat_id):
            bot.sendMessage(
                user_date.me.user_list.list[0],
                text=update.message.text)
        else:
            bot.sendMessage(
                update.message.chat_id,
                text='小猫听不懂你在说什么，小猫只会爱大熊！如果你想给coffeecaty或者summyxy留言，请使用/stc（say to coffeecaty）或者/sts（say to summyxy）',
                reply_to_message_id=update.message.message_id)
