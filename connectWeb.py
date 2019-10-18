import json
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://testnet.tomochain.com",request_kwargs={'timeout':60}))

account ="0x4C637fC36ecA2d02d5214b53c0aEc272f31F7E53"

address= "0x670ecA678Caef877ac669A2c3442688E6655B62b"

file = open('abi.json','r')
abi = file.read()

contract = w3.eth.contract(address = address, abi=abi)

print(contract.functions.getA().call())