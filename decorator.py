#!/usr/bin/env python
# -*- coding: utf-8 -*-
import user_date


def al_in(admin):
    def decorator(func):
        def wrapper(*args, **kw):
            if admin.user_list.inornot(args[1].message.chat_id):
                return func(*args, **kw)
            else:
                return args[1].message.reply_text(
                    '抱歉你没有使用' + admin.name + '类功能的权限，请使用/apply命令向coffeecaty申请使用权限')

        return wrapper

    return decorator


def id(func):
    def wrapper(*args, **kw):
        if len(args)<4:
            return func(*args, **kw)
        else:
            change = []
            n = 3
            while n < len(args):
                try:
                    change.append(int(args[n]))
                except ValueError:
                    if user_date.alluser.chat_id(args[n])=='unknow':
                        return args[1].message.reply_text('小猫无法在数据库中找到用户 '+args[n]+' 请让他使用/start启动本猫后再试或者直接使用chat_id进行权限操作')
                    else:
                        change.append(user_date.alluser.chat_id(args[n]))
                n += 1
            return func(args[0], args[1], args[2], change, **kw)
    return wrapper
