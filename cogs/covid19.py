import discord
from discord.ext import commands
from evs import default
import psutil
import os

class covid19(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")
        self.process = psutil.Process(os.getpid())
        
    @commands.command
    async def aaaaa(self, ctx):
        await ctx.send("^^^^")

def setup(bot):
    bot.add_cog(covid19(bot))
