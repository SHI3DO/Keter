import discord
from discord.ext import commands
from evs import default
from evs import permissions, default, http, dataIO
import requests

class Autoupdate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    # Commands

    @commands.command()
    @commands.check(permissions.is_owner)
    async def update(self, ctx, link: str, filename: str):
        await ctx.trigger_typing()
        await ctx.send("Updating source code...")
        r = requests.get(link, allow_redirects=True)
        open('./cogs/' + filename + ".py", 'wb').write(r.content)
        await ctx.send("Updated: "+filename+".py")
        """ Loads an extension. """
        try:
            self.bot.load_extension(f"cogs.{filename}")
        except Exception as e:
            return await ctx.send(default.traceback_maker(e))
        await ctx.send(f"Loaded extension **{filename}.py**")


def setup(bot):
    bot.add_cog(Autoupdate(bot))
