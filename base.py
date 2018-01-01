#!/usr/bin/env python
# -*- coding: utf-8 -*-
from logprint import log
from datetime import timedelta
from decorator import al_in
import user_date
import sqlite3


def start(bot, update):
    log(update)
    if user_date.me.user_list.inornot(update.message.from_user.id):
        update.message.reply_text('欢迎回来，我的大猫~0w0')
    elif user_date.love.user_list.inornot(update.message.from_user.id):
        update.message.reply_text(
            '你好，我最爱的summy，我是你的专属小猫，我会辅助coffeecaty照顾你，说出你的需求，我会尽量满足。小猫还小，会的很少，请有耐心的慢慢教小猫长大哦~')
    else:
        if update.message.from_user.first_name is not None:
            update.message.reply_text(
                '您好，' +
                update.message.from_user.first_name +
                '，我是辅助coffeecaty照顾summy的专属小猫，主要负责帮caty秀恩爱，当然我也可以提供一些其他服务，但是项目太多我介绍不过来，请用/help自己慢慢看吧~')
        else:
            update.message.reply_text(
                '您好，@' +
                update.message.from_user.username +
                '，我是辅助coffeecaty照顾summy的专属小猫，主要负责帮caty秀恩爱，当然我也可以提供一些其他服务，但是项目太多我介绍不过来，请用/help自己慢慢看吧~')


def miao(bot, update):
    log(update)
    update.message.reply_text('喵？')


def stc(bot, update, args):
    log(update)
    if len(args) > 0:
        message = ''
        for n in args:
            message = message + n + ' '
        update.message.reply_text('已成功为您留言给coffeecaty')
        bot.sendMessage(
            user_date.me.user_list.list[0],
            text='from:@' +
            update.message.from_user.username +
            ':' +
            message +
            '(at ' +
            str(
                update.message.date +
                timedelta(
                    hours=8)) +
            'UTC+8:00)')
    else:
        update.message.reply_text('你怎么比小猫还笨！你都没留言我怎么帮你转达。0w0')


def sts(bot, update, args):
    log(update)
    if len(args) > 0:
        message = ''
        for n in args:
            message = message + n + ' '
        update.message.reply_text('已成功为您留言给summy')
        bot.sendMessage(
            user_date.love.user_list.list[0],
            text='from:@' +
            update.message.from_user.username +
            ':' +
            message +
            '(at ' +
            str(
                update.message.date +
                timedelta(
                    hours=8)) +
            'UTC+8:00)')
    else:
        update.message.reply_text('你怎么比小猫还笨！你都没留言我怎么帮你转达。0w0')


def repeat(bot, update, args):
    log(update)
    if len(args) == 0:
        update.message.reply_text('你怎么比小猫还笨！你都没说话我怎么重复。0w0')
    elif len(args) == 1:
        message = args[0] + '\n' + args[0] + '\n' + args[0]
        update.message.reply_text(message)
    else:
        try:
            time = int(args[-1])
            args = args[:-1]
        except (ValueError):
            time = 3
        if time < 1:
            update.message.reply_text('1后面是2，1前面是？（掰猫爪爪')
        else:
            n, text = 1, args[0]
            while n < len(args):
                text = text + ' ' + args[n]
                n = n + 1
            message = text + ('\n' + text) * (time - 1)
            update.message.reply_text(message)


@al_in(user_date.me)
def mkdb(bot, update):
    try:
        import db_config
        bot.sendMessage(update.message.from_user.id, text='数据库初始化已完成喵~有饼干吃吗？')
    except sqlite3.OperationalError:
        bot.sendMessage(update.message.from_user.id, text='数据库已存在，无需初始化喵~')

def lower(bot, update, args):
    text=''
    for n in args:
        text+=n.lower()+' '
    update.message.reply_text(text)