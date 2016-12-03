#!/usr/bin/python

from myprocess import *
from remoteSTB import remoteSTB
from validateSchema import validateSchema
from validateData import readPayloadJson, convertFile, smartPayload, vendorPayload
from preCondition import preCondition

import os.path
import unittest

class CompareWithFiles(unittest.TestCase):
	def test_compareWithFiles(self):
		ip, password = preCondition()	
		#tmp = tailcmd(ip, password)
		if (os.path.isfile("$s/smart.dat %(tmp)") and os.path.isfile("$s/payload.json %(tmp)")) is True:
			print("\n================Validate payload.json file 's schema==================")
			validateSchema("$s/payload.json %(tmp)", "schema.json")
			print("\n================Validate payload.json file 's VENDOR data==================")
			#vendorPayload()
			print("\n================Validate payload.json file 's SMART data==================")
			#smartPayload()
		else:
			print("\nStill waiting")

