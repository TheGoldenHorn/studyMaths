import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

browser = webdriver.Firefox()
browser.get('http://www.math-shortcut-tricks.com/basic-math-shortcut-tricks/')
time.sleep(5)
file = open('math.txt','w+')
important = browser.find_element_by_xpath('.//aside[@id="text-3"]')
for link in important.find_elements_by_xpath('.//li'):
	file.write (link.find_element_by_xpath('.//a').text + '\n')
	file.write (link.find_element_by_xpath('.//a').get_attribute('href') + '\n \n')


file.close()

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass

    return i + 1


file=open("math.txt", "r")
if file.mode == 'r':
	max_count=file_len('math.txt')
	num=max_count
	for i in range (0, max_count):
		link=file.readline()
		print num
		print link
		num-=1
print "EOF"		
file.close()		