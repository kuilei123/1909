from _sha1 import sha1
from datetime import datetime


import pymysql

from settings import dbParams
# 1.创建连接对象
conn=pymysql.Connect(**dbParams)

# 2.创建游标对象
cursor=conn.cursor()

# 创建库
# try:
#     sql="create database bbs default charset = utf8"
#
#     cursor.execute(sql)
#     conn.commit()
# except Exception as e:
#     print(e)
# finally:
#     cursor.close()
#     conn.close()


# 创建表
# try:
#
#     sql ="create table if not exists user(uid int primary key auto_increment,username varchar(30) unique,usertype enum('普通用户','管理员') default '普通用户',password  varchar(50) not null,regtime datetime,email varchar(30))"
#     cursor.execute(sql)
#     conn.commit()
# except Exception as e:
#     print(e)
# finally:
#     cursor.close()
#     conn.close()

# 用户注册
# try:
#     index_username = "select username from user"
#     username = input("用户名:")
#     while len(username)<2:
#         print("用户名长度小于2,请重新输入")
#         username = input("用户名:")
#     while username in index_username :
#         print("用户名存在,请重新输入")
#         username = input("用户名:")
#     usertype=input("用户类型:")
#     password=input("密码:")
#     email=input("邮箱:")
#     # 3.执行sql语句
#     sql="insert into user(username,usertype,password,regtime,email) values('{}','{}','{}','{}','{}')".format(username,usertype,sha1(password),datetime.now(),email)
#     print(sql)
#     # execute 执行后返回受影响的行数
#     result = cursor.execute(sql)
#     conn.commit()
#     print(result)
#     if result>0:
#         print("执行成功")
#     else:
#         print("执行失败")
# except Exception as e:
#     print(e)
#     conn.rollback() # 回滚
# finally:
#     # 4. 关闭游标和连接
#     cursor.close()
#     conn.close()

# 用户登录
# username = input("请输入用户名：")
# password = input("请输入密码：")
# password = sha1(password.encode('utf8')).hexdigest()
# print(username,password)
#
# sql = "select uid from user where username= %s and password= %s"
# print(sql)
#
# result = cursor.execute(sql,[username,password])
# print(result)
# print(cursor._executed)
#
# if result>0:
#     print("登录成功")
# else:
#     print("登录失败,重新登录")
#
# cursor.close()
# conn.close()


# 用户显示
# class DBHelper:
#     def __init__(self,params):
#         self.conn = pymysql.Connect(**params)
#         self.init_param()
#         self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
#     def __del__(self):
#         self.cursor.close()
#         self.conn.close()
#     def init_param(self):
#         self.params = {
#             'fields':'*',
#             'table':'',
#             'where':'',
#             'groupby':'',
#             'having':'',
#             'orderby':'',
#             'limit':''
#         }
#     def where(self,**kwargs):
#         ops = {
#             'ne':'!=',
#             'gt':'>',
#             'ge':'>=',
#             'lt':'<',
#             'le':'<=',
#             'contains':'like',
#             'in':'in',
#             'nin':'not in'
#         }
#         result = " where "
#         for key in kwargs:
#             keys = key.split("__")
#             if len(key)>1:
#                 op = ops[keys[1]]
#                 if isinstance(kwargs[key],str):
#                     result += keys[0] + op + "'" + kwargs[key] +"' and"
#                 else:
#                     result += keys[0] + op +kwargs[key] + 'and'
#             else:
#                 if isinstance(kwargs[key],str):
#                     result += keys[0] + "= '" + kwargs[key] + "' and"
#                 else:
#                     result += keys[0] + " = " + kwargs[key] + 'and'
#         result = result.strip('and')
#         self.params['where'] = result
#         return  self
#     def table(self,tables):
#         self.params['tables'] = tables
#         return self
#     def fields(self,fields):
#         self.params['fields'] = fields
#         return self
#     def select(self):
#         sql = "select {fields} from {tables} {where} {groupby} {having} {orderby} {limit}"
#         sql = sql.format(**self.params)
#         print(sql)
#         self.cursor.execute(sql)
#         self.init_param()
#         return self.cursor.fetchall()
#
# if __name__ == '__main__':
#     from settings import dbparams
#     db = DBHelper(dbparams)
#     date = db.table('user').fields('username,usertype,password,regtime,email').select()
#     print(date)
