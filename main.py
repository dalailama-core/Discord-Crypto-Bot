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

helpMessage = " HELP \n Bot Tipping Commands \n COIN CONVERT \n |€SYMBOL to quote SYMBOL coin in euro \n |$SYMBOL to quote SYMBOL coin in Dollar  \n |&SYMBOL to quote SYMBOL coin in pound \n\n Example: \n|€BTC to quote bitcoin in euros \n|$BTC to quote bitcoin in dollar \n|&BTC to quote bitcoin in pound " 
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