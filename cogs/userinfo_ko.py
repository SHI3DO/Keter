import discord
from discord.ext import commands
from evs import default

class Userinfo_Ko(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    # Commands
    @commands.command(name='유저정보')
    async def _userinfo(self, ctx):
        if (ctx.message.mentions.__len__() > 0):
            for user in ctx.message.mentions:
                embed = discord.Embed(title="**" + user.name + "**님의 프로필", description="",
                                      color=0xeff0f1)
                embed.add_field(name="**아이디**",
                                value=user.id,
                                inline=True)
                embed.add_field(name="**별명**",
                                value=user.display_name,
                                inline=True)
                embed.add_field(name="**상태**",
                                value=user.status,
                                inline=True)
                embed.add_field(name="**언급**",
                                value="<@" + str(user.id) + ">",
                                inline=True)
                embed.set_thumbnail(url=user.avatar_url)
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=ctx.author.name + "님의 프로필", description="",
                                  color=0xeff0f1)
            embed.add_field(name="**아이디**",
                            value=ctx.author.id,
                            inline=True)
            embed.add_field(name="**별명**",
                            value=ctx.author.display_name,
                            inline=True)
            embed.add_field(name="**상태**",
                            value=ctx.author.status,
                            inline=True)
            embed.add_field(name="**언급**",
                            value="<@" + str(ctx.author.id) + ">",
                            inline=True)
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Userinfo_Ko(bot))
