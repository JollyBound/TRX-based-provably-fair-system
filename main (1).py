import os
import requests
import json
import time

response_API = requests.get('https://apilist.tronscan.org/api/block/latest')
data = response_API.text
parse_json = json.loads(data)
lastBlock = parse_json['number']
print("Current block:",lastBlock)
targetBlock = lastBlock + 5
print("Target block is: ",targetBlock)
#time.sleep(3)

while True:
  params = {'number': targetBlock}
  response = requests.get('https://apilist.tronscan.org/api/block?',
  params=params)
  url = (response.url)
  response_API = requests.get(url)
  data = response_API.text
  parse_json = json.loads(data)
  newBlock = parse_json["data"][0]["number"]
  print(newBlock)
  if newBlock == targetBlock:
    print("Target block mined!") # means that the block was mined obviously
    hash = parse_json["data"][0]["hash"]  #gets the hash
    print("hash is: ",hash)
    hex = hash[0:20] # collects the first 20 characters of the hash - hexadecimal format
    print("hexadecimal str: ",hex) 
    dec = int(hex, 16) # converts those 20 to decimal format
    print("decimal str: ", dec)
    rem = dec % 2 # pretty much checks if the decimal num is divisible by 2
    if rem == 1: # if not the result of the remainder will be 1, which I decided that = black
      print("Black")
    elif rem == 0: # if yes, red.
      print("Red")
    break
  else:
    print("not mined yet")
