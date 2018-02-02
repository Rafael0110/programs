#!/usr/bin/env python
#coding: utf-8

from random import randint
import algo_program

def LRlist(num):
	list = []
	for i in range(num) :
		j = num - int(i) - 1
		if int(i) >= int(j) : return list 
		if 	randint(0,1) :
			list.append(int(i))
			list.append(int(j))
		else :
			list.append(int(j))
			list.append(int(i))


# アタック対象となるカードの選択
def whereCard(numDat, colDat, cards, num, count) :
	for i in range(len(cards)) :
		if i == num : continue
		for j in range(len(cards[i])) :
			if not (len(cards[i][j]) > 1) and numDat[i] and type(numDat[i][j]) is int : 
				return i,j,numDat[i][j]
	else :
		if not count :
			for i in range(len(numDat)) :
				if i == num : continue
				for j in range(len(numDat[i])) :
					if not (len(cards[i][j]) > 2) and type(numDat[i][j]) is list and len(numDat[i][j]) > 1 : 
						return i,j,numDat[i][j][randint(0,len(numDat[i][j]))-1]
		else : return -1,-1,-1

# アタックに使用するカードの選択

def selectCardRandom(num, hands, attack) :
	myhand = []
	for card in hands[num] :
		if len(card) == 2 : myhand.append(hands[num].index(card))
	if len(myhand) : return myhand[randint(0,len(myhand)-1)]
	else 					 : return myhand[0]

def selectCardLR(num, hands, attack) :
	myhand = []
	for card in hands[num] :
		if len(card) == 2 : myhand.append(hands[num].index(card))
	print myhand
	if randint(0,1) : return myhand[0]
	else 						: return myhand[-1]

def selectCardMid(num, hands, attack) :
	myhand = []
	for card in hands[num] :
		if len(card) == 2 : myhand.append(hands[num].index(card))
	mid = [[m,n] for m in range(len(myhand)) for n in list(reversed(range(len(myhand))))]
	for l in range(len(myhand)) :
		for [m,n] in mid :
			if abs(m-n) == l : return myhand[l]

def selectCardAgent(num, hands, attack) :
	myhand   = []
	calchand = []
	for card in hands[num] :
		if len(card) == 2 : myhand.append(hands[num].index(card))
	for i in myhand :
		phands = hands[:]
		print 'hands',hands
		print 'pands',phands
		phands[num][i].append('open')
		numDat, colDat, cards = algo_program.main(phands, attack, num)
		calchand.append(len(cards))
	print myhand,calchand
	return myhand[calchand.index(min(calchand))]