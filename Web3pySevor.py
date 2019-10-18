import RPi.GPIO as GPIO
import time
import json
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://testnet.tomochain.com", request_kwargs={'timeout': 60}))

address = "0x670ecA678Caef877ac669A2c3442688E6655B62b"

file = open('abi.json','r')
abi = file.read()

servo = 22

GPIO.setmode(GPIO.BOARD)

GPIO.setup(servo,GPIO.OUT)

p=GPIO.PWM(servo,50) #50hz frequency

p.start(0) # starting duty cycle (it set the servo to 0 degree)

contract = w3.eth.contract(address = address, abi=abi)

try:
	while True:
    time.sleep(1)
    isclose = contract.functions.getA().call()
    if isclose == 1:
     	p.ChangeDutyCycle(12)
    if isclose == 0:
      p.ChangeDutyCycle(3)

except KeyboardInterrupt:
	GPIO.cleanup()
