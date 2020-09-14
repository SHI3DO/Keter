import discord
import psutil
import os

from datetime import datetime
from discord.ext import commands
from discord.ext.commands import errors
from evs import default


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")
        self.process = psutil.Process(os.getpid())

    @commands.command()
    async def 도움(self, ctx):
        embed = discord.Embed(title="도움말", description="케테르 봇의 명령어에 대한 도움말입니다.",color=0xeff0f1)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/750540820842807396/752684853320745000/KETER_PRESTIGE.png")
        embed.add_field(name='도움', value="이 명령어를 보여줍니다.", inline=True)

def setup(bot):
    bot.add_cog(Help(bot))
