# -*- coding: utf-8 -*-
import urllib2  


def get_html():
	book_url = "http://www.amazon.cn/s/ref=nb_sb_noss_1?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&url=search-alias%3Daps&field-keywords=%E5%93%B2%E5%AD%A6%E7%9A%84%E6%85%B0%E8%97%89&sprefix=%E5%93%B2%E5%AD%A6%E7%9A%84%E6%85%B0%E8%97%89%2Caps";
	response = urllib2.urlopen(book_url)  
	html = response.read() 
	return html


def parse_html():
	html = get_html()
	print html



if(__name__=='__main__'):
	parse_html()