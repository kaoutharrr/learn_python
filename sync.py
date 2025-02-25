import requests
import time

api_key = "JMIY2BCRTIUR8WOJ"
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT']
results =[]

start = time.time()
for symbol in symbols :
    print('working on symbol {}'.format(symbol))
    response = requests.get(url.format(symbol, api_key))
    results.append(response.json())
end = time.time() 
elapsed_time = end - start
print('u did it in {} u fetched {} symbols'.format(elapsed_time, len(symbols)))
