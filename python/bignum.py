#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import add,sub,mul

bnum = []

def made_bnum(nums) :
	bnum = []
	num = 0
	digit = 5 - len(nums) % 4

	for i in nums :
		num += int(i) * 10 ** (4 - digit)
		if not digit % 4 :
			bnum.append(num)
			num = 0
			digit = 0
		digit += 1
	return bnum

def calc_bnum(func,bnumA,bnumB) :
	bnumA.reverse()
	bnumB.reverse()
	bnumC = []
	mini_len = min(len(bnumA),len(bnumB))

	for i in range(mini_len) :
		bnumC.append(func(bnumA[i],bnumB[i]))
		print bnumA[i],"*",bnumB[i],"=",bnumC[i]

	if len(bnumA) > len(bnumB) :
		for i in range(mini_len,len(bnumA)) :
			bnumC.append(bnumA[i])
		for i in range(mini_len,len(bnumB)) :
			bnumC.append(bnumB[i])

	bnumC.reverse()

	return digit_calc_bnum(bnumC)

def digit_calc_bnum(bnum) :
	bnum.reverse()
	for i in range(len(bnum)) :
		if bnum[i] > 9999 :
			if i + 1 == len(bnum) :
				bnum.append(bnum[i] / 10000)
			else :
				bnum[i+1] += bnum[i] / 10000
			bnum[i] = bnum[i] % 10000
	bnum.reverse()
	return bnum


# print "input a num :",
bnumA = made_bnum(raw_input())
bnumB = made_bnum(raw_input())

print calc_bnum(add,bnumA,bnumB)
print calc_bnum(sub,bnumA,bnumB)
print calc_bnum(mul,bnumA,bnumB)