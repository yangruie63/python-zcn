# -*- coding: utf-8 -*-

email_config={
	#邮件用户代理
	'username' : '410298530@qq.com',
	'password' : 'woshiyangrui012198',
	'smtp_server' : 'smtp.qq.com',

	#接受邮件地址
	'to_addr' : '410298530@qq.com',

	#邮件内容
	'from' : 'python电子书价格监控程序',
	'subject' : '亚马逊上电子书降价提醒',
	'content' : '您在亚马逊上关注的电子书${book_name}，原价：${book_price}，现价：${last_price}元，点此链接进行查看：${book_url}',

	#日志目录
	'log_dir' : 'd:/zcn_log.txt'
}