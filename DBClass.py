import mysql.connector as con


class Dbuser:

    def __init__(self):
        self.c = con.connect(host='localhost', user='***db_user***',
                             password='***your_db_password***', database='pythontest')
        query = 'create table if not exists user(userId int, userName Varchar(25), phone int, primary key(userId))'
        cur = self.c.cursor()
        cur.execute(query)

    def fetchAll(self):
        query = 'select * from user'
        cur = self.c.cursor()
        cur.execute(query)
        for i in cur:
            print(f'UserId : {i[0]} , UserName : {i[1]} , Phone no.: {i[2]}')

    def insertUser(self, userId, userName, phone):
        query = f'insert into user values{userId, userName, phone}'
        cur = self.c.cursor()
        cur.execute(query)
        self.c.commit()
        print('User Inserted')

    def updateUser(self, userName, phone, userId):
        query = f'update user set userName = "{userName}", phone = {phone} where userId = {userId}'
        cur = self.c.cursor()
        cur.execute(query)
        self.c.commit()
        print(query)
        print('user updated')

    def delUser(self, userId):
        query = f'delete from user where userId ={userId}'
        cur = self.c.cursor()
        cur.execute(query)
        self.c.commit()
        print(query)
        print('User Deleted')

    def fetchId(self, userId):
        query = f'select * from user where userId={userId}'
        cur = self.c.cursor()
        cur.execute(query)
        print(query)
        for i in cur:
            print(f'UserId : {i[0]} , UserName : {i[1]} , Phone no.: {i[2]}')
