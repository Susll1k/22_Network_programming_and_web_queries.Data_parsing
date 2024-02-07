import requests
import aiohttp
import asyncio
import os
os.mkdir('main')
os.mkdir('aiohttp')

#####################1



def save_data(url):
    response = requests.get(url)
    data = response.json()
    with open (f"main/todos_{data['id']}.json", "w") as file:
        file.write(response.text)


for i in range(1, 101):
    save_data(f"https://jsonplaceholder.typicode.com/todos/{i}")





#####################2



async def get_data_async(url, session, i):
    async with session.get(url) as response:
        return await response.text()



async def paralell():
    async with aiohttp.ClientSession() as session:
         events = [get_data_async(f"https://jsonplaceholder.typicode.com/todos/{i}", session, i) for i in range(1,101)]
         result = await asyncio.gather(*events)
         for ind, data in enumerate(result):
            with open (f"aiohttp/todos_{ind+1}.json", "w") as f:
                f.write(data)



if __name__ == "__main__":
    asyncio.run(paralell())


