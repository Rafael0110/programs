#!/usr/bin/env python
#coding: utf-8

from sys import argv
from distutils.util import strtobool

def printList(List) :
	for i in namesList :
		print i,'\t',
		for j in namesList  :
			print '&&',List[names[i]][names[j]],
		print
	print 

def inputList() :
	with open('countVictory.txt','r') as rf :
		line = ['' for i in range(3)]
		Lists = [[] for i in range(3)]
		for i,j in zip(rf,range(3)) :
			line[j] = i
			num = line[j].split(',')
			Lists[j] = [int(num[i]) for i in range(4)]
		return Lists[0],Lists[1],Lists[2]

def outputList(v,vt,lt) :
	with open('countVictory.txt','w') as wf :
		for List in [v,vt,lt] :
			for i in range(4) :
				wf.write(str(List[i]))
				if i == 3 :
					wf.write('\n')
				else :
					wf.write(',')

namesList = ['random', 'LR', 'mid', 'agent']
names = {'random':0, 'LR':1, 'mid':2, 'agent':3}

countVict 		= [0 for i in range(4)]
countVictTurn = [0 for i in range(4)]
countLoseTurn = [0 for i in range(4)]
countVict, countVictTurn, countLoseTurn = inputList()

with open(argv[1],'r') as f :
	datas = {}
	for line in f:
		word = line.split(',')
		if word[0] == 'gamestart' :
			# print len(datas.keys()), datas
			if len(datas.keys()) == 4:
				for name in namesList :
					if datas[name]['result'] == 'win' :
						countVict[names[name]] 			+= 1
						countVictTurn[names[name]] 	+= int(datas[name]['turn'])
					else :
						countLoseTurn[names[name]] 	+= int(datas[name]['turn'])
			datas.clear()
		elif word[1] in ['win','lose'] :
			datas.update({word[2][:-1]:{'turn':word[0],'result':word[1]}})

print "vict\t",
victSum = 0
for i in range(4) :
	victSum += countVict[i]
	print '&& {}'.format(countVict[i]),
print '&& {}'.format(victSum)

print "victpar\t",
for i in range(4) :
	print '&& {:.2f}'.format(float(countVictTurn[i])/float(countVict[i])),
print 

print "losepar\t",
for i in range(4) :
	print '&& {:.2f}'.format(float(countLoseTurn[i])/float(victSum - countVict[i])),
print

print 
print countVict
print countVictTurn
print countLoseTurn



# outputList(countVict, countVictTurn, countLoseTurn)