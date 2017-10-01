from telegram.ext import Updater
from logprint import log
import config

def start(bot, update):
    log(update)
    if update.message.chat_id == config.yourid:
     update.message.reply_text('欢迎回来，我的大猫主人')
    elif update.message.chat_id == config.loverid:
     update.message.reply_text('你好，我最爱的summy，我是你的专属小猫，我会辅助coffeecaty照顾你，说出你的需求，我会尽量满足。小猫还小，会的很少，请有耐心的慢慢教小猫长大哦~')
    else:
     if update.message.first_name is not None:
      update.message.reply_text('您好，'+update.message.from_user.first_name+'，我是辅助coffeecaty照顾summy的专属小猫，虽然也提供一些其他服务，但基本上你通过我只能...看caty秀恩爱啊~~~')
     else:
      update.message.reply_text('您好，@'+update.message.from_user.username+'，我是辅助coffeecaty照顾summy的专属小猫，虽然也提供一些其他服务，但基本上你通过我只能...看caty秀恩爱啊~~~')
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
  

def stc(bot,update,args):
   log(update)  
   try:
    message=''
    for n in args:
        message=message+n+' '
    update.message.reply_text('已成功为您留言给coffeecaty')
    bot.sendMessage(config.yourid,text='from:@'+update.message.from_user.username+':'+message+'at '+str(update.message.date))
   except (IndexError, ValueError):
        update.message.reply_text('你怎么比小猫还笨！你都没留言我怎么帮你转达。0w0')

def sts(bot,update,args):
   log(update)  
   try:
    message=''
    for n in args:
        message=message+n+' '
    update.message.reply_text('已成功为您留言给summy')
    bot.sendMessage(config.loverid,text='from:@'+update.message.from_user.username+':'+message+'at '+str(update.message.date))
   except (IndexError, ValueError):
        update.message.reply_text('你怎么比小猫还笨！你都没留言我怎么帮你转达。0w0')
