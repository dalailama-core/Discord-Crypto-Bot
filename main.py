import discord
import os
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

# Help message to show on discord bot 

helpMessage = "Help -> Help \n CoinConvert \n startswith € for euro \n startswith $ for Dollar  \n startswith & for Pound \n CRYPTO COIN \nBTC to bitcoin \nXRP to Riple"
ap_key=os.getenv('ap_key')

# Get currency that the user wants information 

def choise(mes):
  fia ='EUR' # stantdart
  if mes.startswith('$'):
    fia = 'USD'
  if mes.startswith('€'):
    fia = 'EUR'
  if mes.startswith('&'):
    fia='GBP'
  
  symbol = mes[1:]
  return [symbol,fia]
  
  
#Scrapt the information on the coinmarket website 

def getCoinInfo(symbol, convertCoin,key):
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
  info=""

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
    parseData = json.dumps(response.json())
    cryptoObj = json.loads(parseData)

    name =   cryptoObj["data"][symbol]["name"]
    supply = cryptoObj["data"][symbol]["circulating_supply"]
    price =  cryptoObj["data"][symbol]["quote"][convertCoin]["price"]

    info = name+"\n"+str(supply)+"\n"+str(price)
    print(info)
    

  except (ConnectionError, Timeout, 
  TooManyRedirects) as e:
    print(e)
  return info

# Discord

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
  print (msg)

  if msg.startswith('help'):
    info = helpMessage
  else :
    b = choise(msg)
    info = getCoinInfo(b[0],b[1],ap_key)  
  await message.channel.send(info)

client.run(os.getenv('TOKEN'))