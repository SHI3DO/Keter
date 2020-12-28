import discord
from discord.ext import commands
from evs import default
from evs import permissions, default, http, dataIO
import requests
import os
from datetime import datetime

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
        msg = await ctx.send(embed=embed)

        def reaction_check_(m):
            if m.message_id == msg.id and m.user_id == ctx.author.id and str(m.emoji) == "✅":
                return True
            return False

        try:
            await msg.add_reaction("✅")
            await self.bot.wait_for('raw_reaction_add', timeout=10.0, check=reaction_check_)
            await ctx.trigger_typing()
            await ctx.send("Updating source code...")
            r = requests.get(content[0], allow_redirects=True)
            if os.path.isfile(content[1]+content[2]+".py"):
                try:
                    self.bot.unload_extension(f"cogs.{content[2]}")
                except Exception as e:
                    return await ctx.send(default.traceback_maker(e))
                await ctx.send(f"Unloaded extension **{content[2]}.py**")
                os.remove(content[1]+content[2]+".py")
                open(content[1]+content[2]+".py", 'wb').write(r.content)
            else:
                open(content[1]+content[2]+".py", 'wb').write(r.content)

            await ctx.send("Updated: " + content[2] + ".py")
            """ Loads an extension. """
            try:
                self.bot.load_extension(f"cogs.{content[2]}")
            except Exception as e:
                return await ctx.send(default.traceback_maker(e))
            await ctx.send(f"Loaded extension **{content[2]}.py**")

        except:
            await msg.delete()
            embed = discord.Embed(title="관리모듈 A1", description="동의하지 않으셨습니다.", color=0xeff0f1)
            embed.set_footer(icon_url=ctx.author.avatar_url,
                             text=ctx.author.name + "#" + ctx.author.discriminator + " " + str(
                                 datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
            await ctx.send(embed=embed)


    @commands.command()
    @commands.check(permissions.is_owner)
    async def 지우기(self, ctx, filename: str):
        if os.path.isfile('./cogs/' + filename + ".py"):
            try:
                self.bot.unload_extension(f"cogs.{filename}")
            except Exception as e:
                return await ctx.send(default.traceback_maker(e))
            await ctx.send(f"Unloaded extension **{filename}.py**")
            os.remove('./cogs/' + filename + ".py")
            await ctx.send(f"**{filename}.py** 삭제완료")
        else:
            await ctx.send(f"**{filename}.py 찾을 수 없음**")
            
    @commands.command()
    @commands.check(permissions.is_owner)
    async def allupdate(self, ctx):
        await ctx.trigger_typing()
        await ctx.send("Updating source code...")
        for file in os.listdir("cogs"):
            if file.endswith(".py"):
                name = file[:-3]
                link = "https://raw.githubusercontent.com/Shio7/Keter/master/cogs/" + name + ".py"
                r = requests.get(link, allow_redirects=True)
                if os.path.isfile('./cogs/' + name + ".py"):
                    try:
                        self.bot.unload_extension(f"cogs.{name}")
                    except Exception as e:
                        return await ctx.send(default.traceback_maker(e))
                    await ctx.send(f"Unloaded extension **{name}.py**")
                    os.remove('./cogs/' + name + ".py")
                    open('./cogs/' + name + ".py", 'wb').write(r.content)
                else:
                    open('./cogs/' + name + ".py", 'wb').write(r.content)
                await ctx.send("Updated: "+name+".py")

                try:
                    self.bot.load_extension(f"cogs.{name}")
                except Exception as e:
                    return await ctx.send(default.traceback_maker(e))
                await ctx.send(f"Loaded extension **{name}.py**") 
        await ctx.send("All modules updated")      
            
def setup(bot):
    bot.add_cog(Autoupdate(bot))
