import aiohttp
import asyncio
import time

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(fetch(session, url))
        responses = await asyncio.gather(*tasks)
        return responses

async def main():
    urls = [f"https://example.com/{i}" for i in range(100)]
    start_time = time.time()
    responses = await fetch_all(urls)
    end_time = time.time()
    print(f"{end_time - start_time} seconds")

asyncio.run(main())
#янемногонепонялэтозаданиенопопытался