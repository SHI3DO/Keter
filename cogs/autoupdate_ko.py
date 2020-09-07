import discord
from discord.ext import commands
from evs import default
from evs import permissions, default, http, dataIO
import requests
import os

class Autoupdate_ko(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    # Commands

    @commands.command()
    @commands.check(permissions.is_owner)
    async def 업데이트(self, ctx, link: str, filename: str):
        await ctx.trigger_typing()
        await ctx.send("소스코드 업데이트 중...")
        r = requests.get(link, allow_redirects=True)
        if os.path.isfile('./cogs/' + filename + ".py"):
            try:
                self.bot.unload_extension(f"cogs.{filename}")
            except Exception as e:
                return await ctx.send(default.traceback_maker(e))
            await ctx.send(f"Unloaded extension **{filename}.py**")
            os.remove('./cogs/' + filename + ".py")
            open('./cogs/' + filename + ".py", 'wb').write(r.content)
        else:
            open('./cogs/' + filename + ".py", 'wb').write(r.content)
        await ctx.send("소스: "+filename+".py")
        """ Loads an extension. """
        try:
            self.bot.load_extension(f"cogs.{filename}")
        except Exception as e:
            return await ctx.send(default.traceback_maker(e))
        await ctx.send(f"**{filename}.py 로드 완료**")


def setup(bot):
    bot.add_cog(Autoupdate_ko(bot))
