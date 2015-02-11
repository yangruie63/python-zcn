#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# ithomer.net
 
import sys
import os

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
 
from email.utils import COMMASPACE,formatdate
from email import encoders
 

server = {
          'name' : 'smtp.qq.com',
          'user' : '410298530@qq.com',
          'passwd' : 'woshiyangrui012198'
         }    


def send_mail(server, fro, to, subject, text, files=[]): 
    assert type(server) == dict 
    assert type(to) == list 
    assert type(files) == list 
 
    msg = MIMEMultipart() 
    msg['From'] = fro 
    msg['Subject'] = subject 
    msg['To'] = COMMASPACE.join(to) #COMMASPACE==', ' 
    msg['Date'] = formatdate(localtime=True) 
    msg.attach(MIMEText(text)) 
 
    for file in files: 
        part = MIMEBase('application', 'octet-stream') #'octet-stream': binary data 
        part.set_payload(open(file, 'rb').read()) 
        encoders.encode_base64(part) 
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file)) 
        msg.attach(part) 
 
    import smtplib 
    smtp = smtplib.SMTP(server['name']) 
    smtp.login(server['user'], server['passwd']) 
    smtp.sendmail(fro, to, msg.as_string()) 
    smtp.close()
    
    print("send email success!")


def printServer():
    name = server['name']
    user = server['user']
    passwd = server['passwd']
    
    print(name + ', ' + user + ', ' + passwd)
    
# main
if __name__ == "__main__":
    to = ["410298530@qq.com"]
#     to.append(str())
    
    files = []
    for i in range(5):
        filename = "file_" + str(i)
        f = open(filename, 'w+')
        f.write("i am ithomer.net " + str(i))
        f.close()
        files.append(filename)
    print files
    #files.append("getUrl.py")
    #files.append("getUrl.py")
    send_mail(server, server['user'], to, 'test python email', 'test from ithomer.net', files)