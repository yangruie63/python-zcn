# -*- coding: utf-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from bs4 import BeautifulSoup
from config import email_config
import smtplib
import urllib2  
import  re
import sys  
import time
import logging



"""设置python默认编码"""
reload(sys)
sys.setdefaultencoding('utf-8')

"""设置logging文件"""
logging.basicConfig(filename = email_config['log_dir'], level = logging.INFO, filemode = 'a',
	 format = '%(asctime)s - %(levelname)s: %(message)s')  


class Book():
	def __init__(self,bookName,bookUrl,oldPrice,lastPrice='0.00'):
		self.__bookName = bookName
		self.__bookUrl = bookUrl
		self.__oldPrice = float(oldPrice)
		self.__lastPrice = float(lastPrice)
	def getBookName(self):
		return self.__bookName
	def getBookUrl(self):
		return self.__bookUrl
	def getOldPrice(self):
		return self.__oldPrice
	def getLastPrice(self):
		return self.__lastPrice
	def setLastPrice(self,lastPrice):
		self.__lastPrice = float(lastPrice)
	def __str__(self):
		return '%s,%s,%s' %(self.__bookName,self.__oldPrice,self.__lastPrice)
	__repr__ = __str__




#返回BookList
def read_book_xml(file_name):
	f = open(file_name, 'r')
	xml_content = f.read().decode('utf-8')
	soup = BeautifulSoup(xml_content)
	books = soup.find_all('books')[0].find_all('book')
	result = []
	for x in books:
		bookName = x.findChildren("bookname")[0]
		bookUrl = x.findChildren("bookurl")[0]
		bookPrice = x.findChildren("bookprice")[0]
		book = Book(bookName.get_text(),bookUrl.get_text(),bookPrice.get_text())
		result.append(book)	
	f.close()
	return result



def sendMail(bookList):
	content_real = ""
	for book in bookList:
		content = email_config['content'];
		content = content.replace('${book_name}','《'+book.getBookName()+'》')
		content = content.replace('${book_price}',str(book.getOldPrice()))
		content = content.replace('${last_price}',str(book.getLastPrice()))
		content = content.replace('${book_url}',book.getBookUrl())
		content_real = content_real + content + "\n\n"
	msg = MIMEText(content_real, 'plain', 'utf-8')
	msg['From'] = email_config['from']
	msg['Subject'] = email_config['subject']

	server = smtplib.SMTP(email_config['smtp_server'], 25)
	#server.set_debuglevel(1)
	server.login(email_config['username'], email_config['password'])
	server.sendmail(email_config['username'], [email_config['to_addr']], msg.as_string())
	server.quit()
	print '邮件已发送！'

def write_log(log_txt):
	with open(email_config['log_dir'],'a') as f:
		f.write(log_txt+'\n')


def search_book_price(book):
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	opener.addheaders = [('Accept-Charset', 'utf-8')]
	try:
		response = opener.open(book.getBookUrl())
		html_contents = response.read().decode('utf-8')
		soup = BeautifulSoup(html_contents)
	except Exception, e:
		logging.error('《'+book.getBookName()+'》的url访问错误\n')
	kindle_text = soup.find_all(attrs={"class": "priceLarge"})
	kindle_price = re.findall(r'(\d+\.\d+)',kindle_text[0].get_text())
	return float(kindle_price[0])


"""
#返回配置文件数据
def read_properties(file_name):
	f = open(file_name, 'r')
	for line in f.readlines():
		if(line[0] != '#' and len(line)>1):
			entry = line.split('=')
			email_config[entry[0]] = entry[1].strip()
	f.close()
	return email_config
"""


def start():
	#获取需要监控的books
	books = read_book_xml("config/books.xml")
	log_txt = time.strftime("%Y-%m-%d %H:%M:%S")+"\n"
	for book in books:
		last_price = search_book_price(book)
		if last_price < book.getOldPrice():
			book.setLastPrice(last_price)
			log_txt = log_txt + '《%s》原价：%s，最新价格：%s' %(book.getBookName(),book.getOldPrice(),last_price) +"\n"
		else:
			log_txt = log_txt + '《%s》没有降价'% book.getBookName() +"\n"
	print log_txt
	write_log(log_txt)
	sendMail(books)

if(__name__=='__main__'):
	start();
	
	