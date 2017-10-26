#!/usr/bin/env python
# -*- coding: utf-8 -*-
import user_date


def al_in(admin):
    def decorator(func):
        def wrapper(*args, **kw):
            if admin.user_list.inornot(args[1].message.chat_id):
                return func(*args, **kw)
            elif admin in user_date.public.list:
                return args[1].message.reply_text(
                    '抱歉你没有使用' + admin.name + '模块的权限，请先使用/apply申请对应模块的使用权限后再尝试此操作')
            else:
                return args[1].message.reply_text(
                    '抱歉你没有使此命令的权限，请先使用/apply申请对应模块的使用权限后再尝试此操作')
        return wrapper

    return decorator


def id(func):
    def wrapper(bot, update, args):
        try:
            change = []
            for n in args[1:]:
                try:
                    change.append(int(n))
                except ValueError:
                    if user_date.alluser.chat_id(n) == 'unknow':
                        update.message.reply_text(
                            '小猫无法在数据库中找到用户 ' + n + ' 请让他使用/start启动本猫后再试或者直接使用chat_id进行权限操作')
                    else:
                        change.append(user_date.alluser.chat_id(n))
            return func(bot, update, args[0], change)
        except IndexError:
            update.message.reply_text(
                '请按照‘模块名 用户1 用户2...’的格式好好输入，不然小猫我可帮不了你~0w0')
    return wrapper


def trans_chat_id(update, args):
    change = []
    for n in args:
        try:
            change.append(int(n))
        except ValueError:
            if user_date.alluser.chat_id(n) == 'unknow':
                update.message.reply_text(
                    '小猫无法在数据库中找到用户 ' + n + ' 请让他使用/start启动本猫后再试或者直接使用chat_id进行权限操作')
            else:
                change.append(user_date.alluser.chat_id(n))
    return change


def idnum(func):
    def wrapper(bot, update, args):
        try:
            change = []
            for n in args[1:]:
                try:
                    change.append(int(n))
                except ValueError:
                    if user_date.alluser.chat_id(n) == 'unknow':
                        update.message.reply_text(
                            '小猫无法在数据库中找到用户 ' + n + ' 请让他使用/start启动本猫后再试或者直接使用chat_id进行权限操作')
                    else:
                        change.append(user_date.alluser.chat_id(n))
            return func(bot, update, args[0], change)
        except IndexError:
            update.message.reply_text(
                '请按照‘活动编号 用户1 用户2...’的格式好好输入，不然小猫我可帮不了你~0w0')
    return wrapper
