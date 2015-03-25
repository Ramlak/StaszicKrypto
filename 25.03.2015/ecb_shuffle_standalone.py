#!/usr/bin/python

# THIS IS ECB_SHUFFLE_STANDALONE

from Crypto.Cipher import AES
import json
from random import SystemRandom
import socket

flag = open("ecb_shuffle_flag.txt", "rb").readline()

def setup():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(("localhost", 9999))
	s.listen(3)
	return s

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
	result = string + chr(add) * add
	return result

def unpad(string):
	result = string
	padding_chr = string[-1]
	for i in xrange(ord(padding_chr)):
		if string[-1 - i] == padding_chr:
			result = result[:-1]
		else:
			return string
	return result

def handle_client(f):
	key = "".join([SystemRandom().choice([chr(i) for i in xrange(0x100)]) for x in xrange(16)])
	cipher = AES.new(key, AES.MODE_ECB)

	f.write(welcome_message)
	f.write("Please register.\n")

	f.write("user:")

	credentials = {}
	credentials['user'] = f.readline().strip()

	if 'admin' in credentials['user']:
		f.write('You cannot register as admin!!!\n')
		return

	f.write("password:")
	credentials['password'] = f.readline().strip()

	to_encrypt = pad(json.dumps(credentials))
	f.write("Your session cookie:"+enhex(cipher.encrypt(to_encrypt)) + "\n")

	f.write("Please login.\n")
	f.write("Session cookie:")

	user_data = unhex(f.readline().strip())
	f.flush()

	if len(user_data) % 16 != 0:
		f.write("Must be multiple of 16!...Exiting\n")
		return

	user_data = json.loads(unpad(cipher.decrypt(unpad(user_data))))

	if 'admin' in user_data['us()er']:
		f.write("Welcome, my Lord!\n")
		f.write("Here is your flag: %s" % flag)
	else:
		f.write("You are not our beloved admin, gtfo!\n")

	f.write("Bye!\n")
	return

s = setup()

while True:
	client, address = s.accept()
	print "{} connected".format(client.getpeername())
	handle_client(client.makefile("rw", bufsize=0))
	client.close()