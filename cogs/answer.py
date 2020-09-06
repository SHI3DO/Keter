import discord
from discord.ext import commands
import wolframalpha

class Answer(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command(name = 'answer')
    async def _answer(self, ctx, *, content:str):
        await ctx.trigger_typing()
        app_id = "VPR9G7-54PV53JYTK"
        client = wolframalpha.Client(app_id)
        answer = next(res.results).text
        embed = discord.Embed(title="Result", description=answer, color=0xeff0f1)
        await ctx.send(embed=embed)
        try:
            res = client.query(content)
        except:
            embed = discord.Embed(title="IDK", description="I don't know about This bruuu.", color=0xeff0f1)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/751791353779716099/751791533958627368/DARK_KETER.png")
            await ctx.send(embed=embed)
            return

def setup(client):
    client.add_cog(Answer(client))
