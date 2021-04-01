
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

# Get currency that the user wants information 

def choise(mes):
  fia ='BTC' # stantdart
  if mes.startswith('$'):
    fia = 'USD'
  elif mes.startswith('€'):
      fia = 'EUR'
  elif mes.startswith('&'):
    fia='GBP'
  elif mes.startswith('#'):
    fia ='BTC'
  
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
    print ( cryptoObj )

    name =   cryptoObj["data"][symbol]["name"]
    supply = cryptoObj["data"][symbol]["circulating_supply"]
    price =  cryptoObj["data"][symbol]["quote"][convertCoin]["price"]
    percent =  cryptoObj["data"][symbol]["quote"][convertCoin]["percent_change_24h"]

    price ="{:.10f}".format(price)
    percent ="{:.2f}".format(percent)
    info = "COIN:"+ name+"\n SUPPY: "+str(supply)+"\n PRICE: "+str(price)+"\n Percent Change 24H: "+str(percent)+"%"
    print(info)
    

  except (ConnectionError, Timeout, 
  TooManyRedirects) as e:
    print(e)
  return info