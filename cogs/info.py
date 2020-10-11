import time
import discord
import psutil
import os

from datetime import datetime
from discord.ext import commands
from evs import default


class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")
        self.process = psutil.Process(os.getpid())

    @commands.command()
    async def ping(self, ctx):
        """ Pong! """
        before = time.monotonic()
        before_ws = int(round(self.bot.latency * 1000, 1))
        message = await ctx.send("🏓 Pong")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"🏓 WS: {before_ws}ms  |  REST: {int(ping)}ms")

    @commands.command(aliases=['joinme', 'join', 'botinvite'])
    async def invite(self, ctx):
        """ Invite me to your server """
        embed = discord.Embed(title="Invite", description=f"**{ctx.author.name}**, use this URL to invite me\n[link](https://discord.com/oauth2/authorize?client_id=749629426777456691&permissions=8&scope=bot)", color=0xeff0f1)
        await ctx.send(embed=embed)

    @commands.command()
    async def source(self, ctx):
        """ Check out my source code <3 """
        await ctx.send(f"**{ctx.bot.user}** is powered by this source code:\nhttps://github.com/Shio7/Keter")

    @commands.command(aliases=['supportserver', 'feedbackserver'])
    async def botserver(self, ctx):
        """ Get an invite to our support server! """
        if isinstance(ctx.channel, discord.DMChannel) or ctx.guild.id != 749595288280498188:
            return await ctx.send(f"**Here you go {ctx.author.name} 🍻\n<{self.config.botserver}>**")

        await ctx.send(f"**{ctx.author.name}** this is my home you know :3")

    @commands.command(aliases=['info', 'stats', 'status'])
    async def about(self, ctx):
        """ About the bot """
        f = open("./lib/cache/version.ccf", "r")
        version = f.read()
        f.close
        ramUsage = self.process.memory_full_info().rss / 1024**2
        avgmembers = round(len(self.bot.users) / len(self.bot.guilds))

        embed = discord.Embed(colour=0xeff0f1)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        embed.add_field(name="Last boot", value=default.timeago(datetime.now() - self.bot.uptime), inline=True)
        embed.add_field(
            name=f"Developer{'' if len(self.config.owners) == 1 else 's'}",
            value=', '.join([str(self.bot.get_user(x)) for x in self.config.owners]),
            inline=True)
        embed.add_field(name="Library", value="discord.py", inline=True)
        embed.add_field(name="Users", value= str(len(ctx.bot.guilds)*avgmembers) + " users", inline=True)
        embed.add_field(name="Commands loaded", value=len([x.name for x in self.bot.commands]), inline=True)
        embed.add_field(name="RAM", value=f"{ramUsage:.2f} MB", inline=True)

        await ctx.send(content=f"ℹ About **{ctx.bot.user}** | **" + version + "**", embed=embed)
    @commands.command()
    async def serverinfo(self, ctx):
        server = ctx.message.guild
        channel_count = len([x for x in server.channels if type(x) == discord.channel.TextChannel])
        channel__count = len([x for x in server.channels if type(x) == discord.channel.VoiceChannel])
        embed = discord.Embed(title='Server Info',description='',color=0xEFF0F1)
        embed.add_field(name='Name',value=server.name)
        embed.add_field(name='Owner',value=server.owner,inline=True)
        embed.add_field(name='Members',value=server.member_count)
        embed.add_field(name='Region',value=server.region)
        embed.add_field(name='Roles',value=str(len(server.roles)))
        embed.add_field(name='Emojis',value=str(len(server.emojis)))
        embed.add_field(name='Text Channels',value=str(channel_count))
        embed.add_field(name='Voice Channels',value=str(channel__count))
        embed.add_field(name='Server ID',value=server.id)
        embed.add_field(name='Verification Level',value=str(server.verification_level))
        embed.add_field(name='Created At',value=server.created_at.__format__('%A, %B %d %Y, %H:%M:%S'))
        embed.set_thumbnail(url=server.icon_url)
        embed.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Information(bot))
