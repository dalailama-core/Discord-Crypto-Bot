import urllib
from bs4 import BeautifulSoup as bt

url = "https://coinmarketcap.com/"

def listCoin (coin):
  page = urllib.request.urlopen(url)
  data = bt(page,"html.parser")
  data = data.find_all('tr')
  for item in data:
    cols = item.find_all('td')
    for c in cols:
      if c.text[1]==coin:
        print(c.text[2])    
        