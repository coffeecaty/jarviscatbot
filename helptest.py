def help()
 help='我现在还是一只小猫，我只支持以下几种功能：'
 hl=[]
 hl.append('/start 开始交互：')
 hl.append('/set 设置时间，格式为“秒 分 时 天”，以空格分隔，可由后向前缺省，如/set 60或/set 0 1均为1分钟')
 hl.append('/unset 取消已设置的闹钟')
 hl.append('/stc 给coffeecaty留言')
 hl.append('/sts 给summy留言')
 hl.append('/repeat 重复留言，格式为“留言 次数”，以空格分隔，次数省略则默认为3次，重要的事情说三次')
 hl.append('/help 显示本帮助')
 hl.append('/miao 叫')

 for n in hl:
     help=help+'\n'+n
 return help
