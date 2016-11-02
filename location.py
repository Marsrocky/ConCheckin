# Judge where the guest belongs to
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

# Initialization
guest = []
location = []
spot = ['FYP room', 'UAV room', 'DIP room', 'Graduate Office', 'other region']
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
			templocation = getLocation(float(temp['x']), float(temp['y']))
			if templocation == location[i]:
				pass
			else:
				#Location is changed so update and print.
				print guest[i]['name'], 'has come to', spot[templocation]
				location[i] = templocation
		except:
			pass
		finally:
			pass

	time.sleep(2)