#!/usr/bin/python

# THIS IS ECB_SHUFFLE

from Crypto.Cipher import AES
import os, json
from sys import stdin, stdout

os.chdir("/home/malware/ecb_shuffle")

stdout = os.fdopen(stdout.fileno(), 'w', 0)
key = open("/dev/urandom", "rb").read(16)

def pad(string):
	add = (len(string)/16 + 1)*16 - len(string)
	result = string + "\x00" * add
	return result

def unpad(string):
	result = string
	while result.endswith("\x00"):
		result = result[:-1]
	return result

cipher = AES.new(key, AES.MODE_ECB)

stdout.write("user:")
credentials = {}
credentials['user'] = stdin.readline().strip()

if 'admin' in credentials['user']:
	stdout.write('You cannot log in as admin!!!\n')
	exit()

stdout.write("password:")
credentials['password'] = stdin.readline().strip()
registered = True
to_encrypt = pad(json.dumps(credentials))
stdout.write("Your cookie length:" + str(len(to_encrypt)) + "\n")
stdout.write("Your session cookie:"+cipher.encrypt(to_encrypt) + "\n")

stdout.write("Cookie length:")
try:
	length = int(stdin.readline().strip(), 10)
	stdin.flush()
except Exception:
	exit()

if length % 16 != 0:
	stdout.write("Must be multiple of 16!...Exiting\n")
	exit()

stdout.write("Session cookie:")

try:
	user_data = json.loads(unpad(cipher.decrypt(stdin.read(length))))
	stdin.flush()
except Exception:
	stdout.write("You fucked something!...Exiting\n")
	exit()

try:
	if 'admin' in user_data['user']:
		stdout.write("Welcome, my Lord!\n")
		stdout.write("Here is your flag: %s" % open("flag.txt").readline())
	else:
		stdout.write("You are not our beloved admin, gtfo!\n")
except Exception:
	stdout.write("Ehh, yes, you fucked again...Exiting\n")

stdout.write("Bye!\n")