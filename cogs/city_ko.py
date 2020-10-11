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

from datetime import datetime
from discord.ext import commands
from evs import default, permissions

def keundon(value: int):
    value = int(value)
    if value < 0:
        return "변수는 음수값을 가질 수 없습니다."
    elif 0 <= value < 10000:
        return str(value)
    elif 10000 <= value < 100000000:
        return str(math.floor(value / 10000)) + "만 " + str(value - math.floor(value / 10000) * 10000)
    elif 100000000 <= value < 1000000000000:
        return str(math.floor(value / 100000000)) + "억 " + str(math.floor(value / 10000) - math.floor(value / 100000000) * 10000) + "만 " + str(value - math.floor(value / 10000) * 10000)
    elif 1000000000000 <= value < 10000000000000000:
        return str(math.floor(value / 1000000000000)) + "조 " + str(math.floor(value / 100000000) - math.floor(value / 1000000000000) * 10000) + "억 " + str(math.floor(value / 10000) - math.floor(value / 100000000) * 10000) + "만 " + str(value - math.floor(value / 10000) * 10000)
    elif 10000000000000000 <= value < 100000000000000000000:
        return str(math.floor(value / 10000000000000000)) + "경 " + str(math.floor(value / 1000000000000) - math.floor(value / 10000000000000000) * 10000) + "조 " + str(math.floor(value / 100000000) - math.floor(value / 1000000000000) * 10000) + "억 " + str(math.floor(value / 10000) - math.floor(value / 100000000) * 10000) + "만 " + str(value - math.floor(value / 10000) * 10000)
    else:
        return "변수의 크기가 너무 큽니다."


class city_ko(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")
        self.process = psutil.Process(os.getpid())

    # Commands
    @commands.command()
    async def nnn(self, ctx):
        ctx.send("wow")
    

def setup(bot):
    bot.add_cog(city_ko(bot))
