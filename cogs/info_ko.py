import time
import discord
import psutil
import os

from datetime import datetime
from discord.ext import commands
from evs import default

class Information_ko(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")
        self.process = psutil.Process(os.getpid())

    @commands.command()
    async def 핑(self, ctx):
        """ Pong! """
        before = time.monotonic()
        before_ws = int(round(self.bot.latency * 1000, 1))
        message = await ctx.send("🏓 퐁")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"🏓 WS: {before_ws}ms  |  REST: {int(ping)}ms")

    @commands.command(aliases=['봇 초대하기', '초대', '참가'])
    async def 초대하기(self, ctx):
        """ Invite me to your server """
        embed = discord.Embed(title="저를 파티에 초대해주세요!", description=f"**{ctx.author.name}**, 아래의 링크를 사용하세요\n[link](https://discord.com/oauth2/authorize?client_id=749629426777456691&permissions=8&scope=bot)", color=0xeff0f1)
        await ctx.send(embed=embed)

    @commands.command()
    async def 소스코드(self, ctx):
        """ Check out my source code <3 """
        await ctx.send(f"**{ctx.bot.user}** 이 소스 코드로 돌아갑니다:\nhttps://github.com/Shio7/Keter")

    @commands.command(aliases=['지원 서버', '문의 서버'])
    async def 서버(self, ctx):
        """ Get an invite to our support server! """
        if isinstance(ctx.channel, discord.DMChannel) or ctx.guild.id != 749595288280498188:
            return await ctx.send(f"**여기로! {ctx.author.name} 🍻\n<{self.config.botserver}>**")

        await ctx.send(f"**{ctx.author.name}** 이게 제 집이잖아요~ :3")

    @commands.command(aliases=['상태'])
    async def 정보(self, ctx):
        """ About the bot """
        f = open("./lib/economy/cache/version.ccf", "r")
        version = f.read()
        f.close
        ramUsage = self.process.memory_full_info().rss / 1024**2
        avgmembers = round(len(self.bot.users) / len(self.bot.guilds))

        embed = discord.Embed(colour=0xeff0f1)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        embed.add_field(name="마지막 부팅", value=default.timeago(datetime.now() - self.bot.uptime), inline=True)
        embed.add_field(
            name=f"개발자{'' if len(self.config.owners) == 1 else 's'}",
            value=', '.join([str(self.bot.get_user(x)) for x in self.config.owners]),
            inline=True)
        embed.add_field(name="라이브러리", value="discord.py", inline=True)
        embed.add_field(name="유저", value= str(len(ctx.bot.guilds)*avgmembers) + " users", inline=True)
        embed.add_field(name="커맨드 로드", value=len([x.name for x in self.bot.commands]), inline=True)
        embed.add_field(name="램", value=f"{ramUsage:.2f} MB", inline=True)

        await ctx.send(content=f"ℹ About **{ctx.bot.user}** | **" + version + "**", embed=embed)


def setup(bot):
    bot.add_cog(Information_ko(bot))
