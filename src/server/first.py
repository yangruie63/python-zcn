# -*- coding: utf-8 -*-
import socket

HOST = ''
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print type(s)
s.bind((HOST, PORT))



