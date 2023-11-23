import requests
from aiohttp import ClientSession
import asyncio


rates_url = 'https://www.cbr-xml-daily.ru/daily_json.js'

async def fetch_json(url: str) -> dict:
    async with ClientSession() as session:
        async with session.get(url) as response:
            data = requests.get(url).json()
            return data


async def fetch_eur():
    data = await fetch_json(rates_url)
    eur = data["Valute"]["EUR"]["Value"]
    print (eur)
    return eur


async def fetch_usd():
    data = await fetch_json(rates_url)
    usd = data["Valute"]["USD"]["Value"]
    print (usd)
    return usd


async def async_main():
    async with ClientSession() as session:  # type: AsyncSession
        eur, usd = await asyncio.gather(
            fetch_eur(),
            fetch_usd())
        return eur, usd


def main():
    asyncio.run(async_main())


main()