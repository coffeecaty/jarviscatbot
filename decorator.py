#!/usr/bin/env python
# -*- coding: utf-8 -*-

def al_in(admin):
    def decorator(func):
        def wrapper(*args, **kw):
            if admin.user_list.inornot(args[1].message.chat_id):
                return func(*args, **kw)
            else:
                return args[1].message.reply_text('抱歉你没有使用' + admin.name + '类功能的权限，请使用/apply命令向coffeecaty申请使用权限')

        return wrapper

    return decorator
