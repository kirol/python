#!/usr/bin/python

from myprocess import *
from remoteSTB import *

import subprocess

def preCondition():
	print('###### You have to stop recording on STB before executing this test case ######')
	
        umsIp = raw_input("Input UMS's ip: ")
	ip, password = remoteSTB()
	
	tmp = tmpdir()
	model(ip,password,tmp)	
		
	# Turn off power saving in case of running STB overnight
	remotecmd(ip,password,'dt apdUser -set false')	

	# Stop maintanance tasks
	remotecmd(ip,password, 'dt setIdleTimeout -secs 7200')
	remotecmd(ip,password,'echo "keycode 670" > /var/viewer/keyc.tmp; dt keyPress -f /var/viewer/keyc.tmp')

	remotecmd(ip, password,'echo "%s ums.dtvce.com" >>  /etc/hosts' % (umsIp))
        remotecmd(ip, password, 'rm /var/viewer/hddVendorData.SM2 /var/viewer/hddVendorData.UDS /var/viewer/hddNextSend.dat /var/viewer/smart.dat /var/bob/payloads/hddhealthmonitoring/payload.json')
	remotecmd(ip, password, 'dt xc -action startAsAcquisition')
	
	upload(ip,password,'setup_certs.sh')		
	remotecmd(ip, password,'/var/viewer/setup_certs.sh')	

	remotecmd(ip,password, 'dt setIdleTimeout -secs 1')
	return ip, password



