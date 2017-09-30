from telegram.ext import Updater


    
def log(update):
   print(update.message.from_user.username)
   print(update.message.text)
   return
