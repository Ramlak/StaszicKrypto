#!/usr/bin/python

# THIS IS ECB_SHUFFLE

from Crypto.Cipher import AES
import os, json
from sys import stdin, stdout

os.chdir("/home/malware/ecb_shuffle")

stdout = os.fdopen(stdout.fileno(), 'w', 0)
key = open("/dev/urandom", "rb").read(16)
flag = open("flag.txt", "rb").readline()

welcome_message = """
Welcome, stranger!
Login and enjoy nothing.
========================
"""
def enhex(string):
	return string.encode('hex')

def unhex(string):
	return string.decode('hex')

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

stdout.write(welcome_message)
stdout.write("Please register.\n")
stdout.write("user:")
credentials = {}
credentials['user'] = stdin.readline().strip()

if 'admin' in credentials['user']:
	stdout.write('You cannot register as admin!!!\n')
	exit()

stdout.write("password:")
credentials['password'] = stdin.readline().strip()
registered = True
to_encrypt = pad(json.dumps(credentials))
stdout.write("Your session cookie:"+enhex(cipher.encrypt(to_encrypt)) + "\n")

stdout.write("Please login.\n")

stdout.write("Session cookie:")

user_data = unhex(stdin.readline().strip())
stdin.flush()

if len(user_data) % 16 != 0:
	stdout.write("Must be multiple of 16!...Exiting\n")
	exit()

user_data = json.loads(unpad(cipher.decrypt(unpad(user_data))))

if 'admin' in user_data['user']:
	stdout.write("Welcome, my Lord!\n")
	stdout.write("Here is your flag: %s" % flag)
else:
	stdout.write("You are not our beloved admin, gtfo!\n")

stdout.write("Bye!\n")