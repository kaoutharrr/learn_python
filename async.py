import asyncio
import aiohttp
import requests
import time

api_key = "JMIY2BCRTIUR8WOJ"
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT']
results =[]

start = time.time()
async def get_symbols():
    async with aiohttp.ClientSession() as session :
        for symbol in symbols :
            print('working on symbol {}'.format(symbol))
            response = await session.get(url.format(symbol, api_key), ssl=False)
            results.append( await response.json())
asyncio.run(get_symbols())
end = time.time() 
elapsed_time = end - start
print('u did it in {} u fetched {} symbols'.format(elapsed_time, len(symbols)))