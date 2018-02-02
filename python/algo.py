#!/usr/bin/env python
#coding: utf-8

import socket
import json
from contextlib import closing

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def send_msg(send_msg):
	soc.send(json.dumps(send_msg))
	recv_msg = json.loads(soc.recv(4096))
	print "send>",send_msg
	print "recv>",recv_msg
	return recv_msg

card_num = 3
players = 4
class card :
	num = 0
	col = ""
	open = False

def INITIALIZE() :
	global card_num
	for i in range(card_num) :
		DRAW()

def DRAW() :
	msg = {'_p':"request" , 'func':"draw"}
	msg.update({'type':"card"})
	msg.update({'from':"stock"})
	msg.update({'num':"1"})
	recv = send_msg(msg)

def ATTACK() :
	msg = {'_p':"request" , 'func':"attack"}
	msg.update({'type':"card"})
	target = "" # select actioned target
	msg.update({'success':["open","target"]})
	msg.update({'fail':["open","owner"]})
	while True :
		target = "" # select actioned target
		msg.update({'where':"target"})
		recv = send_msg(msg)
		if 'false' == recv['result'] : break

def main() :
	msg = {'_p':"request" , 'func':"start"}
	INITIALIZE()
	while msg['_p'] != 'end' :
		DRAW()
		ATTACK()
		msg = send_msg(msg)

if __name__ == "__main__" :
	soc.connect(("localhost", 50007))
	main()
	send_msg({'_p':"break"})
	soc.close()
