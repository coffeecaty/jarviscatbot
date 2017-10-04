#!/usr/bin/env python
# -*- coding: utf-8 -*-

from classdate import usergroup, user
import pickle

def date_save():
    f=open('date.txt','wb')
    pickle.dump(date_all,f)
    f.close

def date_load():
    f=open('date.txt','rb')
    date_all=pickle.load(f)
    f.close
    [token,yourid,loverid,alluser,group]=date_all
    [superadmin, admin_all, superuser, decoder_admin, decoder]=group

try:
    date_load()
except(EOFError):

    #初次在服务器配置时请务必填好此处
    token = '此处粘贴你的bot token'
    yourid = 贴入你的chat_id
    loverid = 贴入你的那个她的chat_id


    # 以下内容不用修改（当然不满意默认的权限设定也可以这里直接改）

    # alluser date
    alluser = user([], [], [])

    # usergroup date
    superadmin = usergroup('superadmin', [yourid], 'all', 0, 'admin', [], [], '')
    admin_all = usergroup('admin', [yourid], 'all', 1, 'admin', [], [], superadmin)
    superuser = usergroup('superuser', [yourid, loverid], 'all', 3, 'user', [], [], admin_all)
    decoder_admin = usergroup('decoder_admin', [yourid], 'decoder', 2, 'admin', [], [], superadmin)
    decoder = usergroup('decoder', [yourid, loverid], 'decoder', 4, 'user', [], [], decoder_admin)

    # group应包含所有usergroup）
    group = [superadmin, admin_all, superuser, decoder_admin, decoder]

    #date_all用于用户数据的备份和恢复
    date_all=[token,yourid,loverid,alluser,group]
