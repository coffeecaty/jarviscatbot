#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegram.ext import Updater
from logprint import log
import config


def love(bot, update):
    log(update)
    if update.message.chat_id == config.yourid:
        update.message.reply_text('谢谢大猫！~')
    elif update.message.chat_id == config.loverid:
        update.message.reply_text('我也爱大熊！~')
    else:
        update.message.reply_text('可我爱大熊！下一个~')
