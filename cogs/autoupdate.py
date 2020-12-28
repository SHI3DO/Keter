# Last Edited: 2020-12-18
# Contributor: Shio
# Code Description: 업데이트 관련 코드들, 한국어만 지원 (관리자 4명 모두 한국인)

import discord
from discord.ext import commands
from evs import default
from evs import permissions, default, http, dataIO
import requests
import os
from datetime import datetime

parfait_url = "https://cdn.discordapp.com/attachments/751791353779716099/792924251803877406/PARFAIT_ICON-1.png"

class Autoupdate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    # Commands

    @commands.command()
    @commands.check(permissions.is_owner)
    async def 업데이트(self, ctx, *, content:str):
        content = content.split()
        embed = discord.Embed(title="관리모듈 A1", description=content[2] + "모듈을 업데이트 하시겠습니까?", color=0xeff0f1)
        embed.set_footer(icon_url=ctx.author.avatar_url,
                         text=ctx.author.name + "#" + ctx.author.discriminator + " " + str(
                             datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
        embed.set_thumbnail(url=parfait_url)
        msg = await ctx.send(embed=embed)

        def reaction_check_(m):
            if m.message_id == msg.id and m.user_id == ctx.author.id and str(m.emoji) == "✅":
                return True
            return False

        try:
            await msg.add_reaction("✅")
            await self.bot.wait_for('raw_reaction_add', timeout=10.0, check=reaction_check_)
            await ctx.trigger_typing()

            try:
                r = requests.get(content[0], allow_redirects=True)

                if os.path.isfile(content[1] + content[2] + ".py"):
                    try:
                        self.bot.unload_extension(f"cogs.{content[2]}")
                    except Exception as e:
                        return await ctx.send(default.traceback_maker(e))
                    os.remove(content[1] + content[2] + ".py")
                    open(content[1] + content[2] + ".py", 'wb').write(r.content)

                    try:
                        self.bot.load_extension(f"cogs.{content[2]}")
                    except Exception as e:
                        return await ctx.send(default.traceback_maker(e))
                    embed = discord.Embed(title="관리모듈 A1", description=content[2] + ".py 로드 완료!",
                                          color=0xeff0f1)
                    embed.set_footer(icon_url=ctx.author.avatar_url,
                                     text=ctx.author.name + "#" + ctx.author.discriminator + " " + str(
                                         datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
                    embed.set_thumbnail(url=parfait_url)
                    msg = await ctx.send(embed=embed)

                else:
                    embed = discord.Embed(title="관리모듈 A1", description=content[2] + "모듈이 없어요. `다운로드` 커맨드를 사용해 주세요.",
                                          color=0xeff0f1)
                    embed.set_footer(icon_url=ctx.author.avatar_url,
                                     text=ctx.author.name + "#" + ctx.author.discriminator + " " + str(
                                         datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
                    embed.set_thumbnail(url=parfait_url)
                    msg = await ctx.send(embed=embed)
            except:
                embed = discord.Embed(title="관리모듈 A1", description="에러 발생!",
                                      color=0xeff0f1)
                embed.set_footer(icon_url=ctx.author.avatar_url,
                                 text=ctx.author.name + "#" + ctx.author.discriminator + " " + str(
                                     datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
                embed.set_thumbnail(url=parfait_url)
                msg = await ctx.send(embed=embed)

        except:
            await msg.delete()
            embed = discord.Embed(title="관리모듈 A1", description="동의하지 않으셨습니다.", color=0xeff0f1)
            embed.set_footer(icon_url=ctx.author.avatar_url,
                             text=ctx.author.name + "#" + ctx.author.discriminator + " " + str(
                                 datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
            embed.set_thumbnail(url=parfait_url)
            await ctx.send(embed=embed)

    @commands.command()
    @commands.check(permissions.is_owner)
    async def 다운로드(self, ctx, *, content:str):
        content = content.split()
        embed = discord.Embed(title="관리모듈 A1", description=content[2] + "모듈을 다운로드 하시겠습니까?", color=0xeff0f1)
        embed.set_footer(icon_url=ctx.author.avatar_url,
                         text=ctx.author.name + "#" + ctx.author.discriminator + " " + str(
                             datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
        msg = await ctx.send(embed=embed)

        def reaction_check_(m):
            if m.message_id == msg.id and m.user_id == ctx.author.id and str(m.emoji) == "✅":
                return True
            return False

        try:
            await msg.add_reaction("✅")
            await self.bot.wait_for('raw_reaction_add', timeout=10.0, check=reaction_check_)
            await ctx.trigger_typing()
            try:
                r = requests.get(content[0], allow_redirects=True)

                if os.path.isfile(content[1] + content[2] + ".py"):
                    embed = discord.Embed(title="관리모듈 A1",
                                        description=content[2] + "모듈이 이미 있어요. `업데이트` 커맨드를 사용해 주세요.",
                                        color=0xeff0f1)
                    embed.set_footer(icon_url=ctx.author.avatar_url,
                                         text=ctx.author.name + "#" + ctx.author.discriminator + " " + str(
                                             datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
                    msg = await ctx.send(embed=embed)

                else:
                    open(content[1] + content[2] + ".py", 'wb').write(r.content)
                    try:
                        self.bot.load_extension(f"cogs.{content[2]}")
                    except Exception as e:
                        return await ctx.send(default.traceback_maker(e))
                    embed = discord.Embed(title="관리모듈 A1",
                                          description=content[2] + "모듈 다운로드 완료! 로드까지도 완료했어요!",
                                          color=0xeff0f1)
                    embed.set_footer(icon_url=ctx.author.avatar_url,
                                     text=ctx.author.name + "#" + ctx.author.discriminator + " " + str(
                                         datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
                    msg = await ctx.send(embed=embed)

            except:
                embed = discord.Embed(title="관리모듈 A1", description="에러 발생!",
                                      color=0xeff0f1)
                embed.set_footer(icon_url=ctx.author.avatar_url,
                                 text=ctx.author.name + "#" + ctx.author.discriminator + " " + str(
                                     datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
                embed.set_thumbnail(url=parfait_url)
                msg = await ctx.send(embed=embed)

        except:
            await msg.delete()
            embed = discord.Embed(title="관리모듈 A1", description="동의하지 않으셨습니다.", color=0xeff0f1)
            embed.set_footer(icon_url=ctx.author.avatar_url,
                             text=ctx.author.name + "#" + ctx.author.discriminator + " " + str(
                                 datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
            await ctx.send(embed=embed)


    @commands.command()
    @commands.check(permissions.is_owner)
    async def 지우기(self, ctx, filename:str):
        embed = discord.Embed(title="관리모듈 A1", description=filename + "모듈을 지우시겠습니까?", color=0xeff0f1)
        embed.set_footer(icon_url=ctx.author.avatar_url,
                         text=ctx.author.name + "#" + ctx.author.discriminator + " " + str(
                             datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
        msg = await ctx.send(embed=embed)

        def reaction_check_(m):
            if m.message_id == msg.id and m.user_id == ctx.author.id and str(m.emoji) == "✅":
                return True
            return False

        try:
            await msg.add_reaction("✅")
            await self.bot.wait_for('raw_reaction_add', timeout=10.0, check=reaction_check_)
            await ctx.trigger_typing()

            if os.path.isfile('./cogs/' + filename + ".py"):
                try:
                    self.bot.unload_extension(f"cogs.{filename}")
                except Exception as e:
                    return await ctx.send(default.traceback_maker(e))
                os.remove('./cogs/' + filename + ".py")
                embed = discord.Embed(title="관리모듈 A1", description=filename + ".py 삭제 완료!",
                                      color=0xeff0f1)
                embed.set_footer(icon_url=ctx.author.avatar_url,
                                 text=ctx.author.name + "#" + ctx.author.discriminator + " " + str(
                                     datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
                embed.set_thumbnail(url=parfait_url)
                msg = await ctx.send(embed=embed)

            else:
                embed = discord.Embed(title="관리모듈 A1", description="에러 발생!",
                                      color=0xeff0f1)
                embed.set_footer(icon_url=ctx.author.avatar_url,
                                 text=ctx.author.name + "#" + ctx.author.discriminator + " " + str(
                                     datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
                embed.set_thumbnail(url=parfait_url)
                msg = await ctx.send(embed=embed)

        except:
            await msg.delete()
            embed = discord.Embed(title="관리모듈 A1", description="동의하지 않으셨습니다.", color=0xeff0f1)
            embed.set_footer(icon_url=ctx.author.avatar_url,
                             text=ctx.author.name + "#" + ctx.author.discriminator + " " + str(
                                 datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
            await ctx.send(embed=embed)
            
def setup(bot):
    bot.add_cog(Autoupdate(bot))
