#!/usr/bin/python
# coding: utf-8 

import RPi.GPIO as GPIO
import time
import signal
import sys 

def rad(num):
  n = float(num)
  return (n+90.0)/180.0*(12.0-2.5)+2.5

def exit_handler(signal, frame):
  # Ctrl+Cが押されたときにデバイスを初期状態に戻して終了する。
  print("\nExit")
  time.sleep(0.5)
  servow.ChangeDutyCycle(rad(-10))
  servoh.ChangeDutyCycle(rad(-90))
  time.sleep(0.5)
  servow.stop()
  servoh.stop() 
  GPIO.cleanup()
  sys.exit(0)

# 終了処理用のシグナルハンドラを準備
signal.signal(signal.SIGINT, exit_handler)
GPIO.setmode(GPIO.BCM)

# pwm = GPIO.PWM([チャンネル], [周波数(Hz)])
# GPIO 20番を使用
gp_out = 20
GPIO.setup(gp_out, GPIO.OUT)
servoh = GPIO.PWM(gp_out, 50) 
servoh.start(0.0)

# GPIO 21番を使用
gp_out = 21
GPIO.setup(gp_out, GPIO.OUT)
servow = GPIO.PWM(gp_out, 50) 
servow.start(0.0)

for k in range(3) :

	for i in range(-50,50,1) :
		print i
		time.sleep(0.01)
		servoh.ChangeDutyCycle(rad(i))

	for i in range(50,-50,-1) :
		print i
		time.sleep(0.01)
		servoh.ChangeDutyCycle(rad(i))

for i in range(-50,-10,1) :
	print i
	time.sleep(0.01)
	servoh.ChangeDutyCycle(rad(i))