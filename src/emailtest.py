# -*- coding: utf-8 -*-
import sys
import email
print sys.path
print email.mime
msg = email.mime.text.MIMEText('hello, send by Python...', 'plain', 'utf-8')

# ����Email��ַ�Ϳ���:
from_addr = raw_input('From: ')
password = raw_input('Password: ')
# ����SMTP��������ַ:
smtp_server = raw_input('SMTP server: ')
# �����ռ��˵�ַ:
to_addr = raw_input('To: ')


server = smtplib.SMTP(smtp_server, 25) # SMTPЭ��Ĭ�϶˿���25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()