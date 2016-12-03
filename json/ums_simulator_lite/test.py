#!/usr/bin/python

from remoteSTB import *
from myprocess import *
from validateData import *

ip,password = remoteSTB()
download(ip,password,'/opt/abc','/opt/')
