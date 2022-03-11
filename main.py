import discord
from discord.ext import commands

import json



with open("databox/token.json","r") as f:
    token_json = json.load(f)

TOKEN = token_json["TOKEN"]
intents = discord.Intents.default()

bot = commands.Bot(command_prefix="k!",intents=intents)

bot.load_extension("Cogs.sum_num")

bot.run(TOKEN)