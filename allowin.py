
def al_in(admin):
    def decorator(func):
     def wrapper(*args, **kw):
      if args[1].message.chat_id in admin.list:
       return func(*args, **kw)
      else:
       return args[1].message.reply_text('抱歉你没有使用'+admin.name+'类功能的权限，请使用/apply命令向coffeecaty申请使用权限')
     return wrapper
    return decorator

           
