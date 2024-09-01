import aiohttp
import asyncio

endpoints = [
    {
        'url': 'https://api.coingecko.com/api/v3/simple/price',
        'params': {'ids': 'bitcoin,ethereum', 'vs_currencies': 'usd'}
    },
    {
        'url': 'https://dog.ceo/api/breeds/image/random',
        'params': {}
    },
    {
        'url': 'https://catfact.ninja/fact',
        'params': {}
    },
    {
        'url': 'https://api.chucknorris.io/jokes/random',
        'params': {}
    },
    {
        'url': 'https://v2.jokeapi.dev/joke/Programming',
        'params': {}
    },
]


async def call(session, endpoint):
    call_times = 5
    for _ in range(call_times):
        async with session.get(endpoint['url'],
                               params=endpoint['params']) as response:
            data = await response.json()
            print(data)


async def main():
    async with aiohttp.ClientSession() as session:
        calls = [call(session, endpoint) for endpoint in endpoints]
        await asyncio.gather(*calls)

if __name__ == "__main__":
    asyncio.run(main())
