import aiohttp
import asyncio

from typing import Dict
import json


async def get_iin(iin: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://127.0.0.1:8000/people/{iin}') as resp:
            assert resp.status == 200 \
            and 'iin' in await resp.json() \
            and 'age' in await resp.json(), 'Not passed!'


async def post_iin(test_iin: Dict[str, str]):
    async with aiohttp.ClientSession() as session:
        async with session.post('http://127.0.0.1:8000/people', json = test_iin) as resp:
            assert resp.status == 201 \
            and 'iin' in await resp.json() \
            and 'age' in await resp.json(), 'Not passed!'



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(post_iin(dict({'iin': '760724300757'})))
    loop.run_until_complete(get_iin('760724300757'))
