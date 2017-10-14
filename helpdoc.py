#!/usr/bin/env python
# -*- coding: utf-8 -*-
import user_date
def help_base():
    text='''/start  开始交互
/help   显示帮助文档，格式为/help 模块，默认为本帮助
/apply  申请额外模块权限，格式为/apply 模块1 （模块2...）
/mute   屏蔽模块系统消息，格式为/mute （模块1 模块2...），默认全部屏蔽
/unmute 解除系统消息屏蔽，格式为/unmute （模块1 模块2...），默认全部解除
/mod    显示模块列表，格式为/mod （all），默认显示已有权限的模块，all显示全部功能模块'''
    update.message.reply_text(text)


def help(bot,update,args=['base']):
    if args[0]=='base':
        help_base()
    elif args[0] in (['admin']+user_date.admin_list.namelist()):
        print('admin')
        help_admin(update.message.chat_id)
    elif args[0] =='decode':
        print('decode')
        #help_decode()
    elif args[0] in (user_date.ENL_tianjin_group.namelist()):
        print('ENL_tianjin')
        #help_ENL()
    else:
        update.message.reply_text('并没有这种模块的帮助文档喵，请核对输入模块名以及你是否有该模块的使用权限。')
