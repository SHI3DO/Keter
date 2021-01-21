import os

import discord

from evs import default
from evs.data import Bot, HelpFormat

config = default.get("config.json")
print("Logging in...")

bot = Bot(
    command_prefix=config.prefix,
    prefix=config.prefix,
    command_attrs=dict(hidden=True),
    help_command=None,
    intents=discord.Intents.all()
)

for name in ['cogs.'+file[:-3] for file in os.listdir("cogs") if file.endswith('.py')]:
    bot.load_extension(name)

try:
    bot.run(config.token)
except Exception as e:
    print(f'Error when logging in: {e}')
