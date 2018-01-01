#!/usr/bin/env python
# -*- coding: utf-8 -*-
from logprint import log
import user_date
import helpdoc
import user_command
import re
from datetime import timedelta
import base

def orsearch(keywords,text):
    for word in keywords:
        if re.search('.*'+word+'.*',text,re.I|re.M|re.S):
            return True
    return False


def talk(bot, update):
    log(update)
    if orsearch(['备份.*资料'],update.message.text):
        user_command.backup(bot,update)
    elif orsearch(['love','爱','喜欢'],update.message.text):
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
    elif orsearch(['使用.*帮助'],update.message.text):
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
    elif orsearch(['申请.*权限'],update.message.text):
        bot.sendMessage(update.message.chat_id, text='小猫正在替你发送你的申请，不要着急哦',
                        reply_to_message_id=update.message.message_id)
        for n in user_date.for_group:
            if n.name in update.message.text:
                user_command.apply(bot, update, [n.name])
    elif orsearch(['屏蔽.*消息'],update.message.text):
        bot.sendMessage(update.message.chat_id, text='小猫正在替你处理你的要求，不要着急哦',
                        reply_to_message_id=update.message.message_id)
        for n in user_date.for_group:
            if n.name in update.message.text:
                user_command.mute(bot, update, [n.name])
    elif orsearch(['解除.*屏蔽'],update.message.text):
        bot.sendMessage(update.message.chat_id, text='小猫正在替你处理你的要求，不要着急哦',
                        reply_to_message_id=update.message.message_id)
        for n in user_date.for_group:
            if n.name in update.message.text:
                user_command.unmute(bot, update, [n.name])
    elif orsearch(['调戏'],update.message.text):
        bot.sendMessage(update.message.chat_id, text='调戏小猫小心被小猫咬死哦V_V',
                        reply_to_message_id=update.message.message_id)
    elif update.message.reply_to_message is not None:
        if orsearch(['向您申请使用.*模块的使用权限.*'],update.message.reply_to_message.text) and update.message.chat_id==update.message.from_user.id:
            result=re.search(r'(.*)向您申请使用(.*)模块的使用权限.*',update.message.reply_to_message.text)
            user=result.group(1)
            modname=result.group(2)
            for mod in user_date.for_group:
                if mod.name==modname and (mod.name is not 'alluser'):
                    group=mod
                    break
            if orsearch(['yes','agree','同意'],update.message.text):
                user_command.add(bot,update,[group.name,user])
            elif orsearch(['no','refuse','拒绝'],update.message.text):
                user_command.apply_refuse(bot,update,[group.name,user])
            elif update.message.date<update.message.reply_to_message.date+timedelta(hours=24):
                    bot.sendMessage(user_date.alluser.chat_id(user), text='来自'+group.name+'管理员 @'+update.message.from_user.username+' 的留言:'+update.message.text)
                    update.message.reply_text('已向 '+user+' 转达留言')
            else:
                update.message.reply_text('小猫无法识别您的操作喵！')
        if orsearch(['from @.*at .*UTC'],update.message.reply_to_message.text):
            result = re.search(r'.*from (.*):.*at.*', update.message.reply_to_message.text,re.S)
            user=result.group(1)
            if user_date.me.user_list.inornot(update.message.from_user.id) or user_date.love.user_list.inornot(update.message.from_user.id):
                user_command.message(bot,update,[user,':',update.message.text])
            elif user_date.me.user_list.inornot(user_date.alluser.chat_id(user)):
                base.stc(bot,update,[update.message.text])
            elif user_date.love.user_list.inornot(user_date.alluser.chat_id(user)):
                base.sts(bot,update,[update.message.text])
            else:
                update.message.reply_text('小猫无法识别您的操作喵！')
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
