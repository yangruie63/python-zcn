# -*- coding: utf-8 -*-

def read_config():
	f = open('config.properties', 'r')
	config = {}
	for line in f.readlines():
		if(line[0] != '#' and len(line)>1):
			entry = line.split('=')
			config[entry[0]] = entry[1].strip()
	f.close()
	return config

