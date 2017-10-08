#!/usr/bin/env python
# -*- coding: utf-8 -*-
from logprint import log
from decorator import al_in
import user_date
import config

def iamcat(bot,update):
    if update.message.from_user.username == config.keyuser:
        user_date.me.add(update.message.chat_id)
        user_date.superadmin(update.message.chat_id)
        user_date.allgroup.add(update.message.chat_id)
        update.message.reply_text('欢迎回来，我的大猫~0w0')
    else:
        update.message.reply_text('小猫可不傻，你根本不是大猫哼哼哼~0w0')

@al_in(user_date.me)
def backup(bot,update):
    user_date.backup()
    update.message.reply_text('资料已经备份完毕，小猫是要休息了吗？0w0')

@al_in(user_date.me)
def recover(bot,update,args):
    if args[0]==config.keyuser:
        user_date.recover()
        update.message.reply_text('资料已经恢复完毕，有饼干吃吗？0w0')
    else:
        update.message.reply_text('资料恢复事关重大，请输入正确的执行密码执行。0w0')

def print(bot,update,args):
    for n in user_date.for_group:
       try:
        if args[0]==n.name and n.admin.user_list.inornot(update.message.chat_id):
            update.message.reply_text(n.print(args[1]))
            return
       except TypeError:
           update.message.reply_text('请好好输入你打印的列表种类？0w0')
    update.message.reply_text('喵？并没有你说的这种模块块哦？0w0')
