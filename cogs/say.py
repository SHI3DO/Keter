import discord
from discord.ext import commands

class Say(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command(name="말하기")
    async def _say(self, ctx, *, content:str):
        async with ctx.typing():
            await ctx.message.delete()
        if (content == "@everyone"):
            embed = discord.Embed(title="NO", description='You cannot do that', color=0xeff0f1)
            await ctx.send(embed=embed)
        else:
            await ctx.send(content)

def setup(client):
    client.add_cog(Say(client))
