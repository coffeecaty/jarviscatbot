#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import base,user_command,helpdoc,timer,logging,ENL_tianjin,talk

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)


def main():

    # 导入config参数
    try:
        import config
    except ImportError:
        print('no config file')
        import sys
        sys.exit(0)
    updater = Updater(config.token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    # commands from base
    dp.add_handler(CommandHandler("start", base.start))
    dp.add_handler(CommandHandler("miao", base.miao))
    dp.add_handler(CommandHandler("stc", base.stc, pass_args=True))
    dp.add_handler(CommandHandler("sts", base.sts, pass_args=True))
    dp.add_handler(CommandHandler("repeat", base.repeat, pass_args=True))
    dp.add_handler(CommandHandler("lower", base.lower, pass_args=True))
    dp.add_handler(CommandHandler('mkdb', base.mkdb))

    # commands from talk
    dp.add_handler(MessageHandler([Filters.text], talk.talk))

    # from user_command
    dp.add_handler(CommandHandler('iamcat', user_command.iamcat))
    dp.add_handler(CommandHandler('backup', user_command.backup))
    dp.add_handler(
        CommandHandler(
            'recovery',
            user_command.recovery,
            pass_args=True))
    dp.add_handler(
        CommandHandler(
            'print',
            user_command.printlist,
            pass_args=True))
    dp.add_handler(CommandHandler('apply', user_command.apply, pass_args=True))
    dp.add_handler(CommandHandler('add', user_command.add, pass_args=True))
    dp.add_handler(
        CommandHandler(
            'remove',
            user_command.remove,
            pass_args=True))
    dp.add_handler(
        CommandHandler(
            'apply_refuse',
            user_command.apply_refuse,
            pass_args=True))
    dp.add_handler(CommandHandler('clean', user_command.clean, pass_args=True))
    dp.add_handler(CommandHandler('ban', user_command.ban, pass_args=True))
    dp.add_handler(CommandHandler('unban', user_command.unban, pass_args=True))
    dp.add_handler(CommandHandler('mute', user_command.mute, pass_args=True))
    dp.add_handler(
        CommandHandler(
            'unmute',
            user_command.unmute,
            pass_args=True))
    dp.add_handler(
        CommandHandler(
            'notice',
            user_command.notice,
            pass_args=True))
    dp.add_handler(
        CommandHandler(
            'message',
            user_command.message,
            pass_args=True))
    dp.add_handler(CommandHandler('mod', user_command.mod, pass_args=True))
    dp.add_handler(CommandHandler('copy', user_command.copy, pass_args=True))
    dp.add_handler(
        CommandHandler(
            'update_mod',
            user_command.update_mod,
            pass_args=True))

    # from helopdoc
    dp.add_handler(CommandHandler('help', helpdoc.help, pass_args=True))

    # from ENL_tianjin

    dp.add_handler(CommandHandler('enl', ENL_tianjin.enl,pass_args=True))
    dp.add_handler(CommandHandler('create', ENL_tianjin.create,pass_args=True))
    dp.add_handler(CommandHandler('event', ENL_tianjin.event,pass_args=True))
    dp.add_handler(CommandHandler('detail', ENL_tianjin.detail,pass_args=True))
    dp.add_handler(CommandHandler('join', ENL_tianjin.join,pass_args=True))
    dp.add_handler(CommandHandler('unjoin', ENL_tianjin.unjoin,pass_args=True))
    dp.add_handler(CommandHandler('holder', ENL_tianjin.holder,pass_args=True))
    dp.add_handler(CommandHandler('news', ENL_tianjin.news,pass_args=True))
    dp.add_handler(CommandHandler('close', ENL_tianjin.close,pass_args=True))
    dp.add_handler(CommandHandler('reopen', ENL_tianjin.reopen,pass_args=True))
    dp.add_handler(CommandHandler('invite', ENL_tianjin.invite,pass_args=True))
    dp.add_handler(CommandHandler('showlist', ENL_tianjin.showlist,pass_args=True))
    dp.add_handler(CommandHandler('event_del', ENL_tianjin.event_del,pass_args=True))
    dp.add_handler(CommandHandler('event_rm', ENL_tianjin.event_rm,pass_args=True))
    dp.add_handler(CommandHandler('data', ENL_tianjin.data, pass_args=True))
    dp.add_handler(CommandHandler('data_new', ENL_tianjin.data_new, pass_args=True))
    dp.add_handler(CommandHandler('data_del', ENL_tianjin.data_del, pass_args=True))
    dp.add_handler(CommandHandler('group_link', ENL_tianjin.group_link, pass_args=True))

    # from timer
    dp.add_handler(CommandHandler("timer", timer.timer,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))
    dp.add_handler(
        CommandHandler(
            "untimer",
            timer.untimer,
            pass_chat_data=True))


    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
