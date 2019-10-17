import RPi.GPIO as GPIO
import time

control = [5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]

servo = 22

GPIO.setmode(GPIO.BOARD)

GPIO.setup(servo,GPIO.OUT)

p=GPIO.PWM(servo,50) #50hz frequency

p.start(0) # starting duty cycle (it set the servo to 0 degree)

try:
	while True :
		for x in range(11):
			p.ChangeDutyCycle(control[x])
			time.sleep(0.5)
			print x
		for x in range(9,0,-1):
			p.ChangeDutyCycle(control[x])
			time.sleep(0.5)
			print x

except KeyboardInterrupt:
	GPIO.cleanup()

