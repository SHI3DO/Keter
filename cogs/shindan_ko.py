import discord
from discord.ext import commands
from evs import default

class Shindan_ko(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    # Commands
    @commands.command(name="진단")
    async def _say(self, ctx, *, content:str):
            await ctx.send(str + "에 대한 진단을 만드시겠습니까?")
            def reaction_check_(m):
            if m.message_id == msg.id and m.user_id == ctx.author.id and str(m.emoji) == "✅":
                return True
            return False

        try:
            await msg.add_reaction("✅")
            await self.bot.wait_for('raw_reaction_add', timeout=10.0, check=reaction_check_)
            await ctx.send(str + "에 대한 진단")


        except asyncio.TimeoutError:
            await msg.delete()
            embed = discord.Embed(title="진단메이커", description="동의하지 않으셨습니다", color=0xeff0f1)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/750540820842807396/752690012369190942/DARK_KETER_1.png")
            await ctx.send(embed=embed)

        except discord.Forbidden:
            embed = discord.Embed(title="진단메이커", description="동의하지 않으셨습니다", color=0xeff0f1)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/750540820842807396/752684853320745000/KETER_PRESTIGE.png")
            await msg.edit(content=embed)
            

def setup(bot):
    bot.add_cog(Shindan_ko(bot))
