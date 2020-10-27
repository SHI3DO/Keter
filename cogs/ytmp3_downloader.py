import discord
import asyncio
from discord.ext import commands
from evs import default

config = default.get("config.json")
downloaddir = config.ytmp3_upload_dir
import os
import youtube_dl
import random
import time

class ytmusic_downloader(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def music_download(self, ctx, *, content:str):
        url = content
        ydl_opts = {
            'format': 'bestaudio/best',
            'extractaudio': True,
            'audioformat': 'mp3',
            'outtmpl': downloaddir + "/%(title)s-%(id)s.%(ext)s"
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        await ctx.send("Downloaded Successfully")
        for file in os.listdir(downloaddir):
            if file.endswith(".webm"):
                src = os.path.join(downloaddir, file)
                namesssss = str(random.randrange(1,1000000000))
                os.rename(src, downloaddir + "/"+ namesssss + ".mp3")
        await ctx.send("Converted Successfully")
        await ctx.send("http://keter.cf/mp3/" + namesssss + ".mp3")
        await ctx.send("파일은 1분 후에 삭제됩니다.")
        await asyncio.sleep(60)
        os.remove(downloaddir + "/"+ namessssss + ".mp3")

def setup(client):
    client.add_cog(ytmusic_downloader(client))
