#!/usr/bin/python

# THIS IS ECB_DECODE_STANDALONE

from Crypto.Cipher import AES
from random import SystemRandom
import socket

flag = open("ecb_decode_flag.txt", "rb").readline()

def setup():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(("localhost", 8888))
	s.listen(3)
	return s

welcome_message = """
Hi, this is our new simple encryption service.
It is very simple. In fact we don't support decryption :(
But I but you can retrieve our secret message anyway.
=========================================================
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

	while True:
		f.write("Your string:")
		user_string = f.readline().strip()
		string_to_encrypt = pad(user_string+flag)
		f.write("Encrypted strings:" + enhex(cipher.encrypt(string_to_encrypt)) + "\n")


s = setup()

while True:
	client, address = s.accept()
	print "{} connected".format(client.getpeername())
	try:
		handle_client(client.makefile("rw", bufsize=0))
	except socket.error:
		pass
	client.close()		