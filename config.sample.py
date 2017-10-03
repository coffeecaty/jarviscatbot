#!/usr/bin/env python
# -*- coding: utf-8 -*-
token='此处粘贴你的bot token'
yourid=贴入你的chat_id
loverid=贴入你的那个她的chat_id


#以下内容不用修改（当然不满意默认的权限设定也可以这里直接改）
from classdate import usergroup,user

#alluser date
alluser=user([],[],[])

#usergroup date
superadmin=usergroup('superadmin',[yourid],'all',0,'admin',[],[],'')
admin_all=usergroup('admin',[yourid],'all',1,'admin',[],[],superadmin)
superuser=usergroup('superuser',[yourid,loverid],'all',3,'user',[],[],admin_all)
decode_admin=usergroup('decode_admin',[yourid],'decode',2,'admin',[],[],superadmin)
decode=usergroup('decode',[yourid,loverid],'decode',4,'user',[],[],decode_admin)

#group应包含所有usergroup）
group=[superadmin,admin_all,superuser,decode_admin,decode]
