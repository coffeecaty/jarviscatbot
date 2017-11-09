#!/usr/bin/env python
# -*- coding: utf-8 -*-
from decorator import al_in, trans_chat_id, idnum
from logprint import log
from datetime import timedelta
import sqlite3
import user_date
import config


@al_in(user_date.ENL_tianjin)
def enl(bot, update, args):
    log(update)
    try:
        agentname = args[0]
        level = int(args[1])
    except (ValueError, IndexError):
        update.message.reply_text('请按照/enl 特工名 等级 的格式维护个人信息喵')
        return
    conn = sqlite3.connect('jarviscatbot.db')
    c = conn.cursor()
    try:
        c.execute(
            "INSERT INTO ENL_agent(id,username,agentname,level) VALUES (?,?,?,?)",
            (update.message.from_user.id,
             '@' + update.message.from_user.username,
             agentname,
             level))
    except sqlite3.IntegrityError:
        c.execute(
            "update ENL_agent SET username=?,agentname=?,level=? WHERE id=?",
            ('@' +
             update.message.from_user.username,
             agentname,
             level,
             update.message.from_user.id))
    conn.commit()
    conn.close()
    update.message.reply_text(
        '您的特工信息已经维护完毕，为了社群效率，在您修改您的telegram username，游戏特工名或者等级产生变化时请及时更新您的个人信息。')


@al_in(user_date.ENL_tianjin_HQ)
def create(bot, update, args):
    log(update)
    try:
        name = args[0]
    except IndexError:
        bot.sendMessage(update.message.from_user.id, text='请至少输入活动名才能创建一个活动喵')
        return
    try:
        test = int(name[0])
        bot.sendMessage(
            update.message.from_user.id,
            text='活动名不可以用数字开头喵！请重新输入活动名')
        return
    except ValueError:
        pass
    try:
        if args[1] in ['open', 'HQ']:
            status = args[1]
        else:
            bot.sendMessage(
                update.message.from_user.id,
                text='请输入正确的活动类型（open/HQ）喵')
    except IndexError:
        status = 'open'

    detail = str(update.message.date + timedelta(hours=8)) + ' ' + \
        user_date.alluser.username(update.message.from_user.id) + ' -- 创建活动：'
    for text in args[2:]:
        detail += text + ' '

    conn = sqlite3.connect('jarviscatbot.db')
    c = conn.cursor()
    c.execute(
        "INSERT INTO ENL_tianjin(eventname,class,detail) VALUES (?,?,?)",
        (name,
         status,
         detail))
    conn.commit()
    id=c.lastrowid
    tablename = name + str(id)
    c.execute(
        'CREATE TABLE ' +
        tablename +
        ' (id INTEGER PRIMARY KEY ,holder INTEGER);')
    c.execute(
        'INSERT INTO ' +
        tablename +
        '(id,holder) VALUES (?,1)',
        (update.message.from_user.id,
         ))
    conn.commit()
    conn.close()
    if status == 'open':
        for member in user_date.ENL_tianjin.user_list.list:
            if member == update.message.from_user.id:
                continue
            elif (not user_date.ENL_tianjin.mute_list.inornot(member)) and (not user_date.alluser.mute_list.inornot(member)):
                bot.sendMessage(member, text='天津启蒙军开展了新的活动: ' + name)
    else:
        for member in user_date.ENL_tianjin_HQ.user_list.list:
            if member == update.message.from_user.id:
                continue
            elif (not user_date.ENL_tianjin_HQ.mute_list.inornot(member)) and (
                    not user_date.alluser.mute_list.inornot(member)):
                bot.sendMessage(member, text='天津启蒙军开展了新的秘密活动: ' + name)
        bot.sendMessage(update.message.from_user.id, text=name + '活动已成功创建')


@al_in(user_date.ENL_tianjin)
def event(bot, update, args):
    log(update)
    conn = sqlite3.connect('jarviscatbot.db')
    c = conn.cursor()
    if user_date.ENL_tianjin_HQ.user_list.inornot(update.message.from_user.id):
        if len(args) > 0 and args[0] == 'all':
            c.execute('SELECT eventnum,eventname,class FROM ENL_tianjin')
        else:
            c.execute(
                '''SELECT eventnum,eventname,class FROM ENL_tianjin WHERE class!='close' ''')
    else:
        if len(args) > 0 and args[0] == 'all':
            c.execute(
                '''SELECT eventnum,eventname,class FROM ENL_tianjin WHERE class!='HQ' ''')
        else:
            c.execute(
                '''SELECT eventnum,eventname,class FROM ENL_tianjin WHERE class!='HQ' AND class!='close' ''')
    list = c.fetchall()
    text = '活动编号'.ljust(6) + '|' + '活动名'.ljust(27) + \
        '|' + '状态'.ljust(8) + '|' + '参与情况'
    for e in list:
        c.execute('SELECT holder FROM ' +
                  e[1] +
                  str(e[0]) +
                  ' WHERE id=? ', (update.message.from_user.id,))
        try:
            if c.fetchone()[0]:
                join = 'holder'
            else:
                join = 'join'
        except TypeError:
            join = ''

        if len(e[1]) < 15:
            name_just = 30
            for l in e[1]:
                if l >= u'\u4e00' and l <= u'\u9fa5':
                    name_just -= 1
        else:
            name_just = 15

        text = text + '\n' + str(e[0]).ljust(10) + \
            '|' + e[1].ljust(name_just) + '|' + e[2].ljust(10) + '|' + join
    bot.sendMessage(update.message.from_user.id, text=text)


@al_in(user_date.ENL_tianjin)
def detail(bot, update, args):
    log(update)
    if len(args) == 0:
        update.message.reply_text('请输入您要了解的活动的活动编号喵！')
        return
    for num in args:
        try:
            num = int(num)
            conn = sqlite3.connect('jarviscatbot.db')
            c = conn.cursor()
            c.execute(
                'SELECT eventname,class,detail FROM ENL_tianjin WHERE eventnum = ?;', (num,))
            result = c.fetchone()
            conn.close()
            name = result[0]
            status = result[1]
            conn = sqlite3.connect('jarviscatbot.db')
            c = conn.cursor()
            c.execute('SELECT count(*) FROM ' + name + str(num) +
                      ' WHERE id = ?;', (update.message.from_user.id,))
            asker = c.fetchone()[0]
            c.close()
            if not asker:
                if status == 'HQ' and (
                    not user_date.ENL_tianjin_HQ.user_list.inornot(
                        update.message.from_user.id)):
                    bot.sendMessage(
                        update.message.from_user.id,
                        text='并没有编号为' + str(num) + '的活动')
                    continue
                else:
                    n = 0
                    while n < len(result[2]):
                        if result[2][n] == '\n':
                            detail = result[2][:n]
                            break
                        else:
                            n += 1
            else:
                detail = result[2]
            bot.sendMessage(
                update.message.from_user.id,
                text=name + '\n' + detail)
        except (IndexError, ValueError, TypeError):
            bot.sendMessage(
                update.message.from_user.id,
                text='并没有编号为' + str(num) + '的活动')


@al_in(user_date.ENL_tianjin)
def join(bot, update, args):
    log(update)
    if len(args) == 0:
        update.message.reply_text('请输入您要加入的活动的活动编号喵！')
        return
    for num in args:
        try:
            num = int(num)
            conn = sqlite3.connect('jarviscatbot.db')
            c = conn.cursor()
            c.execute(
                'SELECT eventnum,eventname,class FROM ENL_tianjin WHERE eventnum = ?;', (num,))
            result = c.fetchone()
            conn.close()
            status = result[2]
            eventname = result[1]
            tablename = result[1] + str(result[0])
        except (IndexError, ValueError, TypeError):
            bot.sendMessage(
                update.message.from_user.id,
                text='并没有编号为' + str(num) + '的活动')
            continue
        if status == 'close':
            bot.sendMessage(
                update.message.from_user.id,
                text='活动：' + eventname + ' 已经结束，无法继续报名')
            continue
        elif status == 'HQ' and (not user_date.ENL_tianjin_HQ.user_list.inornot(update.message.from_user.id)):
            bot.sendMessage(
                update.message.from_user.id,
                text='并没有编号为' + str(num) + '的活动')
            continue
        conn = sqlite3.connect('jarviscatbot.db')
        c = conn.cursor()
        try:
            c.execute(
                'INSERT INTO ' +
                tablename +
                '(id,holder) VALUES (?,0)',
                (update.message.from_user.id,
                 ))
            conn.commit()
            conn.close()
            bot.sendMessage(
                update.message.from_user.id,
                text='您已成功报名' +
                eventname +
                '活动，请耐心等待进一步通知')
            detail(bot, update, [num])
        except sqlite3.IntegrityError:
            bot.sendMessage(
                update.message.from_user.id,
                text='您已经报名过' +
                eventname +
                '活动，请耐心等待进一步通知')


@al_in(user_date.ENL_tianjin)
def unjoin(bot, update, args):
    log(update)
    if len(args) == 0:
        update.message.reply_text('请输入您要退出的活动的活动编号喵！')
        return
    for num in args:
        try:
            num = int(num)
            conn = sqlite3.connect('jarviscatbot.db')
            c = conn.cursor()
            c.execute(
                'SELECT eventnum,eventname,class FROM ENL_tianjin WHERE eventnum = ?;', (num,))
            result = c.fetchone()
            conn.close()
            status = result[2]
            eventname = result[1]
            tablename = result[1] + str(result[0])
        except (IndexError, ValueError, TypeError):
            bot.sendMessage(
                update.message.from_user.id,
                text='并没有编号为' + str(num) + '的活动')
            continue
        if status == 'close':
            bot.sendMessage(update.message.from_user.id, text='你不能退出已经结束的活动哦~')
            continue
        elif status == 'HQ' and (not user_date.ENL_tianjin_HQ.user_list.inornot(update.message.from_user.id)):
            bot.sendMessage(
                update.message.from_user.id,
                text='并没有编号为' + str(num) + '的活动')
            continue
        conn = sqlite3.connect('jarviscatbot.db')
        c = conn.cursor()
        c.execute('SELECT COUNT(*)  FROM ' + tablename +
                  ' WHERE id = ?', (update.message.from_user.id,))
        if c.fetchone()[0]:
            c.execute('DELETE FROM ' + tablename +
                      ' WHERE id = ?;', (update.message.from_user.id,))
            conn.commit()
            conn.close()
            bot.sendMessage(
                update.message.from_user.id,
                text='您已成功退出' +
                eventname +
                '活动，如果改变心意请重新使用/join参加喵~')
        else:
            bot.sendMessage(
                update.message.from_user.id,
                text='您并没有加入' +
                eventname +
                '活动,不需要退出喵~')


@al_in(user_date.ENL_tianjin)
def holder(bot, update, args):
    log(update)
    try:
        tablenum = int(args[0])
        test = args[1]
    except (ValueError, IndexError):
        update.message.reply_text('请按照/holder 活动编号 用户 的格式输入命令喵~')
        return
    try:
        conn = sqlite3.connect('jarviscatbot.db')
        c = conn.cursor()
        c.execute(
            '''SELECT eventname,class FROM ENL_tianjin WHERE eventnum=?''', (tablenum,))
        result = c.fetchone()
        if result[1] == 'close':
            bot.sendMessage(
                update.message.from_user.id,
                text=result[0] +
                '活动已结束，无法添加其他主办者喵。')
            c.close()
            return
        tablename = result[0] + args[0]
        c.execute('SELECT holder FROM ' + tablename +
                  ' WHERE id=?', (update.message.from_user.id,))
        if not c.fetchone()[0]:
            bot.sendMessage(
                update.message.from_user.id,
                text='活动不存在或者你并不是本活动的主办者喵。')
            c.close()
            return
    except TypeError:
        bot.sendMessage(
            update.message.from_user.id,
            text='活动不存在或者你并不是本活动的主办者喵。')
        c.close()
        return
    members = trans_chat_id(update, args[1:])
    for member in members:
        c.execute('SELECT count(*) FROM ' +
                  tablename + ' WHERE id=?', (member,))
        try:
            if c.fetchone()[0]:
                c.execute('UPDATE ' + tablename +
                          ' SET holder=1 WHERE id=?', (member,))
                bot.sendMessage(
                    update.message.from_user.id,
                    text='已成功添加 ' +
                    user_date.alluser.username(member) +
                    ' 为 ' +
                    result[0] +
                    ' 活动的主办者。')
                bot.sendMessage(
                    member,
                    text='您已被添加为 ' +
                    result[0] +
                    ' 活动的主办者。')
        except TypeError:
            bot.sendMessage(
                update.message.from_user.id,
                text=user_date.alluser.username(member) +
                ' 还并未报名参加 ' +
                result[0] +
                ' 活动，无法添加。')


@al_in(user_date.ENL_tianjin)
def news(bot, update, args):
    log(update)
    try:
        tablenum = int(args[0])
    except (ValueError, IndexError):
        update.message.reply_text('请按照/news 活动编号 内容 的格式输入命令喵~')
        return
    news = ''
    for n in args[1:]:
        news += n + ' '
    if news == '':
        update.message.reply_text('您没有输入更新的内容喵~')
        return
    try:
        conn = sqlite3.connect('jarviscatbot.db')
        c = conn.cursor()
        c.execute(
            '''SELECT eventname FROM ENL_tianjin WHERE eventnum=?''', (tablenum,))
        name = c.fetchone()[0]
        tablename = name + args[0]
        c.execute(
            'SELECT id FROM ' +
            tablename +
            ' WHERE id=? and holder=1',
            (update.message.from_user.id,
             ))
        holder = user_date.alluser.username(c.fetchone()[0])
        c.execute(
            'SELECT detail FROM ENL_tianjin WHERE eventnum = ?', (tablenum,))
        detail = c.fetchone()[0] + '\n' + str(update.message.date +
                                              timedelta(hours=8)) + ' ' + holder + ' -- ' + news
        c.execute(
            'UPDATE ENL_tianjin SET detail =? WHERE eventnum = ?',
            (detail,
             tablenum))
        conn.commit()
        c.execute('SELECT id FROM ' + tablename +
                  ' WHERE id!=?', (update.message.from_user.id,))
        result = c.fetchall()
        conn.close()
        for n in result:
            bot.sendMessage(
                n[0],
                text=holder +
                ' 为您参加的活动 ' +
                name +
                ' 更新了新的内容:\n' +
                news)
    except TypeError:
        bot.sendMessage(
            update.message.from_user.id,
            text='活动不存在或者你并不是本活动的主办者喵。')


@al_in(user_date.ENL_tianjin)
def close(bot, update, args):
    log(update)
    if args == []:
        update.message.reply_text('请按照/close 活动编号 的格式输入命令喵~')
        return
    conn = sqlite3.connect('jarviscatbot.db')
    c = conn.cursor()
    for event in args:
        try:
            tablenum = int(event)
            c.execute(
                'SELECT eventname,class FROM ENL_tianjin WHERE eventnum=?', (tablenum,))
            result = c.fetchone()
            tablename = result[0] + event
            status = result[1]
            if status == 'close':
                bot.sendMessage(
                    update.message.from_user.id,
                    text=event + ' 活动已经结束了喵。')
                continue
            c.execute(
                'SELECT id FROM ' +
                tablename +
                ' WHERE id=? and holder=1',
                (update.message.from_user.id,
                 ))
            holder = user_date.alluser.username(c.fetchone()[0])
            c.execute(
                'SELECT detail FROM ENL_tianjin WHERE eventnum = ?', (tablenum,))
            detail = c.fetchone()[0] + '\n' + str(update.message.date +
                                                  timedelta(hours=8)) + ' ' + holder + ' -- 活动结束'
            c.execute(
                '''UPDATE ENL_tianjin SET class='close',detail =? WHERE eventnum = ?''',
                (detail,
                 tablenum))
            conn.commit()
            bot.sendMessage(
                update.message.from_user.id,
                text=str(
                    update.message.date +
                    timedelta(
                        hours=8)) +
                ' ' +
                holder +
                ' -- 活动结束')
        except (TypeError, ValueError):
            bot.sendMessage(
                update.message.from_user.id,
                text=event + ' 活动不存在或者你并不是本活动的主办者喵。')
            continue
    c.close()


@al_in(user_date.ENL_tianjin)
def reopen(bot, update, args):
    log(update)
    if args == []:
        update.message.reply_text('请按照/reopen 活动编号 的格式输入命令喵~')
        return
    conn = sqlite3.connect('jarviscatbot.db')
    c = conn.cursor()
    for event in args:
        try:
            tablenum = int(event)
            c.execute(
                'SELECT eventname,class FROM ENL_tianjin WHERE eventnum=?', (tablenum,))
            result = c.fetchone()
            tablename = result[0] + event
            status = result[1]
            if status != 'close':
                bot.sendMessage(
                    update.message.from_user.id,
                    text=event + ' 活动还没结束，无法重启喵。')
                continue
            c.execute(
                'SELECT id FROM ' +
                tablename +
                ' WHERE id=? and holder=1',
                (update.message.from_user.id,
                 ))
            holder = user_date.alluser.username(c.fetchone()[0])
            c.execute(
                'SELECT detail FROM ENL_tianjin WHERE eventnum = ?', (tablenum,))
            detail = c.fetchone()[0] + '\n' + str(update.message.date +
                                                  timedelta(hours=8)) + ' ' + holder + ' -- 活动重启'
            c.execute(
                '''UPDATE ENL_tianjin SET class='open',detail =? WHERE eventnum = ?''',
                (detail,
                 tablenum))
            conn.commit()
            bot.sendMessage(
                update.message.from_user.id,
                text=str(
                    update.message.date +
                    timedelta(
                        hours=8)) +
                ' ' +
                holder +
                ' -- 活动重启')
        except (TypeError, ValueError):
            bot.sendMessage(
                update.message.from_user.id,
                text=event + ' 活动不存在或者你并不是本活动的主办者喵。')
            continue
    c.close()


@idnum
def invite(bot, update, eventnum, userlist):
    log(update)
    if not user_date.ENL_tianjin_HQ.user_list.inornot(
            update.message.from_user.id):
        bot.sendMessage(
            update.message.from_user.id,
            text='抱歉你没有使用本功能的权限，请先申请对应模块的使用权限后再尝试此操作')
    try:
        tablenum = int(eventnum)
        conn = sqlite3.connect('jarviscatbot.db')
        c = conn.cursor()
        c.execute(
            'SELECT eventname,class FROM ENL_tianjin WHERE eventnum=?', (tablenum,))
        result = c.fetchone()
        tablename = result[0] + event
        status = result[1]
        if status == 'close':
            bot.sendMessage(
                update.message.from_user.id,
                text=event + ' 活动已经结束了喵。')
            return
        c.execute(
            'SELECT id FROM ' +
            tablename +
            ' WHERE id=? and holder=1',
            (update.message.from_user.id,
             ))
        holder = user_date.alluser.username(c.fetchone()[0])
        for member in userlist:
            c.execute('SELECT count(*) FROM ' +
                      tablename + ' WHERE id = ?', (member,))
            if not c.fetchone()[0]:
                c.execute('INSERT INTO ' + tablename +
                          '(id,holder) VALUES (?,0)', (member, ))
                conn.commit()
                bot.sendMessage(
                    member,
                    text='您已受邀加入 ' +
                    result[0] +
                    ' 活动，请使用/detail ' +
                    eventnum +
                    ' 查看活动详情')
        conn.close()
        bot.sendMessage(update.message.from_user.id, text='邀请完毕。')
    except (TypeError, ValueError):
        bot.sendMessage(
            update.message.from_user.id,
            text=eventnum +
            ' 活动不存在或者你并不是本活动的主办者喵。')


@al_in(user_date.ENL_tianjin)
def showlist(bot, update, args):
    log(update)
    if args == []:
        update.message.reply_text('请按照/showlist 活动编号 的格式输入命令喵~')
        return
    conn = sqlite3.connect('jarviscatbot.db')
    c = conn.cursor()
    for eventnum in args:
        try:
            tablenum = int(eventnum)
            c.execute(
                'SELECT eventname FROM ENL_tianjin WHERE eventnum=?', (tablenum,))
            name = c.fetchone()[0]
            tablename = name + eventnum
            if tablenum == 0 and user_date.ENL_tianjin_HQ.user_list.inornot(
                    update.message.from_user.id):
                pass
            else:
                c.execute(
                    'SELECT id FROM ' +
                    tablename +
                    ' WHERE id=? and holder=1',
                    (update.message.from_user.id,
                     ))
                holder = user_date.alluser.username(c.fetchone()[0])
            c.execute(
                'SELECT username,holder,agentname,level,' +
                tablename +
                '.id FROM ' +
                tablename +
                ' LEFT OUTER JOIN ENL_agent ON ENL_agent.id= ' +
                tablename +
                '.id')
            result = c.fetchall()
            text = 'agent list for the event ' + eventnum + ' :' + name + '\n' + \
                'username'.ljust(20) + '|' + '身份'.ljust(6) + '|' + '特工名'.ljust(17) + '|' + '等级'
            for m in result:
                if m[0]:
                    username = m[0]
                    agentname = m[2]
                elif user_date.alluser.username(m[4]) == 'unknow':
                    username = str(m[4])
                    agentname = 'unknow'
                else:
                    username = user_date.alluser.username(m[4])
                    agentname = 'unknow'
                if m[1]:
                    status = 'holder'
                else:
                    status = ''
                text += '\n' + username.ljust(20) + '|' + status.ljust(
                    8) + '|' + agentname.ljust(20) + '|' + str(m[3])
            bot.sendMessage(update.message.from_user.id, text=text)
        except (TypeError, ValueError):
            bot.sendMessage(
                update.message.from_user.id,
                text=eventnum +
                ' 活动不存在或者你并不是本活动的主办者喵。')
            continue
    conn.close()


@al_in(user_date.me)
def event_del(bot, update, args):
    log(update)
    if args[-1] != config.keyuser:
        bot.sendMessage(update.message.from_user.id,
                        text=' 删除操作事关重大，请按照/event_del 活动编号 执行密码的格式输入喵')
        return
    conn = sqlite3.connect('jarviscatbot.db')
    c = conn.cursor()
    for eventnum in args[:-1]:
        try:
            tablenum = int(eventnum)
            if tablenum == 0:
                bot.sendMessage(
                    update.message.from_user.id,
                    text='MU申请功能可是不能删除的永久设定哦大猫，你疯了吗~')
                continue
            c.execute(
                'SELECT eventname FROM ENL_tianjin WHERE eventnum=?', (tablenum,))
            tablename = c.fetchone()[0] + eventnum
            c.execute(
                'DELETE FROM ENL_tianjin WHERE eventnum = ?;', (tablenum,))
            c.execute('DROP TABLE ' + tablename)
            conn.commit()
            bot.sendMessage(
                update.message.from_user.id,
                text=eventnum + ' 活动已成功移除。')
        except (TypeError, ValueError):
            bot.sendMessage(
                update.message.from_user.id,
                text=eventnum + ' 活动不存在喵。')
            continue
    conn.close()


@al_in(user_date.me)
def event_rm(bot, update, args):
    log(update)
    if args[-1] != config.keyuser or len(args) < 3:
        bot.sendMessage(update.message.from_user.id,
                        text=' 删除操作事关重大，请按照/event_rm 活动编号 用户 执行密码的格式输入喵')
        return
    try:
        tablenum = int(args[0])
        conn = sqlite3.connect('jarviscatbot.db')
        c = conn.cursor()
        c.execute(
            'SELECT eventname FROM ENL_tianjin WHERE eventnum=?', (tablenum,))
        result = c.fetchone()
        tablename = result[0] + args[0]
    except (TypeError, ValueError):
        bot.sendMessage(update.message.from_user.id, text=args[0] + ' 活动不存在喵。')
        return
    for member in args[1:-1]:
        try:
            member = int(member)
        except ValueError:
            if user_date.alluser.chat_id(member) == 'unknow':
                update.message.reply_text(
                    '小猫无法在数据库中找到用户 ' +
                    member +
                    ' 请让他使用/start启动本猫后再试或者直接使用chat_id进行权限操作')
                continue
            else:
                member = user_date.alluser.chat_id(member)
        c.execute('DELETE FROM ' + tablename + ' WHERE id=?', (member, ))
        conn.commit()
        bot.sendMessage(
            update.message.from_user.id,
            text='已从 ' +
            result[0] +
            ' 中移出 ' +
            user_date.alluser.username(member))
    conn.close()

@al_in(user_date.ENL_tianjin_HQ)
def data(bot, update, args):
    log(update)
    conn = sqlite3.connect('jarviscatbot.db')
    c = conn.cursor()
    if args == []:
        c.execute('''SELECT id,dataname FROM ENL_HQ''')
        result = c.fetchall()
        text = '编号|内容'
        for info in result:
            text += '\n' + str(info[0]).ljust(4) + '|' + info[1]
        bot.sendMessage(update.message.from_user.id, text=text)
    else:
        for num in args:
            try:
                n = int(num)
                c.execute(
                    '''SELECT  dataname,datalink FROM ENL_HQ WHERE id=?''', (n,))
                data = c.fetchone()
                bot.sendMessage(
                    update.message.from_user.id,
                    text=data[0] + '\n' + data[1])
            except (ValueError, TypeError):
                bot.sendMessage(
                    update.message.from_user.id,
                    text='没有编号为' + num + '的项目喵')


@al_in(user_date.me)
def data_new(bot, update, args):
    log(update)
    if len(args) < 2:
        bot.sendMessage(
            update.message.from_user.id,
            text='请按照/data_new 项目名称/编号 项目链接 的格式好好输入喵~')
        return
    conn = sqlite3.connect('jarviscatbot.db')
    c = conn.cursor()
    try:
        id = int(args[0])
        c.execute('''SELECT dataname FROM ENL_HQ WHERE id=?''', (id,))
        dataname = c.fetchone()[0]
        c.execute(
            '''UPDATE ENL_HQ SET datalink=? WHERE eventnum=?''', (args[1], id))
        conn.commit()
        bot.sendMessage(
            update.message.from_user.id,
            text=dataname +
            '项目的链接信息已更新完毕喵~')
    except TypeError:
        bot.sendMessage(
            update.message.from_user.id,
            text='没有编号为' +
            args[0] +
            '的项目，请输入一个项目名以添加该项喵~')
    except ValueError:
        c.execute(
            '''INSERT INTO ENL_HQ(dataname,datalink) VALUES(?,?) ''',(args[0],args[1]))
        conn.commit()
        bot.sendMessage(update.message.from_user.id, text=args[0] + '项目已添加完毕喵')


@al_in(user_date.me)
def data_del(bot, update, args):
    log(update)
    if args == []:
        bot.sendMessage(update.message.from_user.id, text='请好好输入要删除的项目喵')
        return
    conn = sqlite3.connect('jarviscatbot.db')
    c = conn.cursor()
    for num in args:
        try:
            n = int(num)
            c.execute('''DELETE FROM ENL_HQ WHERE id=?''', (n,))
            conn.commit()
            bot.sendMessage(update.message.from_user.id, text='删除成功喵')
        except (ValueError, TypeError):
            bot.sendMessage(
                update.message.from_user.id,
                text='没有编号为' + num + '的项目喵')

def group_link(bot,update,args):
    log(update)
    if  update.message.chat_id>0:
        update.message.reply_text('本功能只能在组群中使用喵～')
        return
    try:
        tablenum = int(args[0])
    except (ValueError, IndexError):
        update.message.reply_text('请按照/group_link 活动编号 的格式好好输入喵～')
        return
    admin_list=[]
    for member in update.effective_chat.get_administrators():
        admin_list.append(member.user)
    if update.message.from_user not in admin_list:
        update.message.reply_text('只有群管理员才可以使用本功能喵～')
        return
    if not tablenum:
        update.message.reply_text('本活动不支持绑定组群功能喵～')
        return
    conn = sqlite3.connect('jarviscatbot.db')
    c = conn.cursor()
    c.execute(
        'SELECT eventname FROM ENL_tianjin WHERE groupid=?', (update.message.chat_id,))
    try:
        al_event = c.fetchone()[0]
        update.message.reply_text('本群已经绑定了 '+al_event+' 活动了，不能重复绑定喵～')
        return
    except TypeError:
        pass
    c.execute(
        'SELECT eventname FROM ENL_tianjin WHERE eventnum=?', (tablenum,))
    result = c.fetchone()
    try:
        tablename = result[0] + args[0]
    except TypeError:
        update.message.reply_text('活动不存在或者您并不是主办者喵～')
        return
    c.execute(
        'SELECT holder FROM '+tablename+' WHERE id=?', (update.message.from_user.id,))
    holder_check = c.fetchone()
    try:
        if not holder_check[0]:
            update.message.reply_text('活动不存在或者您并不是主办者喵～')
            return
    except TypeError:
        update.message.reply_text('活动不存在或者您并不是主办者喵～')
        return
    c.execute(
        '''UPDATE ENL_tianjin SET groupid=? WHERE eventnum = ?''', (tablenum,))
    conn.commit()
    c.close()
    update.message.reply_text('本群已经成功绑定 '+result[0]+' 活动喵～')

