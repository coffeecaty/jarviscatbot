#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegram.ext import Updater
import config
from decorator import al_in

#base help
def help_base(bot, update):
    
    hb='我现在还是一只小猫，我只支持以下几种功能：'
    hl=[]
    hl.append('/start 开始交互：')
    hl.append('/miao 叫')  
    hl.append('/stc 给coffeecaty留言')
    hl.append('/sts 给summy留言')
    hl.append('/repeat 重复留言，格式为“留言 次数”，以空格分隔，次数省略则默认为3次，重要的事情说三次')
    hl.append('/help 显示本帮助')
    hl.append('/extra 显示额外功能模块')
    hl.append('/apply 申请额外功能模块权限，命令后填写功能模块名')
    hl.append('/mute 在不影响功能使用前提下屏蔽系统消息，默认全部屏蔽，单独屏蔽某模块系统消息请在命令后填写功能模块名')
    hl.append('/unmute 解除屏蔽，默认全部解除，单独解除请在命令后填写功能模块名')

    for n in hl:
        hb=hb+'\n'+n
    update.message.reply_text(hb)

def extra(bot,update):
    hb='本小猫还支持以下模块功能，请使用对应的命令获取相应模块的使用帮助：'
    hl=[]
    hl.append('/help_timer 计时器模块timer')
    hl.append('/help_decoder 解码模块decoder')

    
    for n in hl:
        hb=hb+'\n'+n
    update.message.reply_text(hb)

def help_timer(bot,update):
    hb='欢迎使用timer模块功能：'
    hl=[]
    hl.append('/set 设置时间，格式为“秒 分 时 天”，以空格分隔，可由后向前缺省，如/set 60或/set 0 1均为1分钟')
    hl.append('/unset 取消已设置的闹钟')

    
    for n in hl:
        hb=hb+'\n'+n
    update.message.reply_text(hb)

@al_in(config.decode)
def help_decoder(bot,update):
    hb='欢迎使用decode模块功能：'
    hl=[]
    hl.append('/help_decoder 显示本帮助')

    
    for n in hl:
        dhelp=dhelp+'\n'+n
    update.message.reply_text(hb)

def help_admin(bot,update):
    pass
