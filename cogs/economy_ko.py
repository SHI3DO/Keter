import discord
import time
import psutil
import os
import asyncio
import openpyxl
import random
import math

from datetime import datetime
from discord.ext import commands
from evs import default, permissions

userlib = "./lib/economy/users/"
class economy_ko(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")
        self.process = psutil.Process(os.getpid())
        #폴더생성
        if os.path.isdir("./lib/economy/users"):
            print("user folder exist")
        else:
            os.makedirs("./lib/economy/users")

    #참여
    @commands.command()
    async def 참여(self, ctx):

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
            if os.path.isfile(userlib + str(ctx.author.id) + ".xlsx"):
                embed = discord.Embed(title="케테르 경제", description="이미 참여하셨습니다.", color=0xeff0f1)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="케테르 경제", description="새로 오셨군요? " + str(ctx.author.name) + "님을 위한 파일들을 생성중이에요!",
                                      color=0xeff0f1)
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/750540820842807396/752690012369190942/DARK_KETER_1.png")
                await ctx.send(embed=embed)
                wb = openpyxl.Workbook()
                ws = wb.active
                ws.cell(row=1, column=1).value = "money"
                ws.cell(row=1, column=2).value = "8600000"
                ws.cell(row=1, column=3).value = "0"
                wb.save(userlib + str(ctx.author.id) + ".xlsx")
                wb.close()
                time.sleep(1)
                embed = discord.Embed(title="케테르 경제",
                                      description=str(ctx.author.name) + " 생성 완료!",
                                      color=0xeff0f1)
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

    @commands.command(aliases=['돈내놔', '돈줘'])
    async def 돈받기(self,ctx):
        if os.path.isfile(userlib + str(ctx.author.id) + ".xlsx"):
            num = random.randrange(0,6)
            wb = openpyxl.load_workbook(userlib + str(ctx.author.id) + ".xlsx")
            ws = wb.active
            getmoney = ws.cell(row=1, column=2).value
            getmoney = int(getmoney) + int(num)
            ws.cell(row=1, column=2).value = str(getmoney)
            wb.save(userlib + str(ctx.author.id) + ".xlsx")
            wb.close()
            embed = discord.Embed(title="KET", description="<@" + str(ctx.author.id) + "> " +str(num)+"<:ket:753449741186105375>을 받았어요!", color=0xeff0f1)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="NO", description="먼저 ``.참여``를 입력해서 케테르 경제에 참여해주세요!", color=0xeff0f1)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/750540820842807396/752684853320745000/KETER_PRESTIGE.png")
            await ctx.send(embed=embed)

    @commands.command()
    async def 돈(self, ctx):
        if os.path.isfile(userlib + str(ctx.author.id) + ".xlsx"):
            wb = openpyxl.load_workbook(userlib + str(ctx.author.id) + ".xlsx")
            ws = wb.active
            money = ws.cell(row=1, column=2).value
            wb.close()
            embed = discord.Embed(title="KET", description="<@" + str(ctx.author.id) + "> " + str(money) + "<:ket:753449741186105375>을 가지고 계십니다!", color=0xeff0f1)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="NO", description="먼저 ``.참여``를 입력해서 케테르 경제에 참여해주세요!", color=0xeff0f1)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/750540820842807396/752684853320745000/KETER_PRESTIGE.png")
            await ctx.send(embed=embed)

    @commands.command(aliases=['프리스티지', '프레스티지'])
    async def 호프(self, ctx):
        if os.path.isfile(userlib + str(ctx.author.id) + ".xlsx"):
            wb = openpyxl.load_workbook(userlib + str(ctx.author.id) + ".xlsx")
            ws = wb.active
            prestige = ws.cell(row=1, column=3).value
            wb.close()
            embed = discord.Embed(title="PRESTIGE", description="<@" + str(ctx.author.id) + "> " + str(
                prestige) + "<:pre:753454200658067510>을 가지고 계십니다!", color=0xeff0f1)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="NO", description="먼저 ``.참여``를 입력해서 케테르 경제에 참여해주세요!", color=0xeff0f1)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/750540820842807396/752684853320745000/KETER_PRESTIGE.png")
            await ctx.send(embed=embed)

    @commands.command()
    @commands.check(permissions.is_owner)
    async def 초기화(self,ctx):
        file_list = os.listdir(userlib)
        file_list = [file for file in file_list if file.endswith(".xlsx")]
        for i in range(len(file_list)):
            wb = openpyxl.load_workbook(userlib + file_list[i])
            ws = wb.active
            ws.cell(row=1, column=2).value = "8600000"
            ws.cell(row=1, column=3).value = str(math.ceil(ws.cell(row=1, column=2).value / 1000000000))
            wb.save(userlib + file_list[i])
            wb.close()
        embed = discord.Embed(title="Admin", description="초기화 완료", color=0xeff0f1)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.check(permissions.is_owner)
    async def 돈추가(self, ctx, mention:str, value:int):
        if (ctx.message.mentions.__len__() > 0):
            for user in ctx.message.mentions:
                if os.path.isfile(userlib + str(user.id) + ".xlsx"):
                    wb = openpyxl.load_workbook(userlib + str(user.id) + ".xlsx")
                    ws = wb.active
                    money = ws.cell(row=1, column=2).value
                    money = int(money)+value
                    ws.cell(row=1, column=2).value = money
                    wb.save(userlib + str(user.id) + ".xlsx")
                    wb.close()
                    embed = discord.Embed(title="KET", description=str(money) + "<:ket:753449741186105375> 추가 완료", color=0xeff0f1)
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title="NO", description="유저가 ``케테르 경제``에 참여하지 않았어요..", color=0xeff0f1)
                    embed.set_thumbnail(
                        url="https://cdn.discordapp.com/attachments/750540820842807396/752684853320745000/KETER_PRESTIGE.png")
                    await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(economy_ko(bot))
