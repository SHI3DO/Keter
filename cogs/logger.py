# Last Edited: 2020-12-29
# Contributor: Shio
# Code Description: 로거

import discord
from discord.ext import commands
from evs import default
from evs import permissions, default, http, dataIO
import requests
import os
from datetime import datetime

logfolder = "./lib/logs/"
loadingurl = "https://cdn.discordapp.com/attachments/751791353779716099/793328911568076800/keterloading.gif"

class Logger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # 폴더생성
        if os.path.isdir("./lib/logs"):
            print("Logs exist")
        else:
            os.makedirs("./lib/logs")


    @commands.command()
    @commands.check(permissions.is_owner)
    async def 로그(self, ctx):
        embed = discord.Embed(title="관리", description= "로그 기능을 활성화 하시겠습니까?", color=0xeff0f1)
        embed.set_footer(icon_url=ctx.author.avatar_url,
                         text=ctx.author.name + "#" + ctx.author.discriminator + " " + str(
                             datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
        embed.set_thumbnail(url= ctx.guild.icon_url)
        msg = await ctx.send(embed=embed)

        def reaction_check_(m):
            if m.message_id == msg.id and m.user_id == ctx.author.id and str(m.emoji) == "✅":
                return True
            return False

        def msg_check(m):
            if m.author.id == ctx.author.id:
                return True
            return False

        try:
            await msg.add_reaction("✅")
            await self.bot.wait_for('raw_reaction_add', timeout=10.0, check=reaction_check_)
            if os.path.isfile(logfolder+str(ctx.guild.id)+".ktx"):
                print("로그파일 존재")
                try:
                    logf = open(logfolder + str(ctx.guild.id) + ".ktx", "r")
                    embed = discord.Embed(title="관리",
                                          description="기존에 설정 되어 있는 " + "<#" + logf.read() + ">" + " 채널을 변경하시겠습니까?",
                                          color=0xeff0f1)
                    embed.set_footer(icon_url=ctx.author.avatar_url,
                                     text=ctx.author.name + "#" + ctx.author.discriminator + " " + str(
                                         datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
                    embed.set_thumbnail(url=ctx.guild.icon_url)
                    msg = await ctx.send(embed=embed)
                    logf.close()

                    await msg.add_reaction("✅")
                    await self.bot.wait_for('raw_reaction_add', timeout=10.0, check=reaction_check_)

                    try:
                        await msg.delete()
                        embed = discord.Embed(title="관리",
                                              description="새로운 채널을 입력해주세요.",
                                              color=0xeff0f1)
                        embed.set_footer(icon_url=ctx.author.avatar_url,
                                         text=ctx.author.name + "#" + ctx.author.discriminator + " " + str(
                                             datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
                        embed.set_thumbnail(url=loadingurl)
                        msg = await ctx.send(embed=embed)

                        try:
                            rsg = await self.bot.wait_for('message', timeout=15.0, check=msg_check)
                            logf = open(logfolder + str(ctx.guild.id) + ".ktx", "w")
                            logf.write(rsg.content[2:][:-1])
                            logf.close()

                            embed = discord.Embed(title="관리", description="수정 완료하였습니다.", color=0xeff0f1)
                            embed.set_footer(icon_url=ctx.author.avatar_url,
                                             text=ctx.author.name + "#" + ctx.author.discriminator + " " + str(
                                                 datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
                            embed.set_thumbnail(url=ctx.guild.icon_url)
                            await msg.delete()
                            await ctx.send(embed=embed)

                        except:
                            await msg.delete()
                            embed = discord.Embed(title="관리", description="에러 발생!", color=0xeff0f1)
                            embed.set_footer(icon_url=ctx.author.avatar_url,
                                             text=ctx.author.name + "#" + ctx.author.discriminator + " " + str(
                                                 datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
                            embed.set_thumbnail(url=ctx.guild.icon_url)
                            await ctx.send(embed=embed)

                    except:
                        await msg.delete()
                        embed = discord.Embed(title="관리", description="에러 발생!", color=0xeff0f1)
                        embed.set_footer(icon_url=ctx.author.avatar_url,
                                         text=ctx.author.name + "#" + ctx.author.discriminator + " " + str(
                                             datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
                        embed.set_thumbnail(url=ctx.guild.icon_url)
                        await ctx.send(embed=embed)

                except:
                    await msg.delete()
                    embed = discord.Embed(title="관리", description="에러 발생!", color=0xeff0f1)
                    embed.set_footer(icon_url=ctx.author.avatar_url,
                                     text=ctx.author.name + "#" + ctx.author.discriminator + " " + str(
                                         datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
                    embed.set_thumbnail(url=ctx.guild.icon_url)
                    await ctx.send(embed=embed)

            else:
                try:
                    await msg.delete()
                    embed = discord.Embed(title="관리",
                                          description="새로운 채널을 입력해주세요.",
                                          color=0xeff0f1)
                    embed.set_footer(icon_url=ctx.author.avatar_url,
                                     text=ctx.author.name + "#" + ctx.author.discriminator + " " + str(
                                         datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
                    embed.set_thumbnail(url=loadingurl)
                    msg = await ctx.send(embed=embed)

                    try:
                        ksg = await self.bot.wait_for('message', timeout=15.0, check=msg_check)
                        await msg.delete()
                        logf = open(logfolder + str(ctx.guild.id) + ".ktx", "w")
                        logf.write(ksg.content[2:][:-1])
                        logf.close()

                        embed = discord.Embed(title="관리", description="로그 기능, 세팅 완료하였습니다!", color=0xeff0f1)
                        embed.set_footer(icon_url=ctx.author.avatar_url,
                                         text=ctx.author.name + "#" + ctx.author.discriminator + " " + str(
                                             datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
                        embed.set_thumbnail(url=ctx.guild.icon_url)
                        await ctx.send(embed=embed)

                    except:
                        await msg.delete()
                        embed = discord.Embed(title="관리", description="에러 발생!", color=0xeff0f1)
                        embed.set_footer(icon_url=ctx.author.avatar_url,
                                         text=ctx.author.name + "#" + ctx.author.discriminator + " " + str(
                                             datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
                        embed.set_thumbnail(url=ctx.guild.icon_url)
                        await ctx.send(embed=embed)

                except:
                    await msg.delete()
                    embed = discord.Embed(title="관리", description="에러 발생!", color=0xeff0f1)
                    embed.set_footer(icon_url=ctx.author.avatar_url,
                                     text=ctx.author.name + "#" + ctx.author.discriminator + " " + str(
                                         datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
                    embed.set_thumbnail(url=ctx.guild.icon_url)
                    await ctx.send(embed=embed)

        except:
            await msg.delete()
            embed = discord.Embed(title="관리", description="취소되었습니다.", color=0xeff0f1)
            embed.set_footer(icon_url=ctx.author.avatar_url,
                             text=ctx.author.name + "#" + ctx.author.discriminator + " " + str(
                                 datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
            embed.set_thumbnail(url=ctx.guild.icon_url)
            await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, ctx):
        if os.path.isfile(logfolder+str(ctx.guild.id)+".ktx"):
            logf = open(logfolder + str(ctx.guild.id) + ".ktx", "r")
            log_channel = logf.read()
            logf.close()

            print("log_channel = " + log_channel)
            print("author id = " + str(ctx.author.id))
            print(ctx.content)
            channel = self.bot.get_channel(int(log_channel))

            embed = discord.Embed(title="Message Deleted", description= "The message sent by <@" + str(ctx.author.id) + "> in <#" + str(ctx.channel.id) + "> was deleted", color=0xeff0f1)
            embed.add_field(name="**Message**", value=str(ctx.content))
            embed.set_footer(icon_url=ctx.author.avatar_url,
                             text=ctx.author.name + "#" + ctx.author.discriminator + " " + str(
                                 datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
            await channel.send(embed=embed)

        else:
            print("로그 dir 없음")

def setup(bot):
    bot.add_cog(Logger(bot))
