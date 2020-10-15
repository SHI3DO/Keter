import discord
from discord.ext import commands
import wolframalpha
from evs import default
from evs.data import Bot, HelpFormat
config = default.get("config.json")

class Answer_ja(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command(name = '正解')
    async def __answer(self, ctx, *, content:str):
        await ctx.trigger_typing()
        app_id = config.wolframapi_token
        client = wolframalpha.Client(app_id)
        try:
            res = client.query(content)
        except:
            embed = discord.Embed(title="分かんねえぇよ...", description="正解が見つかりませんでした。", color=0xeff0f1)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/751791353779716099/751791533958627368/DARK_KETER.png")
            await ctx.send(embed=embed)
            return
        answer = next(res.results).text
        embed = discord.Embed(title="答えは", description=answer, color=0xeff0f1)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Answer_ja(client))
