import RPi.GPIO as GPIO
import time

pin7 = 7 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin7, GPIO.OUT)

for i in range(20):
	GPIO.output(pin7, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(pin7, GPIO.LOW)
	time.sleep(1)
GPIO.cleanup()
