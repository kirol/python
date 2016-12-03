#!/usr/bin/python

import simplejson
import zlib
import base64
from myprocess import *

def readPayloadJson(tmp, txtStr):
        #Load data to payloadContent dictionary
        with open(tmp + 'payload.json') as f:
                payloadContent = simplejson.loads(f.read())

        #Load data to list
                payloadData = payloadContent.get(txtStr)
        return payloadData

# Decode base64 then gunzip
def convertFile(data):
        decoded = zlib.decompress(base64.decodestring(data),zlib.MAX_WBITS|32)
        return decoded

# Compare SmartData against payload.json
def smartPayload(tmp):
        #Load data from payload.json to payloadSmart list
        payloadSmart = readPayloadJson(tmp, "SmartData")

        payloadDict = {}
        for i in range(len(payloadSmart)):
                payloadDict[str(payloadSmart[i].get('id'))] = payloadSmart[i].get('value')
	
	# Read data from smart.dat
        smartDict = {}
        with open(tmp + 'smart.dat') as file2:
                for line in file2:
                        k,v = line.strip().split('=')
                        smartDict[k] = v
        if payloadDict == smartDict:
                print('PASSED')
        else:
                print('FAILED')

# Compare VendorData against payload.json
def vendorPayload(ip, password, tmp):
        #Load data to payloadVendor list
        payloadVendor = readPayloadJson(tmp, "VendorData")
        payloadDict = {}
        for i in range(len(payloadVendor)):
                payloadDict[payloadVendor[i].get('VendorId')] = payloadVendor[i].get('Data')

	disk_model = model(ip, password, tmp)
	if disk_model == 'WD':
		decodedIfhm = convertFile(payloadDict.get("ifhm"))
		decodedDrm = convertFile(payloadDict.get("drm"))
		
		with open(tmp + 'hddVendorData.ifhm') as f1:
			originalIfhm = f1.read()

		with open(tmp + "hddVendorData.drm") as f2:
			originalDrm = f2.read()

		if(originalDrm==decodedDrm):
			print("drm: PASSED")
		else:
			print("drm: FAILED")

		if(originalIfhm==decodedIfhm):
			print("ifhm: PASSED")
		else:
			print("ifhm: FAILED")

	elif disk_model == 'ST':
		decodedSM2 = convertFile(payloadDict.get("SM2"))
		decodedUDS = convertFile(payloadDict.get("UDS"))
		
		with open(tmp + 'hddVendorData.SM2') as f3:
			originalSM2 = f3.read()

		with open(tmp + 'hddVendorData.UDS') as f4:
			originalUDS = f4.read()

		if originalSM2 == decodedSM2:
			print("SM2: PASSED")
		else:
			print("SM2: FAILED")

		if originalUDS == decodedUDS:
			print("UDS: PASSED")
		else:
			print("UDS: FAILED")


