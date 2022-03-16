import discord
from discord.ext import commands

import os
from dotenv import load_dotenv


load_dotenv(override=True)
TOKEN = os.getenv("TOKEN")
intents = discord.Intents.default()

bot = commands.Bot(command_prefix="k!",intents=intents)

bot.load_extension("Cogs.sum_num")

bot.run(TOKEN)