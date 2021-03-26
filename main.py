import discord
import os
import requests
import myScrap


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
  reusultado = requests.g("https://coinmarketcap.com/")
  if msg.startswith('$bitcoin'):
    #await message.channel.send("Hello!")
    await message.author.send("ola")

client.run(os.getenv('TOKEN'))

