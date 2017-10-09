#!/usr/bin/env python
# -*- coding: utf-8 -*-

from logprint import log
from decorator import al_in, id
from datetime import timedelta
import user_date,config


def iamcat(bot, update):
    log(update)
    if update.message.from_user.username == config.keyuser:
        user_date.me.add(update.message.chat_id)
        user_date.superadmin.add(update.message.chat_id)
        user_date.allgroup.add(update.message.chat_id)
        update.message.reply_text('欢迎回来，我的大猫~0w0')
    else:
        update.message.reply_text('小猫可不傻，你根本不是大猫哼哼哼~0w0')


@al_in(user_date.me)
def backup(bot, update):
    log(update)
    user_date.backup()
    update.message.reply_text('资料已经备份完毕，小猫是要休息了吗？0w0')


@al_in(user_date.me)
def recover(bot, update, args):
    log(update)
    if args[0] == config.keyuser:
        user_date.recover()
        update.message.reply_text('资料已经恢复完毕，有饼干吃吗？0w0')
    else:
        update.message.reply_text('资料恢复事关重大，请输入正确的执行密码执行。0w0')


def print(bot, update, args):
    log(update)
    for n in user_date.for_group:
        try:
            if args[0] == n.name and n.admin.user_list.inornot(
                    update.message.chat_id):
                update.message.reply_text(n.print(args[1]))
                return
        except TypeError:
            update.message.reply_text('请好好输入你打印的列表种类？0w0')
    update.message.reply_text('喵？并没有你说的这种模块块哦？0w0')


def apply(bot, update, args):
    log(update)
    try:
        for m in args:
            do=0
            for n in user_date.for_group:
                if m == n.name:
                    do=1
                    if n.ban_list.inornot(update.message.chat_id):
                        update.message.reply_text(
                            '喵？您已被管理员封禁' + m + '模块权限，如有疑问请联系模块管理员，小猫可不知道发生了什么哦！0w0')
                    elif n.user_list.inornot(update.message.chat_id):
                        update.message.reply_text(
                            '喵？小猫仔细检查了一下觉得您已经有' + m + '模块的权限了哦！0w0')
                    elif n.apply_list.inornot(update.message.chat_id):
                        update.message.reply_text(
                            '喵？您已提交过' + m + '模块权限，请耐心等候管理员的批准哦~！0w0')
                    else:
                        n.apply(update.message.chat_id)
                        for a in n.admin.user_list.list:
                            if not (user_date.alluser.mute_list.inornot(a) or n.admin.mute_list.inornot(a)):
                                bot.sendMessage(a,text='@'+update.message.from_user.username +'向您申请使用' +m +'模块的使用权限 (at ' +str(update.message.date +timedelta(hours=8)) +'UTC+8:00)')
                        update.message.reply_text(
                            '您的' + m + '模块权限申请小猫我已成功替您提交，请耐心等候管理员的批准哦~！0w0')
                    break
            if not bool(do):
                update.message.reply_text('喵？并没有名叫' + m + '的模块块哦？0w0')
    except TypeError:
        update.message.reply_text('请好好输入你要申请的模块名哦，不然小猫可帮不了你~0w0')


@id
def add(bot, update, tpye, date=[]):
    log(update)
    try:
        for n in user_date.for_group:
            if tpye == n.name and n.admin.user_list.inornot(
                    update.message.chat_id):
                n.add(date)
                update.message.reply_text('用户授权完毕')
                return
            update.message.reply_text('喵？并没有名叫' + type + '的模块块哦？0w0')
    except IndexError:
        update.message.reply_text('请按照‘模块名 用户1 用户2...’的格式好好输入，不然小猫可帮不了你~0w0')


@id
def remove(bot, update, tpye, date):
    log(update)
    try:
        for n in user_date.for_group:
            if tpye == n.name and n.admin.user_list.inornot(
                    update.message.chat_id):
                n.add(date)
                update.message.reply_text('用户移出完毕')
                return
            update.message.reply_text('喵？并没有名叫' + type + '的模块块哦？0w0')
    except TypeError:
        update.message.reply_text('请按照‘模块名 用户1 用户2...’的格式好好输入，不然小猫可帮不了你~0w0')


@id
def apply_refuse(bot, update, tpye, date=[]):
    log(update)
    try:
        for n in user_date.for_group:
            if tpye == n.name and n.admin.user_list.inornot(
                    update.message.chat_id):
                if date == []:
                    n.apply_refuse()
                else:
                    n.apply_refuse(date)
                update.message.reply_text('用户移出完毕')
                return
            update.message.reply_text('喵？并没有名叫' + type + '的模块块哦？0w0')
    except TypeError:
        update.message.reply_text('请按照‘模块名 用户1 用户2...’的格式好好输入，不然小猫可帮不了你~0w0')


def clean(bot, update, args):
    log(update)
    try:
        for n in user_date.for_group:
            if args[0] == n.name and n.admin.user_list.inornot(
                    update.message.chat_id) and args[1] == config.keyuser:
                n.clean()
                update.message.reply_text('组群清空完毕')
                return
        update.message.reply_text('喵？并没有名叫' + args[0] + '的模块块哦？0w0')
    except IndexError:
        update.message.reply_text('请按照‘模块名 执行密码’的格式好好输入，不然小猫可帮不了你~0w0')


@id
def ban(bot, update, tpye, date):
    log(update)
    try:
        for n in user_date.for_group:
            if tpye == n.name and n.admin.user_list.inornot(
                    update.message.chat_id):
                n.ban(date)
                update.message.reply_text('用户封禁完毕')
                return
            update.message.reply_text('喵？并没有名叫' + type + '的模块块哦？0w0')
    except TypeError:
        update.message.reply_text('请按照‘模块名 用户1 用户2...’的格式好好输入，不然小猫可帮不了你~0w0')


@id
def unban(bot, update, tpye, date):
    log(update)
    try:
        for n in user_date.for_group:
            if tpye == n.name and n.admin.user_list.inornot(
                    update.message.chat_id):
                n.unban(date)
                update.message.reply_text('用户解禁完毕')
                return
            update.message.reply_text('喵？并没有名叫' + type + '的模块块哦？0w0')
    except TypeError:
        update.message.reply_text('请按照‘模块名 用户1 用户2...’的格式好好输入，不然小猫可帮不了你~0w0')


def mute(bot, update, args='alluser'):
    for m in args:
        do = 0
        for n in user_date.for_group:
            if m == n.name:
                n.mute(update.message.chat_id)
                update.message.reply_text(
                    '已成功屏蔽' + m + '模块的系统消息~！0w0')
                do = 1
                break
        if not bool(do):
            update.message.reply_text('喵？并没有名叫' + m + '的模块块哦？0w0')


def unmute(bot, update, args='alluser'):
    for m in args:
        do = 0
        for n in user_date.for_group:
            if m == n.name:
                n.unmute(update.message.chat_id)
                update.message.reply_text(
                    '已解除' + m + '模块系统消息的屏蔽~！0w0')
                do = 1
                break
        if not bool(do):
            update.message.reply_text('喵？并没有名叫' + m + '的模块块哦？0w0')
