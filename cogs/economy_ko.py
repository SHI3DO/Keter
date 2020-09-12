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
                ws.cell(row=1, column=1).value = "Hello World" #:)
                ws.cell(row=1, column=2).value = "8600000" #money
                ws.cell(row=1, column=3).value = "0" #pres
                ws.cell(row=1, column=4).value = "-" #rank
                ws.cell(row=2, column=1).value = "None" #status
                ws.cell(row=2, column=2).value = "0" #perfect
                ws.cell(row=2, column=3).value = "0" #great
                ws.cell(row=2, column=4).value = "0" #good
                ws.cell(row=2, column=5).value = "0" #bad
                ws.cell(row=3, column=1).value = "0" #tsucc
                ws.cell(row=3, column=2).value = "0" #tfail
                ws.cell(row=3, column=3).value = "0" #fails
                ws.cell(row=4, column=1).value = "0" #home count
                ws.cell(row=4, column=2).value = "[1]" #title
                ws.cell(row=4, column=3).value = "1" #header
                ws.cell(row=4, column=4).value = "1" #tail
                ws.cell(row=5, column=1).value = "100" #HP
                ws.cell(row=5, column=2).value = "100" #STR
                ws.cell(row=5, column=3).value = "100" #DEF
                ws.cell(row=5, column=4).value = "100" #INT
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
                prestige) + "<:pre:753458787465297993>을 가지고 계십니다!", color=0xeff0f1)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="NO", description="먼저 ``.참여``를 입력해서 케테르 경제에 참여해주세요!", color=0xeff0f1)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/750540820842807396/752684853320745000/KETER_PRESTIGE.png")
            await ctx.send(embed=embed)

    @commands.command(aliases=['ㄷㅂ'])
    async def 도박(self, ctx, val:int):
        if os.path.isfile(userlib + str(ctx.author.id) + ".xlsx"):
            wb = openpyxl.load_workbook(userlib + str(ctx.author.id) + ".xlsx")
            ws = wb.active
            money = ws.cell(row=1, column=2).value
            if int(money) > val:
                discrim = random.random()
                if discrim < 0.02:
                    ws.cell(row=1, column=2).value += 11*val
                    ws.cell(row=1, column=12).value = "0"
                    embed = discord.Embed(title="도박", description="축하합니다! 대박이 나서 12배를 획득 하셨어요! 🎉", color=0xeff0f1)
                elif 0.02 < discrim < 0.05 + math.sqrt(ws.cell(row=1, column=12).value*100)/100:
                    ws.cell(row=1, column=2).value += 2*val
                    ws.cell(row=1, column=12).value = "0"
                    embed = discord.Embed(title="도박", description="축하합니다! 도박에 성공하셔서 3배를 획득 하셨어요! 🎉", color=0xeff0f1)
                elif 0.05 + math.sqrt(ws.cell(row=1, column=12).value*100)/100 < discrim < 0.05 + math.sqrt(ws.cell(row=1, column=12).value*100)/50:
                    ws.cell(row=1, column=2).value += val
                    ws.cell(row=1, column=12).value = "0"
                    embed = discord.Embed(title="도박", description="축하합니다! 도박에 성공하셔서 2배를 획득 하셨어요! 🎉", color=0xeff0f1)
                else:
                    emj = "<:dar:754345236574109716>"
                    ws.cell(row=1, column=2).value -= val
                    ws.cell(row=1, column=12).value = str(int(ws.cell(row=1, column=12).value) + 1)
                    embed = discord.Embed(title="도박", description="도박에 실패하여 돈을 잃으셨습니다. " + emj, color=0xeff0f1)
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="NO", description="보유하신 잔액보다 큰 금액을 베팅할 수는 없어요.", color=0xeff0f1)
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
            if int(ws.cell(row=1, column=3).value) <= 1000:
                ws.cell(row=1, column=3).value = str(int(ws.cell(row=1, column=3).value) + math.ceil(int(ws.cell(row=1, column=2).value) / 1000000000))
            else:
                ws.cell(row=1, column=3).value = str(round(int(ws.cell(row=1, column=3).value) / 2) + math.ceil(int(ws.cell(row=1, column=2).value) / 1000000000))
            ws.cell(row=1, column=2).value = "8600000"
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

    @commands.command()
    @commands.check(permissions.is_owner)
    async def 전체초기화(self, ctx):
        file_list = os.listdir(userlib)
        file_list = [file for file in file_list if file.endswith(".xlsx")]
        for i in range(len(file_list)):
            os.remove(userlib + file_list[i])
            await ctx.send(file_list[i] + "deleted")

def setup(bot):
    bot.add_cog(economy_ko(bot))
