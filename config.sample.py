token='此处粘贴你的bot token'
yourid=贴入你的chat_id
loverid=贴入你的那个她的chat_id

class usergroup:
    __slots__ = ('name,list')
    def __init__(self,name,list=[]):
        self.name=name
    def checkout(self,checklist):
        n=0
        while n<len(checklist):
            if checklist[n] in self.list:
                checklist.pop(n)
            else:
                n=n+1
    def add(self,chat_id):
         if chat_id not in self.list:
             self.list.append(chat_id)
    def remove(self,chat_id):
         n=0
         while n<len(self.list):
             if self.list[n] ==chat_id:
                 self.list.pop(n)
                 break
             n=n+1
    def print(self,username):
         for n in self.list:
             if n in username[0]:
                 print(str(n)+' '+username[1][username[0].index(n)])
             else:
                 print(str(n)+' unknow')

alluser=([],[])
admin=usergroup(admin,[yourid])
superuser=usergroup(superuser,admin.list+[loverid])
decode=usergroup(decode,[superuser]+[])
