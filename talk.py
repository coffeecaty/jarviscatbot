#!/usr/bin/env python
# -*- coding: utf-8 -*-
from logprint import log
import user_date
import helpdoc
import user_command

def talk(bot, update):
    log(update)
    if '喜欢' in update.message.text or 'love' in update.message.text or '爱' in update.message.text:
        if user_date.love.user_list.inornot(update.message.from_user.id):
            bot.sendMessage(update.message.chat_id, text='小猫也爱大熊！最爱大熊了！！',
                            reply_to_message_id=update.message.message_id)
            bot.sendMessage(
                user_date.me.user_list.list[0],
                text=update.message.text)
        elif user_date.me.user_list.inornot(update.message.from_user.id):
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
                helpdoc.help(bot, update, [n.name])
                return
        if 'timer' in update.message.text:
            helpdoc.help(bot, update, ['timer'])
        else:
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
        if user_date.me.user_list.inornot(update.message.from_user.id):
            bot.sendMessage(
                user_date.love.user_list.list[0],
                text=update.message.text)
        elif user_date.love.user_list.inornot(update.message.from_user.id):
            bot.sendMessage(
                user_date.me.user_list.list[0],
                text=update.message.text)
        else:
            bot.sendMessage(
                update.message.chat_id,
                text='小猫听不懂你在说什么，小猫只会爱大熊！如果你想给coffeecaty或者summyxy留言，请使用/stc（say to coffeecaty）或者/sts（say to summyxy）',
                reply_to_message_id=update.message.message_id)
