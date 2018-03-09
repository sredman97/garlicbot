#by Shane :)

import discord
import asyncio
import json
import requests

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    client.loop.create_task(fetch_change_wait())
    return;

def fetch_garlic(to_get):
    r = requests.get('https://api.coinmarketcap.com/v1/ticker/garlicoin')
    for coin in r.json():
        got = coin.get(to_get)
    return got
    
async def fetch_change_wait():
    while True:
        price = fetch_garlic('price_usd')
        to_change = client.get_channel('381265965985562634')
        await client.edit_channel(to_change, name=price + " USD")
        await asyncio.sleep(30)
            
@client.event
async def on_message(message):
    if message.content.contains('garlic'):
        await client.add_reaction(message, ':garlic:')
    elif message.content.startswith('!help'):
        await client.send_message(message.channel, \
                '!rank - display rank of garlicoin\n \
                !pbtc - price in bitcoin\n \
                !pchg - percent change in last 1h\n \
                !pc24 - percent change in last 24h\n')
    elif message.content.startswith('!rank'):
        rank = fetch_garlic('rank')
        await client.send_message(message.channel, rank)
    elif message.content.startswith('!pbtc'):
        pbtc = fetch_garlic('price_btc')
        await client.send_message(message.channel, pbtc)
    elif message.content.startswith('!pchg'):
        pchg = fetch_garlic('percent_change_1h')
        await client.send_message(message.channel, pchg)
    elif message.content.startswith('!pc24'):
        pc24 = fetch_garlic('percent_change_24h')
        await client.send_message(message.channel, pc24)
    
client.run('NDIxNTUzMjQyOTA0NzIzNDcx.DYO5kQ.-HGJ3Va2g0BEFozBD5BcsZyz-m8')
        