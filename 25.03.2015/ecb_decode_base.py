#!/usr/bin/python

from socket import create_connection
from Crypto.Cipher import AES
import telnetlib, string, sys

def enhex(string):
	return string.encode('hex')

def unhex(string):
	return string.decode('hex')

def chunks(array, chunk_size=16):
	result = []
	for i in xrange(0, len(array), chunk_size):
		result.append(array[i:i+chunk_size])
	return result

class Connection(object):
	
	def __init__(self, host, port, newline="\n"):
		self.socket = create_connection([host, port])
		self.newline = newline

	def recv(self, num=1024):
		return self.socket.recv(num)

	def recvuntil(self, delim):
		result = ""
		while not result.endswith(delim):
			result += self.recv(1)
		return result

	def recvline(self):
		return self.recvuntil(self.newline)

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


c = Connection("localhost", 8888)

charset = string.digits + string.lowercase + string.uppercase + "{}_\x00"

def encrypt_string(string):
	c.sendlineafter("Your string:", string)
	c.recvuntil("Encrypted strings:")
	return unhex(c.recvline().strip())

print encrypt_string("Shit is getting real.")
