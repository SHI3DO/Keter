import discord
from discord.ext import commands
import wolframalpha

class Calculate(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command(name = '계산')
    async def _calculate(self, ctx, *, content:str):
        await ctx.trigger_typing()
        app_id = "VPR9G7-54PV53JYTK"
        client = wolframalpha.Client(app_id)
        res = client.query(content)
        answer = next(res.results).text
        embed = discord.Embed(title="Result", description=answer, color=0xeff0f1)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Calculate(client))
