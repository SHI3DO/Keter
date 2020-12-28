import random
import time
import discord
import urllib
import secrets
import asyncio
import aiohttp
import re
from datetime import datetime
import time
from io import BytesIO
from discord.ext import commands
from evs import lists, permissions, http, default, argparser


prestige_url = "https://cdn.discordapp.com/attachments/751791353779716099/751807294341120070/KETER_PRESTIGE.png"
parfait_url = "https://cdn.discordapp.com/attachments/751791353779716099/792924251803877406/PARFAIT_ICON-1.png"

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    @commands.command()
    async def 도움(self, ctx):
        embed = discord.Embed(title="케테르 메뉴얼",
                              description=f"**{ctx.author.name}**님,\n[Keter Manual](https://github.com/Shio7/Keter#how-to-use)을 읽어보세요!",
                              color=0xeff0f1)
        embed.set_thumbnail(url=prestige_url)
        embed.set_author(name="Team Parfait", icon_url=parfait_url)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=ctx.author.name+"#"+ctx.author.discriminator + " " + str(datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
        await ctx.send(embed=embed)

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Keter Manual",
                              description=f"**{ctx.author.name}**,\nRead this: [Keter Manual](https://github.com/Shio7/Keter#how-to-use)",
                              color=0xeff0f1)
        embed.set_thumbnail(url=prestige_url)
        embed.set_author(name="Team Parfait", icon_url=parfait_url)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=ctx.author.name+"#"+ctx.author.discriminator + " " + str(datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))