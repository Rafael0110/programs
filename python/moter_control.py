import time
import picamera
import RPi.GPIO as GPIO
import signal
import sys 
from getch import getch, pause
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

		self.mv(0,0,1)

	def __del__(self):
		self.mv(-10.0,-20.0,0)
		self.servoW.stop()
		self.servoH.stop()
		GPIO.cleanup()

	def mv(self,w,h,option):

		print "mv",str(self.radW),w
		print "mv",str(self.radH),h

		if option :
			tempW = w / 5.0
			tempH = h / 5.0
			self.radW += w
			self.radH += h
		else :
			tempW = (w - self.radW) / 5.0
			tempH = (h - self.radH) / 5.0
			self.radW = w
			self.radH = h

		self.servoW.ChangeDutyCycle(rad(self.radW))
		self.servoH.ChangeDutyCycle(rad(self.radH))

		time.sleep(0.5)

	def photo(self):
		with picamera.PiCamera() as camera:
			camera.led = False
			pictName = 'pict'+datetime.now().strftime('%m%d%H%M%S')+'.jpg'
			camera.resolution = (1024,768)
			camera.capture(pictName)
			time.sleep(1)
			im = Image.open(pictName)
			im.rotate(180).save(pictName)

	def moter_moove(self):
		while True:
		  key = ord(getch())

		  if key == 13: # Enter
		  	self.photo()
		  	print "Photo!"
		  	pass

		  if key == 27: # ESC
		    key = ord(getch())

		    if key == 91: # Arrow keys
		      key = ord(getch())
		      if key == 66:
		        print "Down Arrow"
		        self.mv(0,5.0,1)
		      elif key == 65:
		        print "Up Arrow"
		        self.mv(0,-5.0,1)
		      elif key == 68:
		        print "Left Arrow"
		        self.mv(5.0,0,1)
		      elif key == 67:
		        print "Right Arrow"
		        self.mv(-5.0,0,1)

		    elif key == 27: # ESC
		      print "ESC : exit."
		      break
		self.__del__()
		pause()

if __name__ == '__main__':
	moter = moter_control(21,20)
	moter.moter_moove()