import asyncio
import aiohttp
import requests
import time

api_key = "JMIY2BCRTIUR8WOJ"
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT']
results =[]


def get_tasks(session):
    tasks = []
    for symbol in symbols:
        tasks.append(session.get(url.format(symbol, api_key), ssl=False))
    return tasks

start = time.time()
async def get_symbols():
    async with aiohttp.ClientSession() as session :
        tasks = get_tasks(session)
        responses = await asyncio.gather(*tasks)
        for response in responses :
            results.append(await response.json())

asyncio.run(get_symbols())
end = time.time() 
elapsed_time = end - start
print('u did it in {} u fetched {} symbols'.format(elapsed_time, len(symbols)))