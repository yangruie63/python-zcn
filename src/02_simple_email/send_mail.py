# -*- coding: utf-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from read_config import read_config
import smtplib


def sendMail():
	
	data = read_config()

	content = data['content'];
	content = content.replace('${book_name}','《哲学的慰藉》')
	content = content.replace('${book_price}','18')
	
	msg = MIMEText(content, 'plain', 'utf-8')
	msg['From'] = data['from']
	msg['Subject'] = data['subject']

	server = smtplib.SMTP(data['smtp_server'], 25)
	#server.set_debuglevel(1)
	server.login(data['username'], data['password'])
	server.sendmail(data['username'], [data['to_addr']], msg.as_string())
	server.quit()

if(__name__=='__main__'):
	sendMail()