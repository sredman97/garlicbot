import discord
from discord.ext import commands

import random
import sys
import csv

class Meme():

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def hepl(self, ctx):
        """gives hepl"""
        await self.bot.send_message(ctx.message.channel, 'https://twitter.com/Inky_Cap/status/947582060922781696')

    @commands.command(pass_context=True)
    async def getmeme(self, ctx):
        """retrieves meme for your enjoyment"""
        with open('bigbook.csv') as f:
            memes = csv.reader(f)
            meme = random.choice(list(memes))
        await self.bot.send_message(ctx.message.channel, meme[0])

    @commands.command(pass_context=True)
    async def addmeme(self, ctx, arg=None):
        """add meme for future enjoyment"""
        if arg is None:
            await self.bot.send_message(ctx.message.channel, 'Submit youtube link \n usage: !addmeme youtubelink')
            return;
        elif 'https://www.youtube.com/watch?' not in arg:
            await self.bot.send_message(ctx.message.channel, 'Must be a valid youtube link')
            return;
        with open('bigbook.csv', 'a') as f:
            memes = csv.writer(f)
            towrite = [arg]
            print('writing {} to bigbook'.format(arg))
            memes.writerow(towrite)

def setup(bot):
    bot.add_cog(Meme(bot))
