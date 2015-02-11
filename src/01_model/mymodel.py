 # -*- coding: utf-8 -*-

class People():
	def __init__(self,name,age):
		self.__name = name
		self.__age = age
	
	def printPeople(self):
		print "people:",self.__name,':',self.__age

	def getName(self):
		return self.__name

	def getAge(self):
		return self.__age

class Man(People):
	def __init__(self,name,age,dick):
		People.__init__(self,name,age)
		self.__dick = dick
	def printPeople(self):
		print 'man:',self.getName(),':',self.getAge(),':',self.__dick

class Woman(People):
	def __init__(self,name,age,mimi):
		People.__init__(self,name,age)
		self.__mimi = mimi
	def printPeople(self):
		print 'woman:',self.getName(),':',self.getAge(),':',self.__mimi

def onDate(man,woman):
	if(man.getAge()-woman.getAge()>=2):
		print 'date success!'
	else:
		print 'date fail!'

if __name__ == "__main__":

	p = People('yangrui',25)
	p.printPeople();

	m = Man('yangrui',28,18)
	m.printPeople();

	w = Woman('xiaohong',25,'C')
	w.printPeople();

	onDate(m,w)


