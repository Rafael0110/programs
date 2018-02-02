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

def exit_handler(servow,servoh):
	servow.stop()
	servoh.stop()
	GPIO.cleanup()

def take_pict():
	with picamera.PiCamera() as camera:
		camera.led = False
		pictName = 'pict'+datetime.now().strftime('%m%d%H%M')+'.jpg'
		camera.resolution = (1024,768)
		camera.capture(pictName)
		time.sleep(2)
		im = Image.open(pictName)
		im.rotate(180).save(pictName)

def set_camera() :
	GPIO.cleanup()
	GPIO.setmode(GPIO.BCM)

	gp_out = 20
	GPIO.setup(gp_out, GPIO.OUT)
	servoh = GPIO.PWM(gp_out, 50) 
	servoh.start(0.0)

	gp_out = 21
	GPIO.setup(gp_out, GPIO.OUT)
	servow = GPIO.PWM(gp_out, 50) 
	servow.start(0.0)

	servow.ChangeDutyCycle(rad(-10))
	time.sleep(0.5)
	servoh.ChangeDutyCycle(rad(-20))
	time.sleep(0.5)

	return servow,servoh

if __name__ == '__main__':
	w,h = set_camera()
	exit_handler(w,h)
	take_pict()
	sys.exit(0)