import time
import picamera
import RPi.GPIO as GPIO
import signal
import sys 
from datetime import datetime
from PIL import Image

def rad(num):
  n = float(num)
  return (n+90.0)/180.0*(12.0-2.5)+2.5

class moter_control:
	def __init__(self,GPoutW,GPoutH):
		GPIO.cleanup()
		GPIO.setmode(GPIO.BCM)

		GPIO.setup(GPoutW, GPIO.OUT)
		self.servoW = GPIO.PWM(GPoutW, 50) 
		self.servoW.start(0.0)
		self.radW = -10.0

		GPIO.setup(GPoutH, GPIO.OUT)
		self.servoH = GPIO.PWM(GPoutH, 50) 
		self.servoH.start(0.0)
		self.radH = -20.0

	def __del__(self):
		self.servoW.stop()
		self.servoH.stop()
		GPIO.cleanup()

	def mv(self,w,h,option):
		if option :
			tempW = w / 50.0
			tempH = h / 50.0
			print("mv",self.radW,w)
			print("mv",self.radh,h)
		else :
			tempW = (w - self.radW) / 50.0
			tempH = (h - self.radH) / 50.0
			print("mv",self.radW,"to",w)
			print("mv",self.radh,"to",h)

		for i in range(1,50) :
			self.servoW.ChangeDutyCycle(rad(self.radW+tempW*i))
			self.servoH.ChangeDutyCycle(rad(self.radH+tempH*i))
			time.sleep(0.02)

		self.servoW.ChangeDutyCycle(rad(w))
		self.servoH.ChangeDutyCycle(rad(h))
		time.sleep(0.02)
		self.radW = w
		self.radH = h

	def photo(self):
		with picamera.PiCamera() as camera:
			camera.led = False
			pictName = 'pict'+datetime.now().strftime('%m%d%H%M')+'.jpg'
			camera.resolution = (1024,768)
			camera.capture(pictName)
			time.sleep(1)
			im = Image.open(pictName)
			im.rotate(180).save(pictName)

if __name__ == '__main__':
	moter = moter_control(21,20)
	for i in range(8) :
		moter.mv(i*10,i*10,0)
	moter.mv(-10,-20,0)