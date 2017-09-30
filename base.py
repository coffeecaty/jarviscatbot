from telegram.ext import Updater
from logprint import log
import config

def start(bot, update):
    log(update)
    update.message.reply_text('您好，我是summy专属的JarvisCat，我会代替coffeecaty对summy进行全方位照顾，如果你不是summy本人...你想看他俩秀恩爱我也没意见啊～～～～')

def help(bot, update):
    import helptest
    update.message.reply_text(helptest.help)

def miao(bot, update):
    log(update)
    update.message.reply_text('喵？')
    
def message(bot,update):
    log(update)
    if update.message.chat_id == config.yourid:    
     bot.sendMessage(config.loverid, text=update.message.text)
    elif update.message.chat_id == config.loverid:
     bot.sendMessage(config.yourid, text=update.message.text)   
     bot.sendMessage(update.message.chat_id, text='小猫虽然听不懂你在说什么，但是小猫爱大熊！小猫会问问大猫怎么回答你的！', reply_to_message_id=update.message.message_id)
    else:
     bot.sendMessage(update.message.chat_id, text='小猫虽然听不懂你在说什么，但是小猫爱大熊！', reply_to_message_id=update.message.message_id)
     bot.sendMessage(update.message.chat_id, text='如果想给coffeecaty或者summyxy留言，请使用/stc（say to coffeecaty）或者/sts（say to summyxy）')
  

