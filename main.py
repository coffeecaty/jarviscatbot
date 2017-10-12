#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import base,user_command


def main():

    #导入config参数
    try:
        import config
    except ImportExcept:
        print('no config file')
        import sys
        sys.exit(0)
    updater = Updater(config.token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    # commands from base
    dp.add_handler(CommandHandler("start", base.start))

    #from user_command
    dp.add_handler(CommandHandler('iamcat',user_command.iamcat))
    dp.add_handler(CommandHandler('backup', user_command.backup))
    dp.add_handler(CommandHandler('recover', user_command.recover,pass_args=True))
    dp.add_handler(CommandHandler('print', user_command.printlist,pass_args=True))
    dp.add_handler(CommandHandler('apply', user_command.apply, pass_args=True))
    dp.add_handler(CommandHandler('add', user_command.add, pass_args=True))
    dp.add_handler(CommandHandler('remove', user_command.remove, pass_args=True))
    dp.add_handler(CommandHandler('apply_refuse', user_command.apply_refuse, pass_args=True))
    dp.add_handler(CommandHandler('clean', user_command.clean, pass_args=True))
    dp.add_handler(CommandHandler('ban', user_command.ban, pass_args=True))
    dp.add_handler(CommandHandler('unban', user_command.unban, pass_args=True))
    dp.add_handler(CommandHandler('mute', user_command.mute, pass_args=True))
    dp.add_handler(CommandHandler('unmute', user_command.unmute, pass_args=True))
    dp.add_handler(CommandHandler('notice', user_command.notice, pass_args=True))
    dp.add_handler(CommandHandler('mod', user_command.mod, pass_args=True))



    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
