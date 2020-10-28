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
        
    @commands.command
    async def aaaaa(self, ctx):
        await ctx.send("^^^^")

def setup(bot):
    bot.add_cog(covid19(bot))
