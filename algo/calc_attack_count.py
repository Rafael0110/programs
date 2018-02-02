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
	with open('countAttack.txt','r') as rf :
		line = ['' for i in range(2)]
		for i,j in zip(rf,range(2)) : line[j] = i
		num = line[0].split(',')
		cha = [[int(num[i + j * 4]) for i in range(4)] for j in range(4)]
		num = line[1].split(',')
		suc = [[int(num[i + j * 4]) for i in range(4)] for j in range(4)]
	return cha,suc

def outputList(listCha,listSuc) :
	with open('countAttack.txt','w') as wf :
		for List in [listCha,listSuc] :
			for i in range(4) :
				for j in range(4) :
					wf.write(str(List[i][j]))
					if i == j == 3 :
						wf.write('\n')
					else :
						wf.write(',')

namesList = ['random', 'LR', 'mid', 'agent']
names = {'random':0, 'LR':1, 'mid':2, 'agent':3}

countChallenge = [[0 for i in range(4)] for i in range(4)]
countSuccess   = [[0 for i in range(4)] for i in range(4)]
countPar			 = [[0.0 for i in range(4)] for i in range(4)]
sumChaTate = [0 for i in range(4)]
sumChaYoko = [0 for i in range(4)]
sumSucTate = [0 for i in range(4)]
sumSucYoko = [0 for i in range(4)]
sumChaAll = 0
sumSucAll = 0
countChallenge,countSuccess = inputList()

with open(argv[1],'r') as f :
	for line in f:
		word = line.split(',')
		if word[1] != 'attack' : continue
		countChallenge[names[word[2]]][names[word[3]]] += 1
		if strtobool(word[4][:-1]) :
			countSuccess[names[word[2]]][names[word[3]]] += 1

for i in range(4) :
	for j in range(4) :
		if i == j : continue
		sumChaTate[i] += countChallenge[i][j]
		sumChaYoko[j] += countChallenge[i][j]
		sumChaAll 		+= countChallenge[i][j]
		sumSucTate[i] += countSuccess[i][j]
		sumSucYoko[j] += countSuccess[i][j]
		sumSucAll			+= countSuccess[i][j]

for i in range(4):
	for j in range(4) :
		if i == j : continue
		countPar[i][j] = float(countSuccess[i][j]) / float(countChallenge[i][j])

for i in namesList :
	print i,'\t',
	for j in namesList  :
		print '&& {:,}'.format(countChallenge[names[i]][names[j]]),
	print '&& {:,}'.format(sumChaTate[names[i]])
print 'sum\t',
for i in range(4) :
	print '&& {:,}'.format(sumChaYoko[i]),
print sumChaAll
print 

for i in namesList :

	for j in namesList  :
		print '& {:.3f}'.format(countPar[names[i]][names[j]]),
	print '& {:.3f}'.format(float(sumSucTate[names[i]])/float(sumChaTate[names[i]]))
for i in range(4) :
	print '& {:.3f}'.format(float(sumSucYoko[i])/float(sumChaYoko[i])),
print '& {:.3f}'.format(float(sumSucAll)/float(sumChaAll)),
print 

# with open(argv[1],'r') as f :
# 	for line in f:
# 		word = line.split(',')
# 		if word[1] != 'attack' : continue
# 		countChallenge[names[word[2]]][names[word[3]]] += 1
# 		if strtobool(word[4][:-1]) :
# 			countSuccess[names[word[2]]][names[word[3]]] += 1
# outputList(countChallenge,countSuccess)