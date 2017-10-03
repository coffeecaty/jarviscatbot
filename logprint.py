#!/usr/bin/env python
# -*- coding: utf-8 -*-from telegram.ext import Updater
import config

    
def log(update):
   config.alluser.update(update)
   print(update.message.from_user.username,' ',update.message.chat_id,' ',str(update.message.date))
   print(update.message.text)
   return
