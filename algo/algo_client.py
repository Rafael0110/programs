#!/usr/bin/env python
#coding: utf-8

import sys
import json
import socket
from time import sleep
from contextlib import closing

import algo_program
from algo_attack import whereCard
from algo_attack import selectCardRandom
from algo_attack import selectCardLR
from algo_attack import selectCardMid
from algo_attack import selectCardAgent

funcs =  {'agent'		: selectCardAgent,
         	'random'	: selectCardRandom,
         	'LR'			:	selectCardLR,
         	'mid'			: selectCardMid}

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hands = []

def sendMsg(sendMsg):
	soc.send(json.dumps(sendMsg))

def recvMsg():
	recvMsg = json.loads(soc.recv(4096))
	return recvMsg

def main() :
	global hands

	while True:
		try:
			msg = recvMsg()
		except OSError: break

		if msg['_p'] == 'wait' :
			sendMsg({'_p':'wait'})

		elif msg['_p'] in ['init','end'] :
			sendMsg({'_p':'end'})

		elif msg['_p'] == 'attack' :
			print msg['funcs'][int(sys.argv[1])-1]
			numDat, colDat, cards = algo_program.main(msg['card'],msg['attack'],msg['num'])
			sentmsg = {'_p':'attack','status':'continue'}
			sentmsg['player'], sentmsg['where'], sentmsg['num'] = whereCard(numDat, colDat, msg['card'], msg['num'], msg['count'])
			if (-1,-1) == (sentmsg['where'], sentmsg['num']) :
				sendMsg({'_p':'end'})
			else :
				sentmsg['select'] = funcs[msg['funcs'][int(sys.argv[1])-1]](msg['num'], msg['card'], msg['attack'])

				sentmsg['name'] = msg['funcs'][int(sys.argv[1])-1]
				sentmsg['to']   = msg['funcs'][sentmsg['player']]
				sendMsg(sentmsg)

		elif msg['_p'] == 'result' :
			if msg['result'] 	: sendMsg({'_p':'attack','status':'challenge'})
			else 							: sendMsg({'_p':'end'})

		elif msg['_p'] == 'turn' :
			sendMsg({'_p':'attack','status':'challenge'})

		elif msg['_p'] == 'break' : break

		else :
			continue

	sendMsg({'_p':"break"})
	soc.close()

if __name__ == "__main__" :
	soc.connect(("localhost", 50007))
	sleep(0.5)
	sendMsg({'name':int(sys.argv[1])-1})
	# print "your name >",
	# soc.send(json.dumps({'name':raw_input()}))

	main()