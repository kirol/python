#!/usr/bin/python

import sys
import os.path
import argparse
import subprocess
import unittest
import datetime

from myprocess import *
from remoteSTB import remoteSTB




def main(sysArgs):
	parser = argparse.ArgumentParser()
	parser.add_argument("-t","--test",action="append",help="Specify test to run by name, e.g: -t name without .py in name")
	
	args = parser.parse_args()
	
	
			
	if args.test:
		print("Running selected test")
		test = unittest.defaultTestLoader.loadTestsFromNames(args.test)
		testRunner = unittest.TextTestRunner()
		
		startime = datetime.datetime.now()		
		testRunner.run(test)
		stoptime = datetime.datetime.now()

		print("Test name: %s. Start time: %s.  Stop time: %s" %(args.test,startime,stoptime))

	else:
		print("Using --help or -h option for more info")

if __name__ == '__main__':
	main(sys.argv)
