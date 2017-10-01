from telegram.ext import Updater


    
def log(update):
   print(update.message.from_user.username+' 'update.message.chat_id)
   print(update.message.text)
   return
