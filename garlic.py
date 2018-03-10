import discord
from discord.ext import commands

import requests
import json

class Garlic():

    def __init__(self, bot):
        self.bot = bot

    async def fetch_garlic(self, to_get):
        r = requests.get('https://api.coinmarketcap.com/v1/ticker/garlicoin')
        for coin in r.json():
            got = coin.get(to_get)
        return got
     

    @commands.group(pass_context=True)
    async def grlc(self, ctx):
        """Garlicoin-based commands"""
        if ctx.invoked_subcommand is None:
            bot.send_message(ctx.message.channel, \
                    'Acceptable commands: rank, pbtc, pch, pc24 \
                     use !help for more options')

    @grlc.command(pass_context=True)
    async def rank(self, ctx):
        """Displays rank of garlicoin"""
        rank = await self.fetch_garlic('rank')
        await self.bot.send_message(ctx.message.channel, rank)

    @grlc.command(pass_context=True)
    async def pbtc(self, ctx):
        """Displays garlicoin's current price in BTC"""
        pbtc = await self.fetch_garlic('price_btc')
        await self.bot.send_message(ctx.message.channel, pbtc)

    @grlc.command(pass_context=True)
    async def pchg(self, ctx):
        """Displays garlicoin's percent change in the last hour"""
        pchg = await self.fetch_garlic('percent_change_1h')
        await self.bot.send_message(ctx.message.channel, pchg)

    @grlc.command(pass_context=True)
    async def pc24(self, ctx):
        """Displays garlicoin's percent change in the last 24 hours"""
        pc24 = await self.fetch_garlic('percent_change_24h')
        await self.bot.send_message(ctx.message.channel, pchg)

def setup(bot):
    bot.add_cog(Garlic(bot))

