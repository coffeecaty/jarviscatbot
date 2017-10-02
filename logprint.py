from telegram.ext import Updater
from config import alluser

    
def log(update):
   if update.message.chat_id not in alluser[1]:
      alluser[0].append(update.message.chat_id)
      alluser[1].append('@'+update.message.from_user.username)
   else:
      alluser[1][alluser[0].index(update.message.chat_id)]='@'+update.message.from_user.username
   print(update.message.from_user.username,' ',update.message.chat_id,' ',str(update.message.date))
   print(update.message.text)
   return
