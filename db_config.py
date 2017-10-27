#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('jarviscatbot.db')
c = conn.cursor()
c.execute('''CREATE TABLE ENL_HQ(id INTEGER PRIMARY KEY,dataname TEXT, datalink TEXT);''')
c.execute('''CREATE TABLE ENL_agent(id INTEGER PRIMARY KEY,username TEXT, agentname TEXT,level INTEGER);''')
c.execute('''CREATE TABLE ENL_tianjin(eventnum INTEGER PRIMARY KEY,eventname TEXT,class TEXT  ,detail TEXT);''')
c.execute('''INSERT INTO ENL_tianjin VALUES(0,'MU黑牌申请','permanent','如果你希望社群帮你获取盖场MU黑牌的机会，请在此报名，当有类似活动机会时我们将第一时间联系你。如果你有好的计划或者想法，请使用/stc联系咖啡猫')''')
c.execute('''CREATE TABLE MU黑牌申请0(id INTEGER PRIMARY KEY,holder INTEGER );''')
c.close()

