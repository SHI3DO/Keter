import discord
from discord.ext import commands
from evs import default

class Shindan_ko(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    # Commands
    @commands.command(name="진단")
    async def _say(self, ctx, *, content:str):
            await ctx.send(str + "에 대한 진단을 만드시겠습니까?")

def setup(bot):
    bot.add_cog(Shindan_ko(bot))
