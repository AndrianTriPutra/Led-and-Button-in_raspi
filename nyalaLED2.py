#python 3
#nyalaLED2.py
#created by gondril

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LedList=[17,27,22]

for i in range (0,3):
	GPIO.setup(LedList[i],GPIO.OUT)
	
def LedState(n):
	#print ("........ keputusan menyalakan LED........")
	if n==1:
		print("		kanan ke kiri")
		i=2
		while i>=0:
			GPIO.output(LedList[i],GPIO.HIGH)
			time.sleep(0.25)
			GPIO.output(LedList[i],GPIO.LOW)
			time.sleep(0.25)
			i-=1
	else:		
		print("kiri ke kanan")
		"""
		for i in range (0,3):
			GPIO.output(LedList[i],GPIO.HIGH)
			time.sleep(0.25)
			GPIO.output(LedList[i],GPIO.LOW)
			time.sleep(0.25)
		"""
		for i in LedList:
			GPIO.output(i,GPIO.HIGH)
			time.sleep(0.25)
			GPIO.output(i,GPIO.LOW)
			time.sleep(0.25)	
