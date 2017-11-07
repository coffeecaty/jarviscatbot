#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle


class List(object):
    def __init__(self, name, list):
        self.name = name
        self.list = list

    def add(self, date):
        dolist = []
        try:
            for n in date:
                if n not in self.list:
                    self.list.append(n)
                    dolist.append(n)
        except TypeError:
            if date not in self.list:
                self.list.append(date)
                dolist.append(date)
        return dolist

    def len(self):
        return len(self.list)

    def remove(self, date):
        try:
            for d in date:
                n = 0
                while n < self.len():
                    if d == self.list[n]:
                        self.list.pop(n)
                    else:
                        n = n + 1

        except TypeError:
            n = 0
            while n < self.len():
                if date == self.list[n]:
                    self.list.pop(n)
                else:
                    n = n + 1

    def clean(self):
        self.list = []

    def index(self, date):
        try:
            for n in self.list:
                if n.lower() == date.lower():
                    return self.list.index(n)
        except AttributeError:
            return self.list.index(date)

    def printlist(self):
        text = ''
        for n in self.list:
            text = text + str(n).ljust(15) + ' | ' + alluser.username(n) + '\n'
        text = text + 'total ' + str(self.len()) + ' date.'
        return text

    def inornot(self, date):
        try:
            for n in self.list:
                if date.lower() == n.lower():
                    return True
            return False
        except AttributeError:
            if date in self.list:
                return True
            else:
                return False


class usergroup(object):
    def __init__(
            self,
            name,
            mod_class,
            admin,
            user_list,
            apply_list,
            mute_list,
            ban_list):
        self.name = name
        self.mod_class = mod_class
        self.admin = admin
        self.user_list = user_list
        self.apply_list = apply_list
        self.mute_list = mute_list
        self.ban_list = ban_list

    def add(self, date=[]):
        dolist = []
        if date == []:
            for n in self.apply_list.list:
                if n not in self.ban_list.list:
                    for m in self.user_list.add(n):
                        dolist.append([self.name, m])
            self. apply_list.clean()
        else:
            try:
                for n in date:
                    if n not in self.ban_list.list:
                        for m in self.user_list.add(n):
                            dolist.append([self.name, m])
            except TypeError:
                if date not in self.ban_list.list:
                    for m in self.user_list.add(date):
                        dolist.append([self.name, m])
        for a in dolist:
            if self.mute_list.inornot(a[1]):
                dolist.pop(dolist.index(a))
        return dolist

    def remove(self, date):
        self.user_list.remove(date)

    def clean(self):
        self.user_list.clean()
        self.apply_list.clean()
        self.mute_list.clean()
        self.ban_list.clean()

    def ban(self, date):
        self.ban_list.add(date)
        self.user_list.remove(date)

    def unban(self, date):
        self.ban_list.remove(date)

    def mute(self, date):
        self.mute_list.add(date)

    def unmute(self, date):
        self.mute_list.remove(date)

    def apply(self, date):
        self.apply_list.add(date)

    def apply_refuse(self, date=[]):
        if date == []:
            self.apply_list.clean()
        else:
            self.apply_list.remove(date)

    def printlist(self, type):
        text = self.name + ' ' + type + ' list' + '\n'
        if type == 'user':
            text = text + self.user_list.printlist()
        elif type == 'apply':
            text = text + self.apply_list.printlist()
        elif type == 'mute':
            text = text + self.mute_list.printlist()
        elif type == 'ban':
            text = text + self.ban_list.printlist()
        elif type == 'all':
            text = text + self.name + ' user list' + '\n' + self.user_list.printlist(
            ) + '\n' + self.name + ' apply list' + '\n' + self.apply_list.printlist(
            ) + '\n' + self.name + ' ban list' + '\n' + self.ban_list.printlist(
            )
        else:
            text = text + '喵？并没有这种列表可以打印哦？'
        return text



class groupgroup(object):
    def __init__(self, name, list, admin):
        self.name = name
        self.list = list
        self.admin = admin

    def add(self, date=[]):
        dolist = []
        for n in self.list:
            for m in n.add(date):
                dolist.append(m)
        return dolist

    def remove(self, date):
        for n in self.list:
            n.remove(date)

    def clean(self):
        for n in self.list:
            n.clean()

    def ban(self, date):
        for n in self.list:
            n.ban(date)

    def unban(self, date):
        for n in self.list:
            n.unban(date)

    def mute(self, date):
        for n in self.list:
            n.mute(date)

    def unmute(self, date):
        for n in self.list:
            n.unmute(date)

    def apply(self, date):
        for n in self.list:
            n.apply(date)

    def apply_refuse(self, date='all'):
        for n in self.list:
            n.apply_refuse(date)

    def printlist(self, type):
        text = 'all ' + type + ' list in ' + self.name + '\n'
        for n in self.list:
            text = text + n.printlist(type) + '\n'
        text = text + 'that\'s all'
        return text

    def inany(self, date):
        for n in self.list:
            if n.user_list.inornot(date):
                return True
        return False


    def namelist(self):
        namelist = []
        for n in self.list:
            namelist.append(n.name)
        return namelist


class full_usergroup(usergroup):
    def __init__(
            self,
            name,
            mod_class,
            admin,
            user_list=List('user', []),
            username_list=List('usrname', []),
            apply_list=List('apply', []),

            mute_list=List('mute', []),
            ban_list=List('ban', [])):
        self.name = name
        self.mod_class = mod_class
        self.admin = admin
        self.user_list = user_list
        self.username_list = username_list
        self.apply_list = apply_list
        self.mute_list = mute_list
        self.ban_list = ban_list

    def username(self, date):
        try:
            namegroup = []
            for n in date:
                if self.user_list.inornot(n):
                    namegroup.append(
                        self.username_list.list[self.user_list.index(n)])
                else:
                    'unknow ' + str(n)
            return namegroup
        except TypeError:
            if self.user_list.inornot(date):
                return self.username_list.list[self.user_list.index(date)]
            else:
                return 'unknow ' + str(date)

    def chat_id(self, date):
        if isinstance(date, list):
            idgroup = []
            for n in date:
                if self.username_list.inornot(n):
                    idgroup.append(
                        self.user_list.list[self.username_list.index(n)])
                else:
                    'unknow'
            return idgroup
        else:
            if self.username_list.inornot(date):
                return self.user_list.list[self.username_list.index(date)]
            else:
                return 'unknow'

    def update(self, update):
        if not self.user_list.inornot(update.message.from_user.id):
            self.username_list.list.append(
                '@' + update.message.from_user.username)
            self.user_list.add(update.message.from_user.id)
        else:
            self.username_list.list[self.user_list.index(update.message.from_user.id)] = (
                '@' + update.message.from_user.username)


def backup():
    f = open('date.txt', 'wb')
    for n in date_group:
        pickle.dump(n.user_list, f)
        if n.name == 'alluser':
            pickle.dump(n.username_list, f)
        else:
            pickle.dump(n.apply_list, f)
        pickle.dump(n.mute_list, f)
        pickle.dump(n.ban_list, f)
    f.close


def recovery():
    f = open('date.txt', 'rb')
    for n in date_group:
        n.user_list = pickle.load(f)
        n.apply_list = pickle.load(f)
        n.mute_list = pickle.load(f)
        n.ban_list = pickle.load(f)
    f.close
    alluser.username_list.add(alluser.apply_list.list)
    alluser.apply_list.clean()


me = usergroup(
    'self', 'private', '', List(
        'user', []), List(
            'apply', []), List(
                'mute', []), List(
                    'ban', []))
love = usergroup(
    'love', 'privite', me, List(
        'user', []), List(
            'apply', []), List(
                'mute', []), List(
                    'ban', []))
superadmin = usergroup(
    'superadmin', 'all', me, List(
        'user', []), List(
            'apply', []), List(
                'mute', []), List(
                    'ban', []))
alluser = full_usergroup('alluser', 'alluser', me)
decode_admin = usergroup(
    'decode_admin', 'decode', superadmin, List(
        'user', []), List(
            'apply', []), List(
                'mute', []), List(
                    'ban', []))
decode = usergroup(
    'decode', 'decode', decode_admin, List(
        'user', []), List(
            'apply', []), List(
                'mute', []), List(
                    'ban', []))
ENL_tianjin_admin = usergroup(
    'ENL_tianjin_admin', 'ENL_tianjin', superadmin, List(
        'user', []), List(
            'apply', []), List(
                'mute', []), List(
                    'ban', []))
ENL_tianjin_HQ = usergroup(
    'ENL_tianjin_HQ', 'ENL_tianjin', ENL_tianjin_admin, List(
        'user', []), List(
            'apply', []), List(
                'mute', []), List(
                    'ban', []))
ENL_tianjin = usergroup(
    'ENL_tianjin', 'ENL_tianjin', ENL_tianjin_admin, List(
        'user', []), List(
            'apply', []), List(
                'mute', []), List(
                    'ban', []))

# 对全部模块admin操作
admingroup = groupgroup(
    'admingroup', [
        decode_admin, ENL_tianjin_admin], superadmin)

# 对全部模块普通用户操作
usergroup = groupgroup(
    'usergroup', [
        decode, ENL_tianjin, ENL_tianjin_HQ], superadmin)

# 对全部模块用户操作
allgroup = groupgroup('allgroup', admingroup.list + usergroup.list, superadmin)

# 对ENL_天津类模块全部用户操作
ENL_tianjin_group = groupgroup(
    'ENL_tianjin_group', [
        ENL_tianjin, ENL_tianjin_HQ], ENL_tianjin_admin)

# 数据拷贝用组
date_group = [
    alluser,
    me,
    love,
    superadmin,
    decode_admin,
    decode,
    ENL_tianjin_admin,
    ENL_tianjin_HQ,
    ENL_tianjin]
try:
    recover()
except EOFError:
    pass

# 检索命令组名用组
for_group = [
    alluser,
    love,
    superadmin,
    decode_admin,
    decode,
    ENL_tianjin_admin,
    ENL_tianjin_HQ,
    ENL_tianjin,
    admingroup,
    usergroup,
    allgroup,
    ENL_tianjin_group]

# help admin权限分配用组
admin_list = groupgroup(
    'help_admin_list', [
        me, superadmin, decode_admin, ENL_tianjin_admin], me)

# 公开分组
public = groupgroup('public', [decode, ENL_tianjin], me)
