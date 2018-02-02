#!/usr/bin/env python
#coding: utf-8

from random import sample

PlayersNum   = 4
InitCardNum  = 3
GameTurn     = 0
PlayersCount = 0
GameOverFlag = True

cols    = {'black':"□",'white':"■"}
cards   = [[m, n, 'hidden'] for m in list(cols.keys()) for n in range(12)]
hands   = [[] for i in range(4)]
numDat  = []
colDat  = []
staDat  = []
attacks = []

def drawCard(pNum) :
  global cards
  phands = hands[pNum][:]

  if len(cards) :
    card = sample(cards, 1)[0]
    cards.remove(card)
  else : return

  if len(phands) == 0 :
    phands.append(card) 
  else :
    for hand in phands :
      index = phands.index(hand)
      if hand[1] > card[1] or (hand[1] == card[1] and hand[0] == 'white') :
        phands = phands[:index] + [card] + phands[index:]
        break
      elif hand[1] == card[1] and hand[0] == 'black' :
        index += 1
        phands = phands[:index] + [card] + phands[index:]
        break
    else : phands = phands + [card]
  hands[pNum] = phands[:]

def checkGameOver() :
	global	GameOverFlag
	GameOverFlag = False

def printHands() :
	for i in range(4) :
		print 'P{0}:'.format(i),
		for j in range(len(hands[i])) :
			if type(hands[i][j][]) is int and hands[i][j] > -1 :
				print '{0} {1}'.format(card_col[colDat[i][j]],hands[i][j]),
			elif type(hands[i][j]) is list :
				print '{0} {1}'.format(card_col[colDat[i][j]],hands[i][j]),
			else :
				print '{0}  '.format(card_col[colDat[i][j]]),
		print
	print

def main() :
	global GameTurn
	global PlayersCount

	for i in range(PlayersNum) :
		for j in range(InitCardNum) : drawCard(i)
		printHands()

	while GameOverFlag :


		GameTurn += 1
		PlayersCount = GameTurn % 4
		checkGameOver()
	# while GameOverFlag :
	# 

if __name__ == "__main__":
	main()