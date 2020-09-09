import discord
import time
import psutil
import os
import asyncio

from datetime import datetime
from discord.ext import commands
from evs import default

userlib = "./lib/economy/users/"
class economy_ko(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")
        self.process = psutil.Process(os.getpid())

    @commands.command()
    async def 참여(self, ctx):

        #폴더생성
        if os.path.isdir("./lib/economy/users"):
            print("user folder exist")
        else:
            os.makedirs("./lib/economy/users")

        embed = discord.Embed(title="케테르 경제", description="케테르 경제에 참여하시겠습니까?", color=0xeff0f1)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/750540820842807396/752684853320745000/KETER_PRESTIGE.png")
        msg = await ctx.send(embed=embed)

        def reaction_check_(m):
            if m.message_id == msg.id and m.user_id == ctx.author.id and str(m.emoji) == "✅":
                return True
            return False

        try:
            await msg.add_reaction("✅")
            await self.bot.wait_for('raw_reaction_add', timeout=10.0, check=reaction_check_)
            embed = discord.Embed(title="케테르 경제", description="케테르 경제에 참여하셨습니다.", color=0xeff0f1)
            await ctx.send(embed=embed)

            if os.path.isfile(userlib + str(ctx.author.id) + ".xlsx"):
                embed = discord.Embed(title="케테르 경제", description="이미 참여하셨습니다.", color=0xeff0f1)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="케테르 경제", description="새로 오셨군요? " + str(ctx.author.name) + "님을 위한 파일들을 생성중이에요!",
                                      color=0xeff0f1)
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/750540820842807396/752690012369190942/DARK_KETER_1.png")
                await ctx.send(embed=embed)

        except asyncio.TimeoutError:
            await msg.delete()
            embed = discord.Embed(title="케테르 경제", description="서명하지 않으셨습니다. 다음 기회에..", color=0xeff0f1)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/750540820842807396/752690012369190942/DARK_KETER_1.png")
            await ctx.send(embed=embed)

        except discord.Forbidden:
            embed = discord.Embed(title="케테르 경제", description="케테르 경제에 참여하시겠습니까?", color=0xeff0f1)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/750540820842807396/752684853320745000/KETER_PRESTIGE.png")
            await msg.edit(content=embed)


def setup(bot):
    bot.add_cog(economy_ko(bot))
