import time
import discord
import psutil
import os

from datetime import datetime
from discord.ext import commands
from evs import default

class Information_ja(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")
        self.process = psutil.Process(os.getpid())

    @commands.command()
    async def ピン(self, ctx):
        """ Pong! """
        before = time.monotonic()
        before_ws = int(round(self.bot.latency * 1000, 1))
        message = await ctx.send("🏓 ポン")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"🏓 WS: {before_ws}ms  |  REST: {int(ping)}ms")

    @commands.command(aliases=['ボットを招待する', '招待', '参加'])
    async def 招待する(self, ctx):
        """ Invite me to your server """
        embed = discord.Embed(title="私をパーティーに招待させてください！", description=f"**{ctx.author.name}**, こちらのリンクを使ってください。\n[link](https://discord.com/oauth2/authorize?client_id=749629426777456691&permissions=8&scope=bot)", color=0xeff0f1)
        await ctx.send(embed=embed)

    @commands.command()
    async def コード(self, ctx):
        """ Check out my source code <3 """
        await ctx.send(f"**{ctx.bot.user}** コードはこちらからご確認ください。:\nhttps://github.com/Shio7/Keter")

    @commands.command(aliases=['サーバ', 'サバー', 'サバ'])
    async def サーバー(self, ctx):
        """ Get an invite to our support server! """
        if isinstance(ctx.channel, discord.DMChannel) or ctx.guild.id != 749595288280498188:
            return await ctx.send(f"**こちらえ! {ctx.author.name} 🍻\n<{self.config.botserver}>**")

        await ctx.send(f"**{ctx.author.name}** ここが私のサーバーです~ :3")

    @commands.command(aliases=['常態'])
    async def 情報(self, ctx):
        """ About the bot """
        f = open("./lib/cache/version.ccf", "r")
        version = f.read()
        f.close
        ramUsage = self.process.memory_full_info().rss / 1024**2
        avgmembers = round(len(self.bot.users) / len(self.bot.guilds))

        embed = discord.Embed(colour=0xeff0f1)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        embed.add_field(name="最後のリブート", value=default.timeago(datetime.now() - self.bot.uptime), inline=True)
        embed.add_field(
            name=f"開発陣{'' if len(self.config.owners) == 1 else 's'}",
            value=', '.join([str(self.bot.get_user(x)) for x in self.config.owners]),
            inline=True)
        embed.add_field(name="ライブラリ", value="discord.py", inline=True)
        embed.add_field(name="サーバー", value=f"{len(ctx.bot.guilds)} ( avg: {avgmembers} users/server )", inline=True)
        embed.add_field(name="コマンド", value=len([x.name for x in self.bot.commands]), inline=True)
        embed.add_field(name="ラム", value=f"{ramUsage:.2f} MB", inline=True)

        await ctx.send(content=f"ℹ About **{ctx.bot.user}** | **" + version + "**", embed=embed)


def setup(bot):
    bot.add_cog(Information_ja(bot))
