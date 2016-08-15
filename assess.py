#!/usr/bin/python

import subprocess
import os
import sys
import argparse
import signal
import fileinput

def handler(signalnum, frame):
	print("\n")	
	sys.exit(0)

signal.signal(signal.SIGINT, handler)

def openFile(openF=None):
	global fo
	global dirFile
	if openF != None:
		while True:
			try:
				dirFile = raw_input("\nPlease input the location for the text file (e.g: /tmp): ")
				dirFile = dirFile + "/file.txt"
				fo = open(dirFile,"wb")
			except IOError:
				print("\tError: No such directory")
				continue
			else:
				print("\tThe file will be created at this location: " + dirFile)
				break
	else: 
		fo = open("file.txt","wb")
	
def initFile(initF=None):
	global fo
	global numLine
	if initF != None:
		numLine = 0
		while True:
			try: 
				numLine = int(raw_input("\nPlease input the number of lines that you want to write to the text file (This number of text lines must be between 1 and 1000: "))
			except ValueError:
				print("\tError: You must enter a valid integer (e.g: 3,4,5...) to continue")
				continue
			else:
				if 0 < numLine < 1001:
					break
				else:
					print("\tError: Please enter the number between 1 and 1000\n")
					continue	
	else:
		numLine = 3	
        for i in xrange(numLine):
			i = i + 1
			fo.write(str(i) + '|' + 'TestName' + str(i) + '|' + 'TestAddress' + str(i) + '\n')		

def replaceText():
	createdFile = os.getcwd() + "/file.txt"
	subprocess.call(["sed -i 's/2/4/2' " + createdFile], shell=True)

def closeFile():
	global fo
	fo.close()

def main(sysArgs):
	parser = argparse.ArgumentParser()
	parser.add_argument("-i","--interactive",action="store_true",help="Create a file uing specified info")
	args = parser.parse_args()
        
	if args.interactive:
		openFile(openF="i")
		initFile(initF="i")
		closeFile()
		print("\tThe " + dirFile + " with " + str(numLine) + " text lines are created");
	elif len(sys.argv) == 1:
		# No argument. Using default options.
		print("Create file.txt in current directory using default options\nTo create file.txt with different options, use ./assess.py -i or use ./assess.py -h for more info\n")
		openFile()
		initFile()
		closeFile()
		print("file.txt is created in directory " + os.getcwd() + "/\n")
		replaceText()
		print("Second line of file.txt was replaced")

if __name__ == '__main__':
	main(sys.argv) 
