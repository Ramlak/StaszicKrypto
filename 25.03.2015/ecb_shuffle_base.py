#!/usr/bin/python
# Above line only if you run from Linux

from socket import create_connection
from Crypto.Cipher import AES
import json, re, telnetlib

def chunks(array, chunk_size=16):
	result = []
	for i in xrange(0, len(array), chunk_size):
		result.append(array[i:i+chunk_size])
	return result

class Connection(object):
	
	newline = "\n"

	def __init__(self, host, port):
		self.socket = create_connection([host, port])

	def recv(self, num=1024):
		return self.socket.recv(num)

	def recvuntil(self, delim):
		result = ""
		while not result.endswith(delim):
			result += self.recv(1)
		return result

	def recvline(self, delim=None):
		eol = self.newline
		if delim:
			eol = delim
		return self.recvuntil(eol)

	def send(self, string):
		self.socket.sendall(string)

	def sendline(self, string):
		self.socket.send(string + self.newline)

	def sendlineafter(self, recv_string, send_string):
		self.recvuntil(recv_string)
		self.sendline(send_string)

	def sendafter(self, recv_string, send_string):
		self.recvuntil(recv_string)
		self.send(send_string)

	def interactive(self):
		t = telnetlib.Telnet()
		t.sock = self.socket
		t.interact()

c = Connection("localhost", 9999)

user = "marcin"
password = "kalinowski"

print(user, password)

c.sendlineafter("user:", user)
c.sendlineafter("password:", password)

c.recvuntil("Your cookie length:")

length = int(re.findall(r"([0-9]+)", c.recvline())[0],10)

c.recvuntil("Your session cookie:")

cookie = c.recv(length)

c.sendlineafter("Cookie length:", str(length))
c.sendlineafter("Session cookie:", cookie)
c.interactive()