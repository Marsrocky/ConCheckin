# Judge where the guest belongs to
import time, requests, json, datetime

# Define region
def getLocation(x, y):
	if x>0 and y>0:
		return 1

# Initialization
guest = []
location = []
url = 'http://172.28.220.94/ipsapi/api/GetTargetByMAC?MAC='
file = open('record.txt', 'r')
text = file.read()
dic = json.loads(text)
for i in range(1, len(dic)):
	guest.append(dic[i])
	location.append(0)


print 'Location Recorder:'
while True:
	for i in range(len(dic)-1):
		r = requests.get(url+guest[i]['mac'])
		temp = json.loads(r.text)
		try:
			templocation = getLocation(temp['x'], temp['y'])
			if templocation == location[i]:
				pass
			else:
				print guest[i]['name'], 'has come to room', templocation
				location[i] = templocation
		finally:
			pass

	time.sleep(2)