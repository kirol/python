#!/usr/bin/python

import time
import subprocess
import os
import datetime
import paramiko
import scp
import sys

from mylog import *

def localcmd(data):
# Excute local cmd on local pc. This function supports pipeline
	proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	procOutput, procError = proc.communicate()
	if procOutput:
		mylog(procOutput).info()
	if procError:
		mylog(procError).error()
	return procOutput, procError

def remotecmd(ip, passwd, data):
# Execute remote cmd on remote pc. This function supports pipeline
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(ip, username='root', password=passwd)
	stdout, stderr = ssh.exec_command(data)
	mylog(data).info()
	procOutput = stdout.readline()
	procError = stderr.readlines()
	if procOutput:
		mylog(procOutput).info()
	if procError:
		for line in procError:
			mylog(line).error()
	ssh.close()
	return procOutput


def download(ip, passwd, src, dest):
# Download file from STB to Linux
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(ip, username='root', password=passwd)
	
	mylog('Download %s from %s to %s' % (src, ip, dest)).info()	
	with scp.SCPClient(ssh.get_transport()) as transfer:
		try:
			transfer.get(src, dest)
		except Exception, e:
			print e
	ssh.close()

def upload(ip, passwd, src):
# Upload file from Linux to STB
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(ip, username='root', password=passwd)
	
	mylog('Upload %s' % (src)).info()	
	with scp.SCPClient(ssh.get_transport()) as transfer:
		try:
			transfer.put(src, '/var/viewer/')
		except Exception, e:
			print e
	ssh.close()

def tailcmd(ip, password):
# Poll STB's log
	tmp = tmpdir()
	proc = subprocess.Popen('sshpass -p "%s" ssh -o StrictHostKeyChecking=no root@%s "tail -F /var/viewer/messages.log"' % (password, ip), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	while True:
		proc.poll()
		procOutput = proc.stdout.readline()
		
		# If tail output is empty, poll it again. If tail output is not empty, check output for maintenance task.
		if procOutput == '':		
			continue
		else:
			if 'DiskMaintenance' in procOutput and 'start running' in procOutput:
				mylog(procOutput).info()
				print("Begin to sleep for 10 min")
				time.sleep(600)
				
				disk_model = model(ip, password, tmp)
				if disk_model == 'WD':
					download(ip, password, '/var/viewer/hddVendorData.ifhm', tmp)
					download(ip, password, '/var/viewer/hddVendorData.drm', tmp)
				elif disk_model == 'ST':
					download(ip, password, '/var/viewer/hddVendorData.SM2', tmp)
					download(ip, password, '/var/viewer/hddVendorData.UDS', tmp)

				download(ip, password, '/var/viewer/smart.dat', tmp)

			elif 'HddHealthMaintenanceTask' in procOutput and 'start running' in procOutput:
				print("Begin to sleep for 1 min")
				time.sleep(60)
				download(ip, password, '/var/bob/payloads/hddhealthmonitoring/payload.json', tmp)
				break
			
			elif 'GenieMaintenanceTask' in procOutput and 'start running' in procOutput:
				print('HddHealthMaintenanceTask did not run')
				break
			elif 'start running' in procOutput:
				remotecmd(ip, password, 'echo "keycode 670" > /var/viewer/keyc.tmp; dt keyPress -f /var/viewer/keyc.tmp')
	
	proc.kill()	
	return tmp

def tmpdir():
# Create tmp directory using current timestamp
	mydir = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
	os.makedirs(mydir)
	tmp = mydir + '/'
	return tmp

def model(ip, password, tmp):
# Get disk model
	Seagate = ['1CT162', '1ET162']
	Western = ['63C57Y0', '63UY4Y0']	
	download(ip, password, '/var/viewer/hdbmSMART.dat', tmp)

	with open(tmp + 'hdbmSMART.dat') as txtFile:
		content = txtFile.readlines()
	for line in content:
		if 'Model ID' in line:
			col1, col2 = line.split('-')
		
	if col2.rstrip() in Seagate:
		diskModel = 'ST'
		mylog('Supported ST disk').info()
	elif col2.rstrip() in Western:
		diskModel = 'WD'
		mylog('Supported WD disk').info()
	else:
		mylog('Unsupported disk model').error()
		sys.exit()
	return diskModel

def hddNextSendFile(nextSmartTime, nextVendorTime):
# Create hddNextSend.dat file on local 
	with open('hddNextSend.dat', 'w') as f:
		f.write('nextVendor=%s\nnextSmart=%s' % (nextVendorTime, nextSmartTime)) 
