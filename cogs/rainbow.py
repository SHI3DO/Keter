import time
import aiohttp
import discord
import importlib
import os
import sys

from discord.ext import commands
from evs import permissions, default, http, dataIO

cachelib = "./lib/cache/"


class Rainbow(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    @commands.command()
    @commands.check(permissions.is_owner)
    async def rainbow(self, ctx, role:str):
        for r in ctx.guild.roles:
            if r.name == role:
                print("detected role"); await ctx.send("detected role")
                cycle = 0
                f = open(f"./lib/cache/{str(ctx.guild.id)}.ccf", "w")
                f.close()
                while os.path.isfile(f"./lib/cache/{str(ctx.guild.id)}.ccf"):
                    if cycle < 1791:
                        cycle += 1
                    else:
                        cycle = 0
                    if 0 <= cycle < 256:
                        red = 255
                        green = cycle
                        blue = 0
                    elif 256 <= cycle < 512:
                        red = 512 - cycle
                        green = 255
                        blue = 0
                    elif 512 <= cycle < 768:
                        red = 0
                        green = 255
                        blue = cycle - 512
                    elif 768 <= cycle < 1024:
                        red = 0
                        green = 1024 - cycle
                        blue = 255
                    elif 1280 <= cycle < 1536:
                        red = 0
                        green = 1024 - cycle
                        blue = 255
                    else:
                        red = cycle - 1536
                        green = 0
                        blue = 1736 - cycle
                    colour = 65536*red + 256*green + blue
                    try:
                        await role.edit(color=colour)
                    except Exception:
                        return await ctx.send("For some reason, I can no longer change the role ;-;")
                    await asyncio.sleep(0.04)
        await ctx.send(f"role with the name {role} not found"); return print(f"role with the name {role} not found")

    @commands.command()
    @commands.check(permissions.is_owner)
    async def static_halt(self, ctx):
        try:
            os.remove(f"./lib/cache/{str(ctx.guild.id)}.ccf")
        else:
            return await ctx.send("Error has been occured while processing the command")

def setup(bot):
    bot.add_cog(Rainbow(bot))
