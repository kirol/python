#!/usr/bin/python

import logging

class mylog():
	def __init__(self,message):
		self.message = message
		logging.basicConfig(filename='/var/log/messages',level=logging.DEBUG,format='%(asctime)s - %(levelname)s - HDDHealthMonitoring - %(message)s')
		logging.getLogger("paramiko").setLevel(logging.WARNING)

	def info(self):
		logging.info(self.message)

	def error(self):
		logging.error(self.message)
