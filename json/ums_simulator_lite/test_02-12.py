#!/usr/bin/python

from myprocess import *
from remoteSTB import *
from validateSchema import *
from validateData import *
from preCondition import *

import os.path
import unittest

class test(unittest.TestCase):
	def test_0212(self):
		ip, password = preCondition()	
		remotecmd(ip,password,'dt hddhm -voWd on -voSea on')
		nextTime = remotecmd(ip,password,'echo $(($(date +%s)+60*60*24))')
		hddNextSendFile(nextTime.rstrip(),nextTime.rstrip())
		upload(ip,password,'hddNextSend.dat')
		tmp = tailcmd(ip, password)
		print("\n================Validate hddNextSend file==================")
		
