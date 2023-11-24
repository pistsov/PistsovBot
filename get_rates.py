import requests
from aiohttp import ClientSession
import asyncio

rates_url = 'https://www.cbr-xml-daily.ru/daily_json.js'


def fetch_json(url: str) -> dict:
    data = requests.get(url).json()
    return data


def fetch_eur():
    data = fetch_json(rates_url)
    eur = data["Valute"]["EUR"]["Value"]
    print(eur)
    return eur


def fetch_usd():
    data = fetch_json(rates_url)
    usd = data["Valute"]["USD"]["Value"]
    print(usd)
    return usd


def main():
    eur, usd = fetch_eur(), fetch_usd()
    return eur, usd


main()
