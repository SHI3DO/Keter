import time
import discord
import psutil
import os

from datetime import datetime
from discord.ext import commands
from evs import default

class casino_ko(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")
        self.process = psutil.Process(os.getpid())



def setup(bot):
    bot.add_cog(casino_ko(bot))