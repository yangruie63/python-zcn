 # -*- coding: utf-8 -*-

'  test package  '

__author__ = 'yangrui'

import sys

def test():
	agrs = sys.argv
	if(len(agrs)==1):
		print 'hello,world!'
	elif (len(agrs)==2):
		print 'hello,',agrs[1]
	else:
		print '两个以上参数'

if __name__ == '__main__':
	test()