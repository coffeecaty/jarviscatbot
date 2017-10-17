#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3

def datebase(bot,update,args,chat_date):
    if args[0]=='connect':
        db =sqlite3.connect(args[1]+'.db')
        chat_date['db']=db
        update.message.reply_text('done')
    elif args[0]=='close':
        if 'db' in chat_date:
            db=chat_date['db']
            db.close()
            del chat_data['db']
            update.message.reply_text('done')
    elif args[0]=='commit':
        if 'db' in chat_date:
            db=chat_date['db']
            db.commit()
            update.message.reply_text('done')
    elif args[0]=='execute':
        if 'db' in chat_date:
            db=chat_date['db']
            c=db.cursor()
            c.execute(args[1])
            update.message.reply_text('done')
    elif args[0]=='fetch':
        if 'db' in chat_date:
            db=chat_date['db']
            c=db.cursor()
            if args[1]=='one':
                update.message.reply_text(c.fetchone())
            elif args[1]=='all':
                p=''
                for n in c.fetchall():
                    text= '{} {}{}{}\n'.format(row[0], row[1], row[2], row[3])
                    p=p+text
                    update.message.reply_text(p)