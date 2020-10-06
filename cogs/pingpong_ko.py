import discord
import openpyxl
import asyncio
import datetime
import requests
from bs4 import BeautifulSoup
import traceback
import bs4
from urllib.request import urlopen, Request
import urllib
import smtplib
import sys
import pkg_resources
import aiohttp
import os
import time
from pyowm import OWM
import sqlite3
from difflib import SequenceMatcher
import koreanbots
import dbl
import qrcode
from requests import get
import Dtime
import neispy
import tasks
import argparse
from captcha.image import ImageCaptcha
import random
from Dtime import Uptime
import ast
from discord.ext import commands
from discord.utils import get
from urllib.request import Request
from urllib.request import URLError
from urllib.request import HTTPError
from urllib.request import urlopen
from urllib.request import Request, urlopen
from urllib.request import quote
from bs4 import BeautifulSoup
from urllib import parse
import warnings
import json
import re
import requests as rq
from bs4 import BeautifulSoup as bs
from urllib.parse import quote
from urllib.request import urlopen, Request

pingpongurl = 핑퐁토큰1
pingpongauth = 핑퐁토큰2


class pingpong_ko(commands.Cog):
  def __init__(self, client):
    self.client = client

  # Commands
  async def 케테르(self, ctx, *, content: str):

    header = {
      'Authorization': pingpongauth,
      'Content-Type': 'application/json'
    }
    param = {
      'request': {
        'query': content
      }
    }
    async with aiohttp.ClientSession(headers=header) as session:
      async with session.post(pingpongurl + f'/{ctx.author.id}', json=param) as res:
        data = await res.json()
        assert 'response' in data
        assert 'replies' in data['response']
        for reply in data['response']['replies']:
          if 'text' in reply:
            await ctx.send(reply['text'])


def setup(client):
  client.add_cog(pingpong_ko(client))
