import discord
import time
import psutil
import os
import asyncio
import openpyxl
import random
import math
import numpy as np
import datetime
import matplotlib.pyplot as plt

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
