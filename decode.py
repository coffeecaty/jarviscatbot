from telegram.ext import Updater
from logprint import log
from config import decode
from allowin import al_in

@al_in(decode)
def dhelp(bot,update):
    dhelp='欢迎使用decode模块功能：'
    dhl=[]
    dhl.append('/dhelp 显示本帮助')

    
    for n in dhl:
        dhelp=dhelp+'\n'+n
    update.message.reply_text(dhelp)
