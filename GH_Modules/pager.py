import discord
import asyncio
from discord.ext import commands


async def start_page(bot, ctx, lists: list, time: int = 30, embed=False):
    counts = len(lists) - 1

    emoji_list = ["⬅", "⏹", "➡"]

    def check(reaction, user):
        return str(reaction.emoji) in emoji_list and user == ctx.author

    if embed is True:
        msg = await ctx.send(embed=lists[0])
    else:
        msg = await ctx.send(lists[0])
    counted = 0

    for x in emoji_list:
        await msg.add_reaction(x)

    try:
        while True:
            reaction, user = await bot.wait_for("reaction_add", timeout=time, check=check)
            if str(reaction.emoji) == emoji_list[1]:
                try:
                    await msg.clear_reactions()
                except discord.Forbidden:
                    await msg.remove_reaction(emoji_list[0], msg.author)
                    await msg.remove_reaction(emoji_list[1], msg.author)
                    await msg.remove_reaction(emoji_list[2], msg.author)
                break
            elif str(reaction.emoji) == emoji_list[2]:
                try:
                    await msg.remove_reaction(emoji_list[2], ctx.author)
                except discord.Forbidden:
                    pass
                counted += 1
                if counted > counts:
                    wd = await ctx.send("이미 마지막 페이지입니다.")
                    await wd.delete(delay=3)
                    counted = counts
                    continue
                if embed is True:
                    await msg.edit(embed=lists[counted])
                else:
                    await msg.edit(content=lists[counted])
            elif str(reaction.emoji) == emoji_list[0]:
                try:
                    await msg.remove_reaction(emoji_list[0], ctx.author)
                except discord.Forbidden:
                    pass
                counted -= 1
                if counted < 0:
                    wd = await ctx.send("이미 첫번째 페이지입니다.")
                    await wd.delete(delay=3)
                    counted = 0
                    continue
                if embed is True:
                    await msg.edit(embed=lists[counted])
                else:
                    await msg.edit(content=lists[counted])
    except asyncio.TimeoutError:
        ended_msg = await ctx.send("시간을 초과했습니다.")
        try:
            await msg.clear_reactions()
        except discord.Forbidden:
            await msg.remove_reaction(emoji_list[0], msg.author)
            await msg.remove_reaction(emoji_list[1], msg.author)
            await msg.remove_reaction(emoji_list[2], msg.author)
        await ended_msg.delete(delay=5)
        return
