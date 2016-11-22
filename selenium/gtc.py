#!/usr/bin/python

import schedule
import time
from selenium import webdriver

def job():
	print("I'm working")
	driver = webdriver.Firefox()
	driver.get("http://youtube.com")
	driver.find_element_by_xpath(".//*[@id='yt-masthead-signin']/div/button").click()

job()

#schedule.every().day.at("22:38").do(job)

#while True:
	#schedule.run_pending()
	#time.sleep(1)
