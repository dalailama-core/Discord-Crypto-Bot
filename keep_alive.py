# File copyng from #https://www.codementor.io/@garethdwyer/building-a-discord-bot-with-python-and-r
#epl-it-miblcwejz

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "I'm alive"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
