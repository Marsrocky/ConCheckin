# Monitor who has come to check in
import time
import requests
import json
import datetime

# Initialization
url = 'http://172.28.220.94/ipsapi/api/GetAllTargetsByMinute?minute=1'
# FLAG for whether attendance
attendance = []
file = open('record.txt', 'r')
text = file.read()
dic = json.loads(text)
for i in range(len(dic)):
	attendance.append(0)

# Monitor
# Current IPS data
print 'Welcome to Server Monitor...'
while True:
	r = requests.get(url)
	text = r.text
	dic = json.loads(text)

	total = []
	for item in dic:
		total.append(item['mac'])

	# Database
	file = open('record.txt', 'r')
	text = file.read()
	dic = json.loads(text)
	count = 0
	for item in dic:
		# compare the mac to the total list
		for j in total:
			if item['mac'] == j and attendance[count] == 0:
				print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
				print item['name'], 'has checked in!'
				attendance[count] = 1
				print ' '

	time.sleep(10)
