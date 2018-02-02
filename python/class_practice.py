#!/usr/bin/env python
#coding: utf-8

class Test:
	def __init__(self, num):
		print('call construct : {}'.format(self)) 
		self.num = num;  #このクラスが持つ「num」変数に引数を格納

	def __del__(self):
		print('del destruct {}'.format(self)) 

	def print_num(self):
		print('num is {}'.format(self.num)) 

class Test2(Test):
	def print_test2_info(self):
		print('im Test\'s son')
		super().print_num()

if __name__ == '__main__' :
	test = Test(10)
	test.print_num()
	del test

	test = Test2(10)
	test.print_test2_info()
	del test