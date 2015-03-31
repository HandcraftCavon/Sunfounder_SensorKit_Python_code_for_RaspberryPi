#!/usr/bin/env python
import RPi.GPIO as GPIO

HallPin = 11    # pin11 --- hall
LedPin  = 12    # pin12 --- led

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
	GPIO.setup(HallPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led

def loop():
	while True:
		if GPIO.input(HallPin) == GPIO.LOW:
			print '...led on'
			GPIO.output(LedPin, GPIO.LOW)  # led on
		else:
			print 'led off...'
			GPIO.output(LedPin, GPIO.HIGH) # led off

def destroy():
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

