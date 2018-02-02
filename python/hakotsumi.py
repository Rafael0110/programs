#!/usr/bin/env python
#coding: utf-8

# import pygame
import itertools as ite

field = [[[] for i in range(12)] for i in range(12)]

class col:
  HEADER		= '\033[95m'
  B 				= '\033[94m'
  G 				= '\033[92m'
  Y 				= '\033[93m'
  R 				= '\033[91m'
  ENDC			= '\033[0m'
  BOLD			= '\033[1m'
  UNDERLINE = '\033[4m'
  RB 		 		= '\033[91m\033[1m'

def prints() :
	global field
	print ""
	for cells in field :
		for cell in cells :
			if cell : print cell,
			else 		: print ".",
		print ""
	for i in range(12) : print ('%x' % i),
	print ""

def set_box(box) :
	global field
	print "\n" + box + " : input num ( 0 ~ 11 ) > ",
	inputText = raw_input()

	if not inputText :
		print col.Y + "ERROR : input a num" + col.ENDC,		
	elif not inputText.isdigit() :
		print col.Y + "ERROR : you input str" + col.ENDC,
	else :
		num = int(inputText)

		if ( -1 < num < 12 ) :
			for i in range(12)[::-1] :
				if not (field[i][num]) :
					field[i][num] = box
					return False
			print col.Y + "ERROR : tower is max" + col.ENDC,
		elif not ( -1 < num < 12 ) :
			print col.Y + "ERROR : num is out of 0 ~ 11" + col.ENDC,
	return True

def vict() :
	global field
	for (i,j) in ite.product(range(12),range(12)) :
		if not field[i][j] : continue
		for [p,q] in [[0,1],[1,0],[1,1],[1,-1]] :
			if loop4(i,j,p,q) :
				vict_prints(i,j,p,q)
				return 1
	return 0

def loop4(i,j,p,q) :
	if not ( -1 < i+p*3 < 12 and -1 < j+q*3 < 12 ) : return 0
	for x in range(4)[1:]:
		if field[i][j] == field[i + x*p][j + x*q] : continue
		else : return 0
	return 1

def vict_prints(i,j,p,q) :
	global field
	for x in range(4): field[i + x*p][j + x*q] = str(col.RB + field[i + x*p][j + x*q] + col.ENDC)

def main() :
	box = "O"

	while True :
		prints()
		while set_box(box) : continue
		if vict() : 
			prints()
			print "\n" + box + " is winner !!"
			break
		if box == "O" : box = "X"
		else 					: box = "O"

if __name__ == "__main__" :
	main()