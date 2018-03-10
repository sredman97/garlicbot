#by Shane :)

import discord
from discord.ext import commands
import asyncio
import json
import requests


startup_extensions = ["garlic", "meme"]

bot = commands.Bot(command_prefix='!')
test = True

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    bot.loop.create_task(fetch_change_wait())
    return;

async def fetch_garlic(to_get):
    r = requests.get('https://api.coinmarketcap.com/v1/ticker/garlicoin')
    for coin in r.json():
        got = coin.get(to_get)
    return got
    
async def fetch_change_wait():
    while True:
        price = await fetch_garlic('price_usd')
        if test:
            to_change = bot.get_channel('421514445815021588')
        else:
            to_change = bot.get_channel('381265965985562634')
        await bot.edit_channel(to_change, name=price + " USD")
        await asyncio.sleep(30)
            
@bot.event
async def on_message(message):
    if message.author.bot:
        return;
    if 'garlic' in message.content:
        emoji = discord.utils.get(bot.get_all_emojis(), name='garlic')
        await bot.add_reaction(message, emoji)
    await bot.process_commands(message)

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, e))

if test:
    bot.run('NDIxNTE0MTE3MDQwNDM5MzA3.DYPLeA.9im1jZIL5ZR59WIXoJ4NS0moWm8')
else:
    bot.run('NDIxNTUzMjQyOTA0NzIzNDcx.DYO5kQ.-HGJ3Va2g0BEFozBD5BcsZyz-m8')
        
