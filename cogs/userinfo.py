import discord
from discord.ext import commands
from evs import default

class Userinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    # Commands
    @commands.command()
    async def userinfo(self, ctx):
        if (ctx.message.mentions.__len__() > 0):
            for user in ctx.message.mentions:
                embed = discord.Embed(title="**" + user.name + "'s Profile", description="",
                                      color=0xeff0f1)
                embed.add_field(name="**Username**",
                                value=user.display_name,
                                inline=True)
                embed.add_field(name="**Status**",
                                value=user.status,
                                inline=True)  
                embed.add_field(name="**ID**",
                                value=user.id,
                                inline=True)
                embed.add_field(name="**Mention**",
                                value="<@" + str(user.id) + ">",
                                inline=True)
                embed.add_field(name='**Account created at**',
                                value=user.created_at.__format__('%A, %B %d %Y, %H:%M:%S'),
                                inline=True)
                embed.set_thumbnail(url=user.avatar_url)
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=ctx.author.name + "'s Profile", description="",
                                  color=0xeff0f1)
            embed.add_field(name="**Username**",
                            value=ctx.author.display_name,
                            inline=True)
            embed.add_field(name="**Status**",
                            value=ctx.author.status,
                            inline=True)
            embed.add_field(name="**ID**",
                            value=ctx.author.id,
                            inline=True)
            embed.add_field(name="**Mention**",
                            value="<@" + str(ctx.author.id) + ">",
                            inline=True)
            embed.add_field(name="**Account created at**",
                            value=ctx.author.created_at.__format__('%A, %B %d %Y, %H:%M:%S'),
                            inline=True)
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Userinfo(bot))
