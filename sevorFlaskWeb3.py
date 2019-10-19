
from flask import Flask, request, jsonify   # Importing the Flask modules required for this project
import RPi.GPIO as GPIO     # Importing the GPIO library to control GPIO pins of Raspberry Pi
from time import sleep      # Import sleep module from time library to add delays
import json
from web3 import Web3
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app,support_credentials=True)
app.config['CORS_HEADERS']='Content-Type'

def runSevor(duty):
    # Pins where we have connected servos
    servo_pin = 22

    GPIO.setmode(GPIO.BOARD)      # We are using the BCM pin numbering
    # Declaring Servo Pins as output pins
    GPIO.setup(servo_pin, GPIO.OUT)

    # Created PWM channels at 50Hz frequency
    p = GPIO.PWM(servo_pin, 50)

    # Initial duty cycle
    p.start(0)

    # Change duty cycle
    p.ChangeDutyCycle(duty)
    sleep(1)

def connectWeb3(address):
    w3 = Web3(Web3.HTTPProvider("https://testnet.tomochain.com", request_kwargs={'timeout': 60}))
    file = open('abi.json','r')
    abi = file.read()

    contract = w3.eth.contract(address = address, abi=abi)
    print(address, contract)
    isOpen = contract.functions.getLock().call()
    print(isOpen)

    return isOpen 

@app.route("/door/<door_address>",methods=['GET'])
@cross_origin(supports_credentials=True)
def door(door_address):
    print (door_address)
    isOpen = connectWeb3(door_address)
    print (isOpen)
    if isOpen == True:
        runSevor(12)
    if isOpen == False:
        runSevor(6.5)
    return jsonify({'success':isOpen})

# Run the app on the local development server
if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 3000, debug=False)
