import time
import discord
import psutil
import os
import matplotlib.pyplot as plt
import openpyxl
import asyncio

from datetime import datetime
from discord.ext import commands
from evs import default, permissions

class covid19(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")
        self.process = psutil.Process(os.getpid())
        
    # Commands
    @commands.command(name="말해에")
    async def _say(self, ctx, *, content:str):
        async with ctx.typing():
            await ctx.message.delete()
        if (content == "@everyone"):
            embed = discord.Embed(title="안돼요", description='You cannot do that', color=0xeff0f1)
            await ctx.send(embed=embed)
        else:
            await ctx.send(content)
        
def setup(bot):
    bot.add_cog(covid19(bot))
