from telegram.ext import Updater


    
def log(update):
   print(update.message.chat_id)
   print(update.message.username)
   print(update.message.text)
   return
