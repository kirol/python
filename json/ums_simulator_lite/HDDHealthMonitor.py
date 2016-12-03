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
	parser.add_argument("-a","--all",action="store_true",help="Auto all")
	parser.add_argument("-t","--test",action="append",help="Specify test to run by name, e.g: -t name without .py in name")
	parser.add_argument("-cwu","--compareWithUMS",action="store_true",help="Compare the values in payload.json with the contents UMS receives")
	args = parser.parse_args()
	
	if args.all:
		ip, password = remoteSTB()
		
		while True:
			procOutput1, procError1 = remotecmd(ip,password, 'grep "/var/viewer/messages.log" | while read line; do echo $line | grep --line-buffered "DiskMaintenance"; echo $?; done')
			if procOut1 == 0:
				print("Checking")
				break
		#	then sleep 600; killall sshpass; else sshpass -p %s ssh root@%s "echo "keycode 670" > /var/viewer/keyc.tmp; dt keyPress -f /var/viewer/keyc.tmp"; fi; done""" %(password,ip,password,ip)
		
		
		transferFile('/var/viewer/hddVendorData*')
		transferFile('/var/viewer/smart.dat')

		
		command2 = r"""sshpass -p """ + password + r""" ssh root@""" + ip + r""" 'tail -F /var/log/messages.log' | grep --line-buffered 'start running' | while read line; do echo $line | grep --line-buffered 'HddHealthMaintenanceTask'; if [ $? -eq 0 ]; then sleep 60; killall sshpass; else sshpass -p """ + password + r""" ssh root@""" + ip + r""" "echo "keycode 670" > /var/viewer/keyc.tmp; dt keyPress -f /var/viewer/keyc.tmp"; fi; done"""
		proc2Output, proc2Error = myproccess(command2)
		
		transferFile('/var/bob/payloads/hddhealthmonitoring/payload.json')
		
		if (os.path.isfile("smart.dat") and os.path.isfile("payload.json")) is True:
			print("\n================Validate payload.json file 's schema==================")
			validateSchema()
			print("\n================Validate payload.json file 's VENDOR data==================")
			vendorPayload()
			print("\n================Validate payload.json file 's SMART data==================")
			smartPayload()
		else:
			print("\nStill waiting")
			
	elif args.test:
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
