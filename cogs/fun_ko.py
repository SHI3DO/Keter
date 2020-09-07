import random
import time
import discord
import urllib
import secrets
import asyncio
import aiohttp
import re

from io import BytesIO
from discord.ext import commands
from evs import lists, permissions, http, default, argparser


class Fun_Commands_ko(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    @commands.command(aliases=['8볼'])
    async def 질문(self, ctx, *, question: commands.clean_content):
        """ Consult 8ball to receive an answer """
        answer = random.choice(lists.ballresponse)
        await ctx.send(f"🎱 **Question:** {question}\n**Answer:** {answer}")

    async def randomimageapi_(self, ctx, url, endpoint):
        try:
            r = await http.get(url, res_method="json", no_cache=True)
        except aiohttp.ClientConnectorError:
            return await ctx.send("The API seems to be down...")
        except aiohttp.ContentTypeError:
            return await ctx.send("The API returned an error or didn't return JSON...")

        await ctx.send(r[endpoint])

    async def api_image_creator_(self, ctx, url, filename, content=None):
        async with ctx.channel.typing():
            req = await http.get(url, res_method="read")

            if req is None:
                return await ctx.send("I couldn't create the image ;-;")

            bio = BytesIO(req)
            bio.seek(0)
            await ctx.send(content=content, file=discord.File(bio, filename=filename))

    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def 고양이(self, ctx):
        """ Posts a random cat """
        await self.randomimageapi_(ctx, 'https://api.alexflipnote.dev/cats', 'file')

    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def 개(self, ctx):
        """ Posts a random dog """
        await self.randomimageapi_(ctx, 'https://api.alexflipnote.dev/dogs', 'file')

    @commands.command(aliases=["조류"])
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def 새(self, ctx):
        """ Posts a random birb """
        await self.randomimageapi_(ctx, 'https://api.alexflipnote.dev/birb', 'file')

    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def 오리(self, ctx):
        """ Posts a random duck """
        await self.randomimageapi_(ctx, 'https://random-d.uk/api/v1/random', 'url')

    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def 커피(self, ctx):
        """ Posts a random coffee """
        await self.randomimageapi_(ctx, 'https://coffee.alexflipnote.dev/random.json', 'file')

    @commands.command(aliases=['동전 던지기', '코인'])
    async def 동전(self, ctx):
        """ Coinflip! """
        coinsides = ['앞면', '뒷면']
        await ctx.send(f"**{ctx.author.name}**님이 동전을 던져 **{random.choice(coinsides)}**이 나왔습니다!")

    @commands.command()
    async def 슈프림(self, ctx, *, text: commands.clean_content(fix_channel_mentions=True)):
        parser = argparser.Arguments()
        parser.add_argument('input', nargs="+", default=None)
        parser.add_argument('-d', '--dark', action='store_true')
        parser.add_argument('-l', '--light', action='store_true')

        args, valid_check = parser.parse_args(text)
        if not valid_check:
            return await ctx.send(args)

        inputText = urllib.parse.quote(' '.join(args.input))
        if len(inputText) > 500:
            return await ctx.send(f"**{ctx.author.name}**, 500자 미만으로만 가능해요.")

        darkorlight = ""
        if args.dark:
            darkorlight = "dark=true"
        if args.light:
            darkorlight = "light=true"
        if args.dark and args.light:
            return await ctx.send(f"**{ctx.author.name}**, 동시에 --dark 와 --light를 지정할 수 없어요..")

        await self.api_img_creator_(ctx, f"https://api.alexflipnote.dev/supreme?text={inputText}&{darkorlight}", "supreme.png")

    @commands.command(aliases=['색깔'])
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def 색(self, ctx, colour: str):
        """ View the colour HEX details """
        async with ctx.channel.typing():
            if not permissions.can_embed(ctx):
                return await ctx.send("임베딩을 할 수 없어요 ;-;")

            if colour == "랜덤" or colour == "무작위":
                colour = "%06x" % random.randint(0, 0xFFFFFF)

            if colour[:1] == "#":
                colour = colour[1:]

            if not re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', colour):
                return await ctx.send("You're only allowed to enter HEX (0-9 & A-F)")

            try:
                r = await http.get(f"https://api.alexflipnote.dev/colour/{colour}", res_method="json", no_cache=True)
            except aiohttp.ClientConnectorError:
                return await ctx.send("API에 문제가 발생했어요...")
            except aiohttp.ContentTypeError:
                return await ctx.send("API가 값을 제대로 출력하지 ...")

            embed = discord.Embed(colour=0xeff0f1)
            embed.set_thumbnail(url=r["image"])
            embed.set_image(url=r["image_gradient"])

            embed.add_field(name="HEX", value=r['hex'], inline=True)
            embed.add_field(name="RGB", value=r['rgb'], inline=True)
            embed.add_field(name="Int", value=r['int'], inline=True)
            embed.add_field(name="Brightness", value=r['brightness'], inline=True)

            await ctx.send(embed=embed, content=f"{ctx.invoked_with.title()} 이름: **{r['name']}**")

    @commands.command()
    @commands.cooldown(rate=1, per=2.0, type=commands.BucketType.user)
    async def 사전(self, ctx, *, search: commands.clean_content):
        """ Find the 'best' definition to your words """
        async with ctx.channel.typing():
            try:
                url = await http.get(f'https://api.urbandictionary.com/v0/define?term={search}', res_method="json")
            except Exception:
                return await ctx.send("불러오는 중에 예외가 발생했어요.")

            if not url:
                return await ctx.send("API가 망가진 것 같아요...")

            if not len(url['list']):
                return await ctx.send("사전에 없는 말이에요...")

            result = sorted(url['list'], reverse=True, key=lambda g: int(g["thumbs_up"]))[0]

            definition = result['definition']
            if len(definition) >= 1000:
                definition = definition[:1000]
                definition = definition.rsplit(' ', 1)[0]
                definition += '...'

            await ctx.send(f"📚 **{result['word']}** 의 의미```fix\n{definition}```")

    @commands.command()
    async def 거꾸로(self, ctx, *, text: str):
        t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
        await ctx.send(f"🔁 {t_rev}")

    @commands.command()
    async def 비밀번호(self, ctx, nbytes: int = 18):
        if nbytes not in range(3, 1401):
            return await ctx.send("I only accept any numbers between 3-1400")
        if hasattr(ctx, 'guild') and ctx.guild is not None:
            await ctx.send(f"**{ctx.author.name}**님에게 임의의 비밀번호를 보냈어요!")
        await ctx.author.send(f"🎁 **Here is your password:**\n{secrets.token_urlsafe(nbytes)}")

    @commands.command()
    async def 평가(self, ctx, *, thing: commands.clean_content):
        rate_amount = random.uniform(0.0, 100.0)
        await ctx.send(f"`{thing}`님을 **{round(rate_amount, 4)} / 100** 로 평가했어요!")

    @commands.command(aliases=['맥주', '비어', '한잔해'])
    async def 술(self, ctx, user: discord.Member = None, *, reason: commands.clean_content = ""):
        """ Give someone a beer! 🍻 """
        if not user or user.id == ctx.author.id:
            return await ctx.send(f"**{ctx.author.name}**: 건배!🎉🍺")
        if user.id == self.bot.user.id:
            return await ctx.send("*같이 한잔 하자고요? 좋아요!* 🍻")
        if user.bot:
            return await ctx.send(f"I would love to give beer to the bot **{ctx.author.name}**, 봇들은 술을 못 마실 거라 생각해요 :/")

        beer_offer = f"**{user.name}**님 **{ctx.author.name}**님에게 커플샷🍻 제의가 왔어요!"
        beer_offer = beer_offer + f"\n\n**Reason:** {reason}" if reason else beer_offer
        msg = await ctx.send(beer_offer)

        def reaction_check(m):
            if m.message_id == msg.id and m.user_id == user.id and str(m.emoji) == "🍻":
                return True
            return False

        try:
            await msg.add_reaction("🍻")
            await self.bot.wait_for('raw_reaction_add', timeout=30.0, check=reaction_check)
            await msg.edit(content=f"**{user.name}**님과**{ctx.author.name}**님은 서로 즐겁게 커플샷을 마셨습니다. 🍻")
        except asyncio.TimeoutError:
            await msg.delete()
            await ctx.send(f"아마도 **{user.name}**님은 **{ctx.author.name}**님과 같이 마시기 싫으신 것 같아요 ;-;")
        except discord.Forbidden:
            # Yeah so, bot doesn't have reaction permission, drop the "offer" word
            beer_offer = f"**{user.name}**님 **{ctx.author.name}**님에게 커플샷🍻 제의가 왔어요!"
            beer_offer = beer_offer + f"\n\n**Reason:** {reason}" if reason else beer_offer
            await msg.edit(content=beer_offer)

    @commands.command(aliases=['하우 핫'])
    async def 핫(self, ctx, *, user: discord.Member = None):
        """ Returns a random percent for how hot is a discord user """
        user = user or ctx.author

        random.seed(user.id + round(time.time()))
        r = random.randint(1, 100)
        hot = r / 1.17

        emoji = "💔"
        if hot > 25:
            emoji = "❤"
        if hot > 50:
            emoji = "💖"
        if hot > 75:
            emoji = "💞"

        await ctx.send(f"**{user.name}**님은 **{hot:.2f}%**만큼 H.O.T 해요! {emoji}")

    @commands.command()
    async def 알림(self, ctx):
        """ Notice me senpai! owo """
        if not permissions.can_upload(ctx):
            return await ctx.send("메시지를 보낼 수 없어요 ;-;")

        bio = BytesIO(await http.get("https://i.alexflipnote.dev/500ce4.gif", res_method="read"))
        await ctx.send(file=discord.File(bio, filename="noticeme.gif"))

    @commands.command(aliases=['슬롯'])
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def 내기(self, ctx):
        """ Roll the slot machine """
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"

        if (a == b == c):
            await ctx.send(f"{slotmachine} 모두 매칭되었어요! 축하드려요! 🎉")
        elif (a == b) or (a == c) or (b == c):
            await ctx.send(f"{slotmachine} 2개가 맞았어요! 축하드려요! 🎉")
        else:
            await ctx.send(f"{slotmachine} 아무것도 맞은게 없어요 😢")


def setup(bot):
    bot.add_cog(Fun_Commands_ko(bot))
