# -*- coding: utf-8 -*-
"""
Created on Wed Nov 02 13:09:10 2016

@author: jianf
Divide people to different region
"""

import os
import time, requests, json, datetime

def ifloc(x, y, loc):
	if x>=loc[0][0] and x<=loc[1][0] and y>=loc[0][1] and y<=loc[1][1]:
		return True
	else:
		return False

# Define region
def getLocation(x, y):
	fyp = [[0,0],[6.3,16.6]]	#0
	UAV = [[6.4,0],[16,16.6]]	#1
	DIP = [[16.3,0], [35.5,6.8]]	#2
	office = [[16.3,7], [35.5,16.6]]	#3
	tloc = [fyp, UAV, DIP, office]
	for i in range(4):
		if ifloc(x, y, tloc[i]):
			return i
	return 4	#other

# Intialization
spot = ['FYP room', 'UAV room', 'DIP room', 'Graduate Office', 'other region']
url = 'http://172.28.220.94/ipsapi/api/GetAllTargetsByMinute?minute=1'


while True:
	timestamp = ''
	total = 0
	region = [0, 0, 0, 0, 0]
	r = requests.get(url)
	temp = json.loads(r.text)
	for item in temp:
		timestamp = item['timestamp']
		iloc = getLocation(float(item['x']), float(item['y']))
		region[iloc] = region[iloc] + 1
		total = total + 1
	
	# output the result
	print '**************************************'
	print 'Time: ', timestamp
	for i in range(5):
		print spot[i]+':', region[i]
	print '**************************************'
	time.sleep(2)