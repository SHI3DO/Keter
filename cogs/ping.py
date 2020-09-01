import discord
from discord.ext import commands

class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Keter is Online')

    # Commands
    @commands.command()
    async def 핑(self, ctx):
        await ctx.trigger_typing()
        embed = discord.Embed(title="핑", description= f"{str(round(self.client.latency*1000))}ms", color=0xeff0f1)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Ping(client))
