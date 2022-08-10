
from peewee import *

db = SqliteDatabase('users.sqlite')



class Users(Model):
    id = PrimaryKeyField(unique=True)
    vip = BooleanField(null=False,default=False)
    usage = TextField()
    class Meta:
        database = db

def statq():
    with  db:
        io=0
        for user in Users.select(Users.id):
            io +=1
    return io

def check(_id):
    with db:
        return Users.select(1).where(Users.id == _id).exists()

def new_user(_id):
    with  db:
        Users.create(id=_id, vip=False,usage='У вас еще нет сохраненных CC')


def del_cc(_id,cc):
    with db:
        usa = Users.get(id=_id).usage
        list_usa=usa.split('/')
        new=''
        for i in list_usa:
            print(i,cc)
            if i != cc:
                new = new+'/'+i
        new.split('/',maxsplit=1)
        try:
            Users.update(usage=new).where(Users.id ==_id).execute()
            return True
        except:
            return False



def add_cc(_id,cc):
    with db:
        usa = Users.get(id=_id).usage
        if usa != 'У вас еще нет сохраненных CC\nby @SMOKE_SOFTWARE':
            us = usa + '/' + cc
            Users.update(usage=us).where(Users.id ==_id).execute()
        else:
            us = '/' + cc
            Users.update(usage=us).where(Users.id ==_id).execute()

def my_cc(_id):
    with db:
        d = Users.get(id=_id).usage
        return d.split('/')