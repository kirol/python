#!/usr/bin/python

import sys
import argparse
import subprocess

def main(sysArgs):
        global args
        parser = argparse.ArgumentParser()
        parser.add_argument("-a","--all",action="store_true",help="Run all tests")
        parser.add_argument("-t","--test",action="append",help="Run this test")
        args = parser.parse_args()

        if args.all:
                print "Running all tests"
                proc = subprocess.Popen(['python -m unittest discover TestCases/'] \
                ,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                procOutput, procError = proc.communicate()
                if proc.returncode != 0:
                        print('Error')
                        print(procError)
                else:
                        print("Success")
                        print(procOutput)
        else:
                print "Running selected tests"
                print(vars(args)["test"][0])
                input = vars(args)["test"][0]
                proc = subprocess.Popen(['python -m unittest TestCases.' + input] \
                ,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                procOutput, procError = proc.communicate()
                if proc.returncode != 0:
                        print('Error')
                        print(procError)
                else:
                        print("Success")
                        print(procOutput)

main(sys.argv)
