#!/usr/bin/env python
# -*- coding: utf-8 -*-

from logprint import log
from decorator import al_in
import user_date

def enter_code(args):
    try:
        code=args[0].lower()
    except IndexError:
        code='o'
    if code not in ['o','n']:
        user_date['origin_code']=code
        try:
            del user_data['new_code']
        except KeyError:
        pass
    elif code == 'o':
        code=user_date['origin_code']
    else:
        code=user_date['new_code']
    return code


@al_in(user_date.decode)
def atbash(bot,update,args):
    log(update)
    try:
        code=enter_code(args)
    except KeyError:
        update.message.reply_text('无法找到待解码数据，请直接输入待解码以开始工作喵~')
    try:
        dofor = args[1]
        if dofor in ['n','a']:
            try:
                num=int(args[2])
            except (ValueError,IndexError):
                num=9
    except IndexError:
        dofor='l'


