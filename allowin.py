
def al_in(admin_list):
    def decorator(func):
     def wrapper(*args, **kw):
      if args[1].message.chat_id in admin_list:
       return func(*args, **kw)
      else:
       return args[1].message.reply_text('抱歉你没有使用'+admin_list[0]+'类功能的权限，请使用'+admin_list[1]+'向coffeecaty申请使用权限')
     return wrapper
    return decorator

if __name__ == '__main__':
from telegram.ext import Updater, CommandHandler, MessageHandler
updater=Updater('474180148:AAFXxSzhH3j3DG6PFIP9rExnYIteLxIWslc')
@al_in(['decode','/ap_decode',153042393])
def start(bot,update):
    update.message.reply_text('欢迎回来，我的大猫主人')

dp = updater.dispatcher
dp.add_handler(CommandHandler("start",start))
