#!/usr/bin/env python
# -*- coding: utf-8 -*-
from logprint import log

def start(bot, update):
    log(update)
        update.message.reply_text('哦')