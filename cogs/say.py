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
        await ctx.send(content)

def setup(client):
    client.add_cog(Say(client))
