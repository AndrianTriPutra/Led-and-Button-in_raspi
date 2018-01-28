#python3
#modulButton
#created by gondril

import RPi.GPIO as GPIO
import time

pushbutton=18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(pushbutton,GPIO.IN,pull_up_down=GPIO.PUD_UP)

try:
	while True:
		input_state = GPIO.input(pushbutton)
		if input_state == False:
			#print("Switch:",input_state,"=>Switch ditekan")		
			import nyalaLED2
			nyalaLED2.LedState(1)
		else:
			#print("Switch:",input_state,"=>Switch Tidak ditekan")
			import nyalaLED2
			nyalaLED2.LedState(0)	
except KeyboardInterrupt:
	pass
GPIO.cleanup()
