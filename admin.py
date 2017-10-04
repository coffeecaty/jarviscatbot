#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegram.ext import Updater
from logprint import log
import config
from decorator import al_in

@al_in(config.superadmin)
def date_revovery(bot,update,args):
    log(update)
    if args[0]='yes':
        try
            config.date_load()
        except(EOFError):
            update.message.reply_text('没有备份的数据可供还原喵！')
    else:
        update.message.reply_text('数据库操作事关重大，请在命令后输入yes执行')
        
# def show_mod:

#    all(admin)

#    your

#    anyone(admin)

# def show_list:

#    alluser(super)

#    superadmin(self)

#    admin_all(self)

#    admin_group(self)

#    superuser(admin_all)

#    groupuser(admin_group)


# def add:

#    superadmin(self)

#    admin_all(super)

#    admin_group(super)

#    superuser(admin_all)

#    groupuser(admin_group)


# def remove:

#    superadmin(self)

#    admin_all(super)

#    admin_group(super)

#    superuser(admin_all)

#    groupuser(admin_group)


# def clean:

#    alluser(super)

#    superadmin(self)

#    admin_all(super)

#    admin_group(super)

#    superuser(admin_all)

#    groupuser(admin_group)

# def reapply:(print_apply,add_apply,remove_apply,clean_apply,addupdate_apply)

#    superadmin(self)

#    admin_all(super)

#    admin_group(super)

#    superuser(admin_all)

#    groupuser(admin_group)

# def apply:

#    admin_all(super)

#    admin_group(super)

#    superuser(admin_all)

#    groupuser(admin_group)

# def mute:

#    syetem

#    group

# def unmute:

#    system

#    group

# def system:

#    alluser(super)

#    superadmin(self)

#    admin_all(super)

#    admin_group(super)

#    superuser(admin_all)

#    groupuser(admin_group)
