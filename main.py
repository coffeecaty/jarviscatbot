from telegram.ext import Updater
from logprint import log

def start(bot, update):
    log(update)
    update.message.reply_text('您好，我是summy专属的JarvisCat，我会代替coffeecaty对summy进行全方位照顾，如果你不是summy本人...你想看他俩秀恩爱我也没意见啊～～～～')

def help(bot, update):
    import helptest
    update.message.reply_text(helptest.help)

def miao(bot, update):
    log(update)
    update.message.reply_text('喵？')
    
def unknow(bot,update):
    log(update)
    bot.sendMessage(update.message.chat_id, text='小猫虽然听不懂你在说什么，但是小猫爱大熊！', reply_to_message_id=update.message.message_id)
  

