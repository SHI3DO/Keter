import discord
from discord.ext import commands
from evs import default

class Serverinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    @commands.command()
        async def serverinfo(self, ctx):
            if (ctx.message.mentions.__len__() > 0):
                server = ctx.message.guild
                channel_count = len([x for x in server.channels if type(x) == discord.channel.TextChannel])
                channel__count = len([x for x in server.channels if type(x) == discord.channel.VoiceChannel])
                embed = discord.Embed(title='Server Info',description='',color=0xFF4500)
                embed.add_field(name='Name',value=server.name)
                embed.add_field(name='Owner',value=server.owner,inline=True)
                embed.add_field(name='Members',value=server.member_count)
                embed.add_field(name='Region',value=server.region)
                embed.add_field(name='Roles',value=str(len(server.roles)))
                embed.add_field(name='Emojis',value=str(len(server.emojis)))
                embed.add_field(name='Server ID',value=server.id)
                embed.add_field(name='Text Channels',value=str(channel_count))
                embed.add_field(name='Voice Channels',value=str(channel__count))
                embed.add_field(name='Verification Level',value=str(server.verification_level))
                embed.set_thumbnail(url=server.icon_url)
                await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Serverinfo(bot))