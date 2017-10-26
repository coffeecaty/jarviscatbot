#!/usr/bin/env python
# -*- coding: utf-8 -*-
import user_date,config


def help_base(update):
    text = '''/start 开始交互
/help 显示帮助文档，格式为/help 模块，默认为本帮助
/apply 申请额外模块权限，格式为/apply 模块1 （模块2...）
/mute 屏蔽模块系统消息，格式为/mute （模块1 模块2...），默认全部屏蔽
/unmute 解除系统消息屏蔽，格式为/unmute （模块1 模块2...），默认全部解除
/mod 显示模块列表，格式为/mod （all），默认显示已有权限的模块，all显示全部模块
/update_mod 更新自己的模块权限信息
/stc 给coffeecaty留言 ，格式为/stc 留言内容
/sts 给summyxy留言 ，格式为/sts 留言内容
/repeat 重复消息，格式为/repeat 内容（次数），默认为重要的事情说三遍'''
    if user_date.me.user_list.inornot(update.message.from_user.id):
        text = text + '\n/mkdb 初始化数据库'
    update.message.reply_text(text)


def help_admin(update):
    text = '/help admin 显示本帮助'
    if user_date.me.user_list.inornot(update.message.from_user.id):
        text = text + '''
/iamcat 重设self权限
/backup 备份用户数据
/recovery ''' + config.keyuser + ''' 从备份中恢复用户数据'''
    text = text + '''\n以下全部涉及用户的操作，均可使用chat_id或@username两种形式，两者完全等价。
/print 打印列表，格式为/print 模块 （列表），列表包括用户列表（user），申请列表（apply），封禁列表（ban），全部列表（all)，'''
    if user_date.me.user_list.inornot(update.message.from_user.id):
        text = text + '屏蔽列表（mute），'
    text=text+'默认输出user列表'
    if user_date.superadmin.user_list.inornot(update.message.from_user.id):
        text = text + '''\n/mod 增加显示指定玩家可使用的模块列表，格式为/mod （用户1 用户2...）
/update_mod 增加更新指定玩家的模块权限信息，格式为/update_mod （用户1 用户2）'''
    text = text + '''\n/add 增加新用户，格式为/add 模块 （用户1 用户2...），默认添加全部已提交申请的用户。
/apply_refuse 拒绝用户的申请请求，格式为/apply_refuse 模块 （用户1 用户2），默认拒绝队列中全部的请求。
/remove 删除用户，格式为/remove 模块 用户1 （用户2...)
/ban 封禁并删除用户，格式为/ban 模块 用户1 （用户2...）
/unban 解封用户，格式为/unban 模块 用户1 （用户2...）
/notice 对模块内用户发送系统消息，格式为/notice 模块 消息内容'''
    if user_date.me.user_list.inornot(update.message.from_user.id):
        text = text + '\n/message 向任意用户留言，格式为/message 用户1 （用户2...） : 内容'
    text = text + '\n/clean 模块 ' + config.keyuser + \
        ' 清空整个模块的用户数据(牛逼操作 请务必慎重操作)！！\n\n您可以管理的模块包括：\n'
    mod = 0
    for n in user_date.for_group:
        if n.admin.user_list.inornot(update.message.from_user.id):
            text = text + n.name + ' '
            mod += 1
    text = text + '\ntotal ' + str(mod) + ' mod group'
    update.message.reply_text(text)

def help_timer(update):
    text = '''欢迎使用timer模块功能：
/timer 设置时间，格式为“秒 分 时 天”，以空格分隔，可由后向前缺省，如/set 60或/set 0 1均为1分钟
/untimer 取消已设置的闹钟'''
    update.message.reply_text(text)

def help_ENL_tianjin(update):
    text = '''欢迎使用ENL_tianjin模块功能，初次使用请务必先进行个人特工信息维护：
特别提示：本模块中绝大部分对用户/活动编号操作均支持批量操作，但强烈建议一次只对一个目标进行操作，尤其是showlist功能
/enl 个人特工信息维护，格式为/enl 特工名 特工等级'''
    if user_date.ENL_tianjin_HQ.user_list.inornot(update.message.from_user.id):
        text = text + '\n/create 创建一个活动，格式为/create 活动名 （活动类型 详细介绍），活动名不能以数字开头，活动类型分为open或HQ，默认为open'
    text=text+'''
/event 显示全部活动，格式为/event （all），默认只显示进行中的活动，all显示全部活动
/detail 显示活动的详细情报，格式为/event 活动编号1 （活动编号2 ...）
/join 报名参与活动，格式为/join 活动编号1 （活动编号2 ...）
/unjoin 取消活动的报名，格式为/unjoin 活动编号1 （活动编号2 ...）
/holder 设定活动的主办人，格式为/holder 活动编号 用户1 （用户2...），您需为该活动的主办人方可执行，被设定用户需已报名该活动
/news 更新活动进度，格式为/news 活动编号 更新内容，您需为该活动的主办人方可执行，更新将记录在detail信息内并通知全体参加人
/close 结束活动，格式为/close 活动编号1 （活动编号2 ...），您需为该活动的主办人方可执行'''
    if user_date.ENL_tianjin_HQ.user_list.inornot(update.message.from_user.id):
        text = text + '，一旦活动close则会对全部玩家公开，HQ类活动请慎重close'
    text = text + '''
/reopen 重启活动，格式为/reopen 活动编号1 （活动编号2 ...），您需为该活动的主办人方可执行，支持批量操作但不建议，我也不知道为什么会有这种奇怪的功能'''
    if user_date.ENL_tianjin_HQ.user_list.inornot(update.message.from_user.id):
        text = text + '''
/invite 将用户加入活动，格式为/invite 活动编号 用户1 （用户2...），本功能仅为HQ类活动手动添加非HQ人员时使用，其他情况请尽量等待玩家主动报名'''
    text = text + '''
/showlist 显示参加活动的用户列表，格式为 /showlist 活动编号1 （活动编号2 ...），您需为该活动的主办人方可执行'''
    if user_date.me.user_list.inornot(update.message.from_user.id):
        text = text + '''
/event_del 删除活动，格式为/event_del 活动编号1 （活动编号2...）''' + config.keyuser + '''
/event_rm 从活动中移出特工，格式为/event_rm 活动编号 用户1 （用户2...） ''' + config.keyuser
    update.message.reply_text(text)

def help(bot, update, args):
    if args == [] or args[0] == 'base':
        help_base(update)
    elif args[0] in (['admin'] + user_date.admin_list.namelist()) and user_date.admin_list.inany(update.message.from_user.id):
        help_admin(update)
    elif args[0] == 'decode':
        update.message.reply_text('还没写')
        # help_decode()
    elif args[0] in (user_date.ENL_tianjin_group.namelist()) and user_date.ENL_tianjin_group.inany(update.message.from_user.id):
        help_ENL_tianjin(update)
    elif args[0] == 'timer':
         help_timer(update)
    else:
        update.message.reply_text('并没有这种模块的帮助文档喵，请核对输入模块名以及你是否有该模块的使用权限。')
