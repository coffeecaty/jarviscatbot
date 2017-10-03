#!/usr/bin/env python
# -*- coding: utf-8 -*-
class user:
    __slots__ = ('id', 'username', 'mu')

    def __init__(self, id, username, mu):
        self.id = id
        self.username = username
        self.mu = mu

    def update(self, update):
        if update.message.chat_id not in self.id:
            self.id.append(update.message.chat_id)
            self.username.append('@' + update.message.from_user.username)
        else:
            self.username[self.id.index(update.message.chat_id)] = ('@' + update.message.from_user.username)

    def clean(self):
        self.id = []
        self.username = []
        self.mu = []

    def name(self, chat_id):
        if chat_id in self.id:
            return self.username[self.id.index(chat_id)]
        else:
            return 'unknow'

    def chat_id(self, username):
        if username in self.username:
            return self.id[self.username.index(username)]
        else:
            return 0

    def print(self, chat_id=True, username=True):
        text = ''
        if username == True and chat_id == True:
            for n in self.id:
                text = text + str(n).ljust(20) + ' | ' + self.name(n) + '\n'
            text = text + 'total ' + str(len(self.id)) + ' date.'
        elif username == True and chat_id == False:
            for n in self.id:
                text = text + self.name(n) + '\n'
            text = text + 'total ' + str(len(self.id)) + ' date.'
        elif username == False and chat_id == True:
            for n in self.id:
                text = text + str(n) + '\n'
            text = text + 'total ' + str(len(self.id)) + ' date.'
        else:
            text = '喵？你输入的参数是不是有问题喵？'
        return text

    def mute(self, chat_id):
        if chat_id not in self.mu:
            self.mu.append(chat_id)

    def unmute(self, chat_id):
        n = 0
        while n < len(self.mu):
            if self.mu[n] == chat_id:
                self.mu.pop(n)
                break
            n = n + 1


class usergroup:
    __slots__ = ('name', 'list', 'type', 'level', 'admin', 'apply', 'mu', 'send_to')

    def __init__(self, name, list, type, level, admin, apply, mu, send_to):
        self.name = name
        self.list = list
        self.type = type
        self.level = level
        self.admin = admin
        self.apply = apply
        self.mu = mu
        self.send_to = send_to

    def add(self, chat_id):
        if chat_id not in self.list:
            self.list.append(chat_id)

    def remove(self, chat_id):
        n = 0
        while n < len(self.list):
            if self.list[n] == chat_id:
                self.list.pop(n)
                break
            n = n + 1

    def addupdate(self, chat_id, group):
        self.add(chat_id)
        for n in group:
            if self.level < n.level and (self.type == 'all' or self.type == n.type):
                n.add(chat_id)

    def removeupdate(self, chat_id, group):
        self.remove(chat_id)
        if self.type == 'all':
            for n in group:
                if self.admin == n.admin and self.level < n.level:
                    n.remove(chat_id)

    def clean(self, group):
        while self.list != []:
            self.removeupdate(self.list[0], group)

    def print(self, user=None, id=True):
        text = ''
        if user == None and id == True:
            for n in self.list:
                text = text + str(n) + '\n'
            text = text + 'total ' + str(len(self.list)) + ' date.'
        elif user != None and id == True:
            for n in self.list:
                text = text + str(n) + ' | ' + user.name(n) + '\n'
            text = text + 'total ' + str(len(self.list)) + ' date.'
        elif user != None and id == False:
            for n in self.list:
                text = text + user.name(n) + '\n'
            text = text + 'total ' + str(len(self.list)) + ' date.'
        else:
            text = '喵？你输入的参数是不是有问题喵？'
        return text

    def print_apply(self, user=None, id=True):
        text = ''
        if user == None and id == True:
            for n in self.apply:
                text = text + str(n) + '\n'
            text = text + 'total ' + str(len(self.list)) + ' date.'
        elif user != None and id == True:
            for n in self.apply:
                text = text + str(n) + ' | ' + user.name(n) + '\n'
            text = text + 'total ' + str(len(self.list)) + ' date.'
        elif user != None and id == False:
            for n in self.apply:
                text = text + user.name(n) + '\n'
            text = text + 'total ' + str(len(self.list)) + ' date.'
        else:
            text = '喵？你输入的参数是不是有问题喵？'

    def add_apply(self, chat_id):
        if chat_id not in self.apply:
            self.apply.append(chat_id)

    def remove_apply(self, chat_id):
        n = 0
        while n < len(self.apply):
            if self.apply[n] == chat_id:
                self.apply.pop(n)
                break
            n = n + 1

    def clean_apply(self):
        self.apply = []

    def addupdate_apply(self, group):
        for n in self.apply:
            self.addupdate(n, group)
        self.clean_apply()

    def mute(self, chat_id):
        if chat_id not in self.mu:
            self.mu.append(chat_id)

    def unmute(self, chat_id):
        n = 0
        while n < len(self.mu):
            if self.mu[n] == chat_id:
                self.mu.pop(n)
                break
            n = n + 1

    def muteupdate(self, chat_id, group):
        self.mute(chat_id)
        for n in group:
            if self.level < n.level and (self.type == 'all' or self.type == n.type) and (self.admin == n.admin):
                n.mute(chat_id)

    def unmuteupdate(self, chat_id, group):
        self.unmute(chat_id)
        if self.type == 'all':
            for n in group:
                if self.admin == n.admin and self.level < n.level:
                    n.unmute(chat_id)


if __name__ == '__main__':
    alluser = user([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], [])
    superadmin = usergroup('superadmin', [1], 'all', 0, 'admin', [], [])
    admin_all = usergroup('admin', [1], 'all', 1, 'admin', [], [])
    superuser = usergroup('superuser', [1, 2], 'all', 3, 'user', [], [])
    admin_decode = usergroup('admin_decode', [1], 'decode', 2, 'admin', [], [])
    decode = usergroup('decode', [1, 2], 'decode', 4, 'user', [], [])
    admin_enltianjin = usergroup('admin_enltianjin', [1], 'enltianjin', 2, 'admin', [], [])
    enltianjin = usergroup('enltianjin', [1, 2], 'enltianjin', 4, 'user', [], [])
    group = [superadmin, admin_all, superuser, admin_decode, decode, admin_enltianjin, enltianjin]


    def p(group=group):
        try:
            for n in group:
                print(n.name + ' ' + n.type + ' ' + str(n.level) + ' ' + n.admin)
                print(n.list)
                print(n.apply)
        except (TypeError):
            print(group.name + ' ' + group.type + ' ' + str(group.level) + ' ' + group.admin)
            print(group.list)
            print(group.apply)
