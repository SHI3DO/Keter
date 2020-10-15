import discord
import asyncio
import os
from discord.ext import commands
import urllib
from urllib.request import URLError
from urllib.request import HTTPError
from urllib.request import urlopen
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote
import re
import warnings
import requests
import unicodedata
import json

from evs import default
from evs.data import Bot, HelpFormat
config = default.get("config.json")

client_id = config.translation_client_id
client_secret = config.translation_client_secret

class Translate(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    #Ko to En
    @commands.command()
    async def 한영(self, ctx):
        reply = ctx.message.content.split(" ")
        if len(reply) > 1:
            for i in range(2, len(reply)):
                reply[1] = reply[1] + " " + reply[i]

        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        try:
            if len(reply) == 1:
                await ctx.trigger_typing()
                embed = discord.Embed(title="에러", description="단어 혹은 문장이 입력되지 않았어요. 다시한번 확인해주세요.", color=0xff0051)
               
                await ctx.send(embed = embed)
            else:
                await ctx.trigger_typing()
                dataParmas = "source=ko&target=en&text=" + reply[1]
                # Make a Request Instance
                request = Request(baseurl)
                # add header to packet
                request.add_header("X-Naver-Client-Id", client_id)
                request.add_header("X-Naver-Client-Secret", client_secret)
                response = urlopen(request, data=dataParmas.encode("utf-8"))

                responsedCode = response.getcode()
                if (responsedCode == 200):
                    response_body = response.read()
                    # response_body -> byte string : decode to utf-8
                    api_callResult = response_body.decode('utf-8')
                    # JSON data will be printed as string type. So need to make it back to type JSON(like dictionary)
                    api_callResult = json.loads(api_callResult)
                    # Final Result
                    translatedText = api_callResult['message']['result']["translatedText"]
                    embed = discord.Embed(title="번역결과", description=translatedText, color=0xff0051)
                    await ctx.send(embed=embed)
                else:
                    await ctx.trigger_typing()
                    embed = discord.Embed(title="에러", description="에러 코드: " + responsedCode, color=0xff0051)

                    await ctx.send(embed = embed)
        except HTTPError as e:
            await ctx.trigger_typing()
            embed = discord.Embed(title="에러", description="오류가 발생하여 번역에 실패했어요.", color=0xff0051)

            await ctx.send(embed = embed)

    #En to Ko
    @commands.command()
    async def 영한(self, ctx):
        reply = ctx.message.content.split(" ")
        if len(reply) > 1:
            for i in range(2, len(reply)):
                reply[1] = reply[1] + " " + reply[i]

        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        try:
            if len(reply) == 1:
                await ctx.trigger_typing()
                embed = discord.Embed(title="에러", description="단어 혹은 문장이 입력되지 않았어요. 다시한번 확인해주세요.", color=0xff0051)

                await ctx.send(embed = embed)
            else:
                await ctx.trigger_typing()
                dataParmas = "source=en&target=ko&text=" + reply[1]
                # Make a Request Instance
                request = Request(baseurl)
                # add header to packet
                request.add_header("X-Naver-Client-Id", client_id)
                request.add_header("X-Naver-Client-Secret", client_secret)
                response = urlopen(request, data=dataParmas.encode("utf-8"))

                responsedCode = response.getcode()
                if (responsedCode == 200):
                    response_body = response.read()
                    # response_body -> byte string : decode to utf-8
                    api_callResult = response_body.decode('utf-8')
                    # JSON data will be printed as string type. So need to make it back to type JSON(like dictionary)
                    api_callResult = json.loads(api_callResult)
                    # Final Result
                    translatedText = api_callResult['message']['result']["translatedText"]
                    embed = discord.Embed(title="번역결과", description=translatedText, color=0xff0051)

                    await ctx.send(embed=embed)
                else:
                    await ctx.trigger_typing()
                    embed = discord.Embed(title="에러", description="에러 코드: " + responsedCode, color=0xff0051)

                    await ctx.send(embed = embed)
        except HTTPError as e:
            await ctx.trigger_typing()
            embed = discord.Embed(title="에러", description="오류가 발생하여 번역에 실패했어요.", color=0xff0051)

            await ctx.send(embed = embed)

    #Ko to zh-CN(간체)
    @commands.command()
    async def 한중(self, ctx):
        reply = ctx.message.content.split(" ")
        if len(reply) > 1:
            for i in range(2, len(reply)):
                reply[1] = reply[1] + " " + reply[i]

        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        try:
            if len(reply) == 1:
                embed = discord.Embed(title="에러", description="단어 혹은 문장이 입력되지 않았어요. 다시한번 확인해주세요.", color=0xff0051)

                await ctx.send(embed = embed)
            else:
                await ctx.trigger_typing()
                dataParmas = "source=ko&target=zh-CN&text=" + reply[1]
                # Make a Request Instance
                request = Request(baseurl)
                # add header to packet
                request.add_header("X-Naver-Client-Id", client_id)
                request.add_header("X-Naver-Client-Secret", client_secret)
                response = urlopen(request, data=dataParmas.encode("utf-8"))

                responsedCode = response.getcode()
                if (responsedCode == 200):
                    response_body = response.read()
                    # response_body -> byte string : decode to utf-8
                    api_callResult = response_body.decode('utf-8')
                    # JSON data will be printed as string type. So need to make it back to type JSON(like dictionary)
                    api_callResult = json.loads(api_callResult)
                    # Final Result
                    translatedText = api_callResult['message']['result']["translatedText"]
                    embed = discord.Embed(title="번역결과", description=translatedText, color=0xff0051)

                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title="에러", description="에러 코드: " + responsedCode, color=0xff0051)

                    await ctx.send(embed = embed)
        except HTTPError as e:
            embed = discord.Embed(title="에러", description="오류가 발생하여 번역에 실패했어요.", color=0xff0051)

            await ctx.send(embed = embed)

    #Ko to Ja
    @commands.command()
    async def 한일(self, ctx):
        reply = ctx.message.content.split(" ")
        if len(reply) > 1:
            for i in range(2, len(reply)):
                reply[1] = reply[1] + " " + reply[i]

        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        try:
            if len(reply) == 1:
                embed = discord.Embed(title="에러", description="단어 혹은 문장이 입력되지 않았어요. 다시한번 확인해주세요.", color=0xff0051)

                await ctx.send(embed = embed)
            else:
                await ctx.trigger_typing()
                dataParmas = "source=ko&target=ja&text=" + reply[1]
                # Make a Request Instance
                request = Request(baseurl)
                # add header to packet
                request.add_header("X-Naver-Client-Id", client_id)
                request.add_header("X-Naver-Client-Secret", client_secret)
                response = urlopen(request, data=dataParmas.encode("utf-8"))

                responsedCode = response.getcode()
                if (responsedCode == 200):
                    response_body = response.read()
                    # response_body -> byte string : decode to utf-8
                    api_callResult = response_body.decode('utf-8')
                    # JSON data will be printed as string type. So need to make it back to type JSON(like dictionary)
                    api_callResult = json.loads(api_callResult)
                    # Final Result
                    translatedText = api_callResult['message']['result']["translatedText"]
                    embed = discord.Embed(title="번역결과", description=translatedText, color=0xff0051)

                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title="에러", description="에러 코드: " + responsedCode, color=0xff0051)

                    await ctx.send(embed = embed)
        except HTTPError as e:
            embed = discord.Embed(title="에러", description="오류가 발생하여 번역에 실패했어요.", color=0xff0051)

            await ctx.send(embed = embed)

    #Ja to Ko
    @commands.command()
    async def 일한(self, ctx):
        reply = ctx.message.content.split(" ")
        if len(reply) > 1:
            for i in range(2, len(reply)):
                reply[1] = reply[1] + " " + reply[i]

        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        try:
            if len(reply) == 1:
                embed = discord.Embed(title="에러", description="단어 혹은 문장이 입력되지 않았어요. 다시한번 확인해주세요.", color=0xff0051)

                await ctx.send(embed = embed)
            else:
                dataParmas = "source=ja&target=ko&text=" + reply[1]
                # Make a Request Instance
                request = Request(baseurl)
                # add header to packet
                request.add_header("X-Naver-Client-Id", client_id)
                request.add_header("X-Naver-Client-Secret", client_secret)
                response = urlopen(request, data=dataParmas.encode("utf-8"))

                responsedCode = response.getcode()
                if (responsedCode == 200):
                    response_body = response.read()
                    # response_body -> byte string : decode to utf-8
                    api_callResult = response_body.decode('utf-8')
                    # JSON data will be printed as string type. So need to make it back to type JSON(like dictionary)
                    api_callResult = json.loads(api_callResult)
                    # Final Result
                    translatedText = api_callResult['message']['result']["translatedText"]
                    embed = discord.Embed(title="번역결과", description=translatedText, color=0xff0051)

                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title="에러", description="에러 코드: " + responsedCode, color=0xff0051)

                    await ctx.send(embed = embed)
        except HTTPError as e:
            embed = discord.Embed(title="에러", description="오류가 발생하여 번역에 실패했어요.", color=0xff0051)

            await ctx.send(embed = embed)

    #zh-CN to Ko(간체)
    @commands.command()
    async def 중한(self, ctx):
        reply = ctx.message.content.split(" ")
        if len(reply) > 1:
            for i in range(2, len(reply)):
                reply[1] = reply[1] + " " + reply[i]

        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        try:
            if len(reply) == 1:
                embed = discord.Embed(title="에러", description="단어 혹은 문장이 입력되지 않았어요. 다시한번 확인해주세요.", color=0xff0051)

                await ctx.send(embed = embed)
            else:
                dataParmas = "source=zh-CN&target=ko&text=" + reply[1]
                # Make a Request Instance
                request = Request(baseurl)
                # add header to packet
                request.add_header("X-Naver-Client-Id", client_id)
                request.add_header("X-Naver-Client-Secret", client_secret)
                response = urlopen(request, data=dataParmas.encode("utf-8"))

                responsedCode = response.getcode()
                if (responsedCode == 200):
                    response_body = response.read()
                    # response_body -> byte string : decode to utf-8
                    api_callResult = response_body.decode('utf-8')
                    # JSON data will be printed as string type. So need to make it back to type JSON(like dictionary)
                    api_callResult = json.loads(api_callResult)
                    # Final Result
                    translatedText = api_callResult['message']['result']["translatedText"]
                    embed = discord.Embed(title="번역결과", description=translatedText, color=0xff0051)

                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title="에러", description="에러 코드: " + responsedCode, color=0xff0051)

                    await ctx.send(embed = embed)
        except HTTPError as e:
            embed = discord.Embed(title="에러", description="오류가 발생하여 번역에 실패했어요.", color=0xff0051)

            await ctx.send(embed = embed)



def setup(client):
    client.add_cog(Translate(client))
