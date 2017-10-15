#!/usr/bin/env python
# -*- coding: utf-8 -*-

from logprint import log
from decorator import al_in, id
from datetime import timedelta
import user_date
import config


def iamcat(bot, update):
    log(update)
    if update.message.from_user.username == config.keyuser:
        user_date.me.add(update.message.chat_id)
        user_date.superadmin.add(update.message.chat_id)
        user_date.allgroup.add(update.message.chat_id)
        update.message.reply_text('欢迎回来，我的大猫~0w0')
    else:
        update.message.reply_text('小猫我可不傻，你根本不是大猫哼哼哼~0w0')


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


def printlist(bot, update, args):
    log(update)
    try:
        for n in user_date.for_group:
            if args[0] == n.name and n.admin.user_list.inornot(
                    update.message.chat_id):
                update.message.reply_text(n.printlist(args[1]))
                return
        update.message.reply_text('喵？并没有你说的这种模块块哦？0w0')
    except IndexError:
        update.message.reply_text('请好好输入你打印的列表种类？0w0')


def apply(bot, update, args):
    log(update)
    try:
        for m in args:
            do = 0
            for n in user_date.for_group:
                if m == n.name:
                    do = 1
                    if n.ban_list.inornot(update.message.chat_id):
                        update.message.reply_text(
                            '喵？您已被管理员封禁' + m + '模块权限，如有疑问请联系模块管理员，小猫我可不知道发生了什么哦！0w0')
                    elif n.user_list.inornot(update.message.chat_id):
                        update.message.reply_text(
                            '喵？小猫我仔细检查了一下觉得您已经有' + m + '模块的权限了哦！0w0')
                    elif n.apply_list.inornot(update.message.chat_id):
                        update.message.reply_text(
                            '喵？您已提交过' + m + '模块权限，请耐心等候管理员的批准哦~！0w0')
                    else:
                        n.apply(update.message.chat_id)
                        for a in n.admin.user_list.list:
                            if not (user_date.alluser.mute_list.inornot(
                                    a) or n.admin.mute_list.inornot(a)):
                                bot.sendMessage(a, text='@' +
                                                update.message.from_user.username +
                                                '向您申请使用' +
                                                m +
                                                '模块的使用权限 (at ' +
                                                str(update.message.date +
                                                    timedelta(hours=8)) +
                                                'UTC+8:00)')
                        update.message.reply_text(
                            '您的' + m + '模块权限申请小猫我已成功替您提交，请耐心等候管理员的批准哦~！0w0')
                    break
            if not bool(do):
                update.message.reply_text('喵？并没有名叫' + m + '的模块块哦？0w0')
    except IndexError:
        update.message.reply_text('请好好输入你要申请的模块名哦，不然小猫我可帮不了你~0w0')


@id
def add(bot, update, type, date=[]):
    log(update)
    for n in user_date.for_group:
        if type == n.name and n.admin.user_list.inornot(
                update.message.chat_id):
            for m in n.add(date):
                if not user_date.alluser.mute_list.inornot(m[1]):
                    bot.sendMessage(m[1], text='您已获得 ' +
                                    m[0] +
                                    ' 模块的使用权限，请使用/help ' +
                                    m[0] +
                                    ' 获取模块使用帮助\n(at ' +
                                    str(update.message.date +
                                        timedelta(hours=8)) +
                                    'UTC+8:00)')
            update.message.reply_text('用户授权完毕')
            return
    update.message.reply_text('喵？并没有名叫' + type + '的模块块哦？0w0')


@id
def remove(bot, update, type, date):
    log(update)
    if date == []:
        update.message.reply_text('请按照‘模块名 用户1 用户2...’的格式好好输入，不然小猫我可帮不了你~0w0')
    else:
        for n in user_date.for_group:
            if type == n.name and n.admin.user_list.inornot(
                    update.message.chat_id):
                n.remove(date)
                update.message.reply_text('用户移出完毕')
                return
        update.message.reply_text('喵？并没有名叫' + type + '的模块块哦？0w0')


@id
def apply_refuse(bot, update, type, date=[]):
    log(update)
    for n in user_date.for_group:
        if type == n.name and n.admin.user_list.inornot(
                update.message.chat_id):
            n.apply_refuse(date)
            update.message.reply_text('用户移出完毕')
            return
    update.message.reply_text('喵？并没有名叫' + type + '的模块块哦？0w0')


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
        update.message.reply_text('请按照‘模块名 执行密码’的格式好好输入，不然小猫我可帮不了你~0w0')


@id
def ban(bot, update, type, date):
    log(update)
    if date == []:
        update.message.reply_text('请按照‘模块名 用户1 用户2...’的格式好好输入，不然小猫我可帮不了你~0w0')
    else:
        for n in user_date.for_group:
            if type == n.name and n.admin.user_list.inornot(
                    update.message.chat_id):
                n.ban(date)
                update.message.reply_text('用户封禁完毕')
                return
        update.message.reply_text('喵？并没有名叫' + type + '的模块块哦？0w0')


@id
def unban(bot, update, type, date):
    log(update)
    if date == []:
        update.message.reply_text('请按照‘模块名 用户1 用户2...’的格式好好输入，不然小猫我可帮不了你~0w0')
    else:
        for n in user_date.for_group:
            if type == n.name and n.admin.user_list.inornot(
                    update.message.chat_id):
                n.unban(date)
                update.message.reply_text('用户解禁完毕')
                return
        update.message.reply_text('喵？并没有名叫' + type + '的模块块哦？0w0')


def mute(bot, update, args):
    if args == []:
        user_date.alluser.mute(update.message.chat_id)
        update.message.reply_text('已成功屏蔽全部的系统消息~！0w0')
    else:
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


def unmute(bot, update, args):
    if args == []:
        user_date.alluser.unmute(update.message.chat_id)
        update.message.reply_text('已成功解除全部系统消息的屏蔽状态~！0w0')
    else:
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


def notice(bot, update, args):
    log(update)
    try:
        text = ''
        for a in args[1:]:
            text = text + a
        if text == '':
            update.message.reply_text('小猫我可不知道你想说什么~0w0')
            return
        for n in user_date.for_group:
            if args[0] == n.name and n.admin.user_list.inornot(
                    update.message.chat_id):
                for m in n.user_list.list:
                    if not (n.mute_list.inornot(m)
                            or user_date.alluser.mute_list.inornot(a)):
                        bot.sendMessage(
                            m,
                            text='system notice from group ' +
                            n.name +
                            ':\n' +
                            text +
                            '\n(at ' +
                            str(
                                update.message.date +
                                timedelta(
                                    hours=8)) +
                            'UTC+8:00)')
                update.message.reply_text('通知完毕')
                return
        update.message.reply_text('喵？并没有名叫' + args[0] + '的模块块哦？0w0')
    except AttributeError:
        text = ''
        for a in args[1:]:
            text = text + a + ' '
        if text == '':
            update.message.reply_text('小猫我可不知道你想说什么~0w0')
            return
        noticelist = user_date.List('', [])
        templist = user_date.List('', [])
        for n in user_date.for_group:
            if args[0] == n.name and n.admin.user_list.inornot(
                    update.message.chat_id):
                noticelist.name = n.name
                for m in n.list:
                    templist.add(m.user_list.list)
                    templist.remove(m.mute_list.list)
                    noticelist.add(templist.list)
                    templist.clean()
                noticelist.remove(user_date.alluser.mute_list.list)
                break
        for a in noticelist.list:
            bot.sendMessage(
                a,
                text='system notice from class ' +
                     noticelist.name +
                     ':\n' +
                     text +
                     '\n(at ' +
                     str(
                         update.message.date +
                         timedelta(
                             hours=8)) +
                     'UTC+8:00)')
    except IndexError:
        update.message.reply_text('请按照‘模块名 通知内容’的格式好好输入，不然小猫我可帮不了你~0w0')


def mod(bot, update, args=[]):
    log(update)
    if args == [] or (
        ('all' not in args)and (
            not user_date.superadmin.user_list.inornot(
            update.message.chat_id))):
        change = [update.message.chat_id]
    elif ('all' in args)and (not user_date.superadmin.user_list.inornot(update.message.chat_id)):
        change = ['all']
    else:
        change = []
        for n in args:
            try:
                change.append(int(n))
            except ValueError:
                if n == 'all':
                    change.append('all')
                elif user_date.alluser.chat_id(n) == 'unknow':
                    update.message.reply_text(
                        '小猫无法在数据库中找到用户 ' + n + ' 请让他使用/start启动本猫后再试或者直接使用chat_id进行操作')
                else:
                    change.append(user_date.alluser.chat_id(n))
    for m in change:
        if m == 'all':
            text = 'all mod list:\n'
            dolist = user_date.List('', [])
            for a in user_date.for_group:
                if a.admin.user_list.inornot(update.message.chat_id):
                    dolist.add([a.admin.name, a.name])
                elif a.user_list.inornot(update.message.chat_id):
                    dolist.add([a.name])
            dolist.add(user_date.public.namelist())
            for n in dolist.list:
                text = text + n + '\n'
            text = text + 'total ' + str(dolist.len()) + ' mod'
            update.message.reply_text(text)
        else:
            text = 'all mod list for ' + user_date.alluser.username(m) + ' :\n'
            mod = 0
            for a in user_date.date_group:
                try:
                    if a.user_list.inornot(m):
                        name = a.name.ljust(20)
                        mute = ''
                        if a.mute_list.inornot(m):
                            mute = '|mute'
                        text = text + name + mute + '\n'
                        mod = mod + 1
                except AttributeError:
                    continue
            text = text + 'total ' + \
                str(mod) + ' mod for ' + user_date.alluser.username(m)
            update.message.reply_text(text)


def message(bot,update,args):
    try:
        user=args[:args.index('~')]
        text=args[args.index('~')+1:]
    except ValueError:
        update.message.reply_text('请按照‘用户1 （用户2...） ~ 内容’的格式好好输入，小猫才能帮你发送消息哦~0w0')
    if text == []:
        update.message.reply_text('小猫我可不知道你想说什么~0w0')
    user_id=[]
    for n in user:
        try:
            user_id.append(int(n))
        except ValueError:
            if user_date.alluser.chat_id(n) == 'unknow':
                update.message.reply_text(
                    '小猫无法在数据库中找到用户 ' + n + ' 请让他使用/start启动本猫后再试或者直接使用chat_id进行操作')
            else:
                user_id.append(user_date.alluser.chat_id(n))
    if user_id==[]:
        update.message.reply_text('小猫我可不知道你想和谁说悄悄话哦~0w0')
    text_message = ''
    for n in text:
        text_message = text_message + n + ' '
    for m in user_id:
            bot.sendMessage(
                m,
                text='@coffeecaty:\n'+
                     text_message +
                     '\n(at ' +
                     str(
                         update.message.date +
                         timedelta(
                             hours=8)) +
                     'UTC+8:00)')
            update.message.reply_text('已向 '+user_date.alluser.username(m)+' 成功转达消息')