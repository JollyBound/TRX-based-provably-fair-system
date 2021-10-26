import os
import requests
import json
import time

response_API = requests.get('https://apilist.tronscan.org/api/block/latest')
data = response_API.text
parse_json = json.loads(data)
lastBlock = parse_json['number']
print("Current block:",lastBlock)
targetBlock = lastBlock + 20
print("Target block is: ",targetBlock)

while True:
  params = {'number': targetBlock}
  response = requests.get('https://apilist.tronscan.org/api/block?',
  params=params)
  url = (response.url)
  response_API = requests.get(url)
  data = response_API.text
  parse_json = json.loads(data)
  try:
    newBlock = parse_json["data"][0]["number"]
    print(newBlock)
    print("block mined")
    hash = parse_json["data"][0]["hash"]
    print(hash)
    break

  except:
    time.sleep(1)
    print("not mined yet")
