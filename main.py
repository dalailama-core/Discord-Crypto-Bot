import discord
import os
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os

ap_key=os.getenv('ap_key')
def getCoinInfo(symbol, convertCoin,key):
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
  info=""
  #symbol= input("symbol coin? ").upper()
  #convertCoin=input("convert coin? ").upper()
  parameters = {
      'symbol':symbol,
      'convert':convertCoin
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': key
  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    #data = json.loads(response.text)
    #print(data)
    parseData = json.dumps(response.json())
    #print(parseData)
    ethObj = json.loads(parseData)
    name = ethObj["data"][symbol]["name"]
    supply = ethObj["data"][symbol]["circulating_supply"]
    price = ethObj["data"][symbol]["quote"][convertCoin]["price"]
    #print("Name -> ",name)
    #print("Circulating Supply _> ",supply)
    #print("Price -> ",price)
    info = name+"\n"+str(supply)+"\n"+str(price)
    print(info)
    ethString = str(ethObj["data"][symbol]["quote"][convertCoin]["price"])
    ethPrice = float(ethString)

  except (ConnectionError, Timeout, 
  TooManyRedirects) as e:
    print(e)
  return info


client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content
  print(message.author.name)
  
  if msg.startswith('$bitcoin'):
    info = getCoinInfo("BTC","EUR",ap_key)
    await message.channel.send(info)
   # await message.author.send("ola")

client.run(os.getenv('TOKEN'))

