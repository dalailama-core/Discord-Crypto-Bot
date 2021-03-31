import discord
import os
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from coinmarket import choise as ch
from coinmarket import getCoinInfo as getInfo
from keep_alive import keep_alive

# Help message to show on discord bot 

helpMessage = "Help -> Help \n CoinConvert \n startswith € for euro \n startswith $ for Dollar  \n startswith & for Pound \n CRYPTO COIN \nBTC to bitcoin \nXRP to Riple"
ap_key=os.getenv('ap_key')


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
    b = ch(msg)
    info = getInfo(b[0],b[1],ap_key)  
  await message.channel.send(info)
keep_alive()
client.run(os.getenv('TOKEN'))