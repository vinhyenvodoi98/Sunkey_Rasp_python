import RPi.GPIO as GPIO
import time
import json
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://testnet.tomochain.com", request_kwargs={'timeout': 60}))

address = "0x2af7268C88FDE26AE20AbEaee2f8d8233Dde4127"

file = open('abi.json','r')
abi = file.read()
servo = 22

GPIO.setmode(GPIO.BOARD)

GPIO.setup(servo,GPIO.OUT)

p=GPIO.PWM(servo,50) #50hz frequency

p.start(0) # starting duty cycle (it set the servo to 0 degree)
temp = 2
contract = w3.eth.contract(address = address, abi=abi)
try:
    while True:
        time.sleep(1)
        isclose = contract.functions.getLock().call()
        print (isclose)
#        print(isclose)
#        temp = isclose
#        if (temp != contract.functions.getA().call()):
#            p.ChangeDutyCycle(12)
#        else:
#            p.ChangeDutyCycle(6.5)

        if (temp != isclose):
            if isclose == True:
                p.ChangeDutyCycle(12)
                print ('trang thai:', isclose)
            if isclose == False:
                p.ChangeDutyCycle(6.5)
                print ('trang thai:', isclose)
            temp = isclose
            print ('temp:', temp)

except KeyboardInterrupt:
    GPIO.cleanup()
