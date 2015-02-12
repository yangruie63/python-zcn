# -*- coding: utf-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import urllib2  
import  re
from bs4 import BeautifulSoup



class Book():
	def __init__(self,bookName,bookUrl,bookCurPrice):
		self.bookName = bookName
		self.bookUrl = bookUrl
		self.bookCurPrice = bookCurPrice
			



def read_properties(file_name):
	f = open(file_name, 'r')
	config = {}
	for line in f.readlines():
		if(line[0] != '#' and len(line)>1):
			entry = line.split('=')
			config[entry[0]] = entry[1].strip()
	f.close()
	return config


def read_xml(file_name):
	f = open(file_name, 'r')
	xml_content = f.read().decode('utf-8')
	soup = BeautifulSoup(xml_content)
	books = soup.find_all('books')[0].find_all('book')
	
	print books




def sendMail():
	mail_config = read_properties('email_config.properties')
	content = mail_config['content'];
	content = content.replace('${book_name}','《哲学的慰藉》')
	content = content.replace('${book_price}','18')
	
	msg = MIMEText(content, 'plain', 'utf-8')
	msg['From'] = mail_config['from']
	msg['Subject'] = mail_config['subject']

	server = smtplib.SMTP(mail_config['smtp_server'], 25)
	#server.set_debuglevel(1)
	server.login(mail_config['username'], mail_config['password'])
	server.sendmail(mail_config['username'], [mail_config['to_addr']], msg.as_string())
	server.quit()



def search_book_price():
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	opener.addheaders = [('Accept-Charset', 'utf-8')]
	response = opener.open('http://www.amazon.cn/%E5%93%B2%E5%AD%A6%E7%9A%84%E6%85%B0%E8%97%89-%E9%98%BF%E5%85%B0%C2%B7%E5%BE%B7%E6%B3%A2%E9%A1%BF/dp/B00JM2HNVG/ref=sr_1_1?ie=UTF8&qid=1423709296&sr=8-1&keywords=%E5%93%B2%E5%AD%A6%E7%9A%84%E6%85%B0%E8%97%89')
	html_contents = response.read().decode('utf-8')
	soup = BeautifulSoup(html_contents)
	kindle_text = soup.find_all(attrs={"class": "priceLarge"})
	print kindle_text[0].get_text()
	kindle_price = re.findall(r'(\d+\.\d+)',kindle_text[0].get_text())
	print kindle_price[0]


if(__name__=='__main__'):
	#sendMail()
	#search_book_price()
	read_xml('book_config.xml')