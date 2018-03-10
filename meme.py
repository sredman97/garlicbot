import discord
from discord.ext import commands

class Meme():

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def hepl(self, ctx):
        """gives hepl"""
        await self.bot.send_message(ctx.message.channel, 'https://twitter.com/Inky_Cap/status/947582060922781696')

def setup(bot):
    bot.add_cog(Meme(bot))
