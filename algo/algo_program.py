#!/usr/bin/env python
#coding: utf-8

# 詰めアルゴ第３問
table = [
	[['black'],['white',3],['white',4],['black',5],['white'],['white',11]],
	[['white'],['white',2],['black',3],['black',4],['black',8],['white']],
	[['white'],['black',1],['black'],['white'],['white',8],['black',9]],
	[['black',2],['white'],['black',6],['white'],['black',10],['black']]]

# 詰めアルゴ第４問
# table = [
# 	[['black'],['white'],['white'],['black',8],['white',10],['black']],
# 	[['white',3],['white'],['black'],['white'],['black'],['black',7]],
# 	[['white'],['black',1],['black'],['black'],['white',9],['white']],
# 	[['white',1],['white'],['black',3],['white'],['black',9],['black']]]

# 詰めアルゴ第５問
# table = [
# 	[['black'],['white'],['white'],['black',10]],
# 	[['white',1],['white'],['black',6],['white']],
# 	[['white'],['white'],['black'],['black',7]],
# 	[['white'],['white',3],['black'],['black']]]


# table = [
# 	[['black',5],['white',6],['black',7],['white'],['white']],
# 	[['white'],['white'],['white'],['white'],['white',8]],
# 	[['black'],['black',3],['black'],['black',10],['black',11]],
# 	[['white',0],['white',2],['black',4],['black',6],['black',9]]]
# table = [
# 	[['black'],['white',3],['white',4],['black',5],['white'],['white',11]],
# 	[['white'],['white',2],['black',3],['black',4],['black',8],['white']],
# 	[['white'],['black',1],['black'],['white'],['white',8],['black',9]],
# 	[['black',2],['white'],['black',6],['white'],['black',10],['black']]]

card_col = {'black':"□",'white':"■"}
cards  = []
numDat = []
colDat = []

def printAll() :
	print
	printTable()
	printCards()
	print

def printCards() :
	for col in card_col.keys() :
		print col,":",
		for card in cards :
			if card[0] == col : print card[1],
		print

def printTable() :
	for i in range(4) :
		print 'P{0}:'.format(i),
		for j in range(len(numDat[i])) :
			if type(numDat[i][j]) is int and numDat[i][j] > -1 :
				print '{0} {1}'.format(card_col[colDat[i][j]],numDat[i][j]),
			elif type(numDat[i][j]) is list :
				print '{0} {1}'.format(card_col[colDat[i][j]],numDat[i][j]),
			else :
				print '{0}  '.format(card_col[colDat[i][j]]),
		print
	print
	# writeTable()

def writeTable() :
	with open('log.txt','a') as f :
		for i in range(4) :
			f.write('P{0}: '.format(i))
			for j in range(len(numDat[i])) :
				if type(numDat[i][j]) is int and numDat[i][j] > -1 :
					f.write('{0} {1}'.format(card_col[colDat[i][j]],numDat[i][j]))
				elif type(numDat[i][j]) is list :
					f.write('{0} {1}'.format(card_col[colDat[i][j]],numDat[i][j]))
				else :
					f.write('{0}  '.format(card_col[colDat[i][j]]))
			f.write("\n")
		f.write("\n")

def setCard(table) :
	global numDat
	global colDat
	global cards
	cards  = [[m, n] for m in list(card_col.keys()) for n in range(12)][:]

	for player in table :
		numDat.append([])
		colDat.append([])
		for card in player :
			if type(card) is list and len(card) >= 2 and card[:2] in cards: 
				numDat[table.index(player)].append(card[1])
				cards.remove(card[:2])
			else : numDat[table.index(player)].append(-1)
			colDat[table.index(player)].append(card[0])

def compCard(cardA, cardB) :
	if  cardA[0] == cardB[0] :
		return cardA[1] > cardB[1]
	elif cardA[0] == 'black' :
		return cardA[1] >= cardB[1]
	else :
		return cardA[1] > cardB[1]

def setFactNum(player,num) :
	global numDat
	global colDat

	color = colDat[player][num]

	count = 0
	for i in range(num-1,-1,-1) :
		if colDat[player][i] == colDat[player][i+1] or colDat[player][i] == 'white' : count += 1
		if type(numDat[player][i]) is int and numDat[player][i] > -1 :
			minCard = numDat[player][i]+count
			break
	else :
		count = 0
		for i in range(0,num) :
			if colDat[player][i] == colDat[player][i+1] or colDat[player][i] == 'white' : count += 1
		minCard = count

	count = 0
	for i in range(num+1,len(numDat[player])) :
		if colDat[player][i-1] == colDat[player][i] or colDat[player][i] == 'black' : count += 1
		if type(numDat[player][i]) is int and numDat[player][i] > -1 :
			maxCard = numDat[player][i]-count+1
			break
	else :
		count = 0
		for i in range(len(numDat[player])-1,num,-1) :
			if colDat[player][i-1] == colDat[player][i] or colDat[player][i] == 'black' : count += 1
		maxCard = 12 - count

	numDat[player][num] = []
	for i in range(minCard,maxCard) :
		if [color,i] in cards : numDat[player][num].append(i)

def smartFactNum(player,num) :
	global numDat
	global colDat

	color = colDat[player][num]

	count = 0
	removeList = []
	for i in range(num-1,-1,-1) :
		if colDat[player][i] == colDat[player][i+1] or colDat[player][i] == 'white' : count += 1
		if type(numDat[player][i]) is list and len(numDat[player][i]) > 1 :
			for j in numDat[player][num] :
				if numDat[player][i][0] + count > j: removeList.append(j)
			for j in removeList :
				if j in numDat[player][num] : numDat[player][num].remove(j)

	count = 0
	removeList = []
	for i in range(num+1,len(numDat[player])) :
		if colDat[player][i-1] == colDat[player][i] or colDat[player][i] == 'black' : count += 1
		if type(numDat[player][i]) is list and len(numDat[player][i]) > 1 :
			for j in numDat[player][num] :
				if numDat[player][i][-1] - count < j: removeList.append(j)
			for j in removeList :
				if j in numDat[player][num] : numDat[player][num].remove(j)

def setFact() :
# 	confirmCard()
# def confirmCard() :
# 	global numDat
	for i in range(len(numDat)) :
		for j in range(len(numDat[i])) :
			if type(numDat[i][j]) is list and len(numDat[i][j]) == 1 :
				numDat[i][j] = numDat[i][j][0]
				# print [colDat[i][j],numDat[i][j]],i,j
				cards.remove([colDat[i][j],numDat[i][j]])

def cardLoop(func) :
	global numDat
	for i in range(len(numDat)) :
		for j in range(len(numDat[i])) :
			if numDat[i][j] == -1 or (type(numDat[i][j]) is list and len(numDat[i][j]) > 1):
				func(i,j)	

def removeAttack(attackList, num):
	global numDat
	for attack in attackList :
		[attacker,select,player,where,number,result] = attack
		if not result and type(numDat[player][where]) is list and number in numDat[player][where] :
			# print player,where,number
			numDat[player][where].remove(number)

# 重複除去
def removeDuplication():
	flat_numDat = [i for line in numDat for i in line]
	flat_colDat = [i for line in colDat for i in line]

	numList = [] # 重複カードの値を収納するリスト
	colList = [] # 重複カードの色を収納するリスト

	for i in flat_numDat :
		count = -1
		if not type(i) is list or i in numList : continue
		for j in flat_numDat :
			if i == j and flat_colDat[flat_numDat.index(i)] == flat_colDat[flat_numDat.index(j)]:
				count += 1
		if count and count + 1 == len(i) : # 重複数がカードの数と一致すれば重複とみなす
			numList.append(i)
			colList.append(flat_colDat[flat_numDat.index(i)])

	for nums,cols in zip(numDat,colDat) :
		for num,col in zip(nums,cols) :
			for numL,colL in zip(numList,colList) :
				if num == numL : continue
				if col == colL and type(num) is list :
					i = numDat.index(nums)
					j = numDat[i].index(num)
					for n in numL : 
						while n in numDat[i][j] : numDat[i][j].remove(n)
						if not numDat[i][j] : print "omg"

def main(table, attackList, num) :
	global cards
	global numDat
	global colDat

	numDat = []
	colDat = []

	setCard(table)
	setFact()
	removeAttack(attackList, num)
	while True :
		before = len(cards)
		cardLoop(setFactNum)		# 推測値の設定
		cardLoop(smartFactNum)	# 連番による推測値の重複削除
		setFact()								# カードの値の確定
		removeDuplication()			# 重複情報の削除
		setFact()								# カードの値の確定
		# printTable()						# 出力
		if before == len(cards) : break
	# printTable()
	return numDat, colDat, cards

if __name__ == "__main__":
	main(table,[],0)