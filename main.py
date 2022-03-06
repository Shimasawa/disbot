import discord
from discord.ext import commands

import json



with open("databox/token.json","r") as f:
    token_json = json.load(f)

TOKEN = token_json["TOKEN"]

bot = commands.Bot(command_prefix="k!")

bot.load_extension("Cogs.sum_num")

bot.run(TOKEN)