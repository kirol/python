#!/usr/bin/python

from myprocess import *
from remoteSTB import *
from validateSchema import *
from validateData import *
from preCondition import *

import os.path
import unittest

class test(unittest.TestCase):
	def test_0204(self):
		ip, password = preCondition()	
		remotecmd(ip,password,'dt hddhm -voWd on -voSea on')
		tmp = tailcmd(ip, password)
		print("\n================Validate payload.json file 's schema==================")
		validateSchema(tmp)
		print("\n================Validate payload.json file 's VENDOR data==================")
		vendorPayload(ip,password,tmp)
		print("\n================Validate payload.json file 's SMART data==================")
		smartPayload(tmp)
