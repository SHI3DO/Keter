import discord
from discord.ext import commands
from evs import default

class Userinfo_Ja(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    # Commands
    @commands.command(aliases=['ユーザー情報', 'ユーザ情報', 'ユザー情報', 'ユザ情報'])
    async def __userinfo(self, ctx):
        if (ctx.message.mentions.__len__() > 0):
            for user in ctx.message.mentions:
                embed = discord.Embed(title="**" + user.name + "さんのプロフィール", description="",
                                      color=0xeff0f1)
                embed.add_field(name="**ID**",
                                value=user.id,
                                inline=True)
                embed.add_field(name="**ニックネーム**",
                                value=user.display_name,
                                inline=True)
                embed.add_field(name="**ステイタス**",
                                value=user.status,
                                inline=True)
                embed.add_field(name="**メンション**",
                                value="<@" + str(user.id) + ">",
                                inline=True)
                embed.set_thumbnail(url=user.avatar_url)
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=ctx.author.name + "さんのプロフィール", description="",
                                  color=0xeff0f1)
            embed.add_field(name="**ID**",
                            value=ctx.author.id,
                            inline=True)
            embed.add_field(name="**ニックネーム**",
                            value=ctx.author.display_name,
                            inline=True)
            embed.add_field(name="**ステイタス**",
                            value=ctx.author.status,
                            inline=True)
            embed.add_field(name="**メンション**",
                            value="<@" + str(ctx.author.id) + ">",
                            inline=True)
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Userinfo_Ja(bot))
