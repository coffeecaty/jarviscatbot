#!/usr/bin/env python
# -*- coding: utf-8 -*-from telegram.ext import Updater
import user_date
from datetime import timedelta


def log(update):
    user_date.alluser.update(update)
    print(update.message.from_user.username, ' ', update.message.chat_id,
          ' ', str(update.message.date + timedelta(hours=8)))
    print(update.message.text)
