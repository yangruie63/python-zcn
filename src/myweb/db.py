# -*- coding: utf-8 -*-
import MySQLdb

'''User对象'''
class User():
	def __init__(self,id,name):
		self.id = int(id)
		self.name = name
	def __str__(self):
		return 'id:%d,name:%s'%(self.id,self.name)
	__repr__=__str__


'''返回user对象数组'''
def selectById(id=None):

	conn=MySQLdb.connect(host='localhost',user='user1',passwd='123',port=3306,db='python')

	cur=conn.cursor()

	if(id != None):
		cur.execute('select * from user where id=%d'%int(id))
	else:
		cur.execute('select * from user')

	rs = cur.fetchall()

	list = []

	for i in range(len(rs)):
		user = User(rs[i][0],rs[i][1])
		list.append(user)

	return list

if(__name__=='__main__'):
	list = selectById()
	print list
