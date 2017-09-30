from telegram.ext import Updater
from logprint import log
import config
    
def love(bot, update):
    log(update)
    update.message.reply_text('我也爱大熊！')

def saytolove(bot,update):
    log(update)
    if update.message.chat_id = config.yourid:
        bot.sendMessage(config.loverid, text=update.message.text) 
