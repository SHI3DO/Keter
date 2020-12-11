import discord
from discord.ext import commands
from evs import default

class Say_ko(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    # Commands
    @commands.command(name="말해")
    async def _say(self, ctx, *, content:str):
        async with ctx.typing():
            await ctx.message.delete()
        if "@everyone" in content:
            embed = discord.Embed(title="안돼요", description='You cannot do that', color=0xeff0f1)
            await ctx.send(embed=embed)
        else:
            await ctx.send(content)

def setup(bot):
    bot.add_cog(Say_ko(bot))
