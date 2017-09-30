from telegram.ext import Updater
from logprint import log
import config
    
def love(bot, update):
    log(update)
    update.message.reply_text('我也爱大熊！')
