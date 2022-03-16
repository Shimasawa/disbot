import discord
from discord.ext import commands

import os
from dotenv import load_dotenv


load_dotenv(override=True)
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="k!",intents=intents)

files = [file[:-3] for file in os.listdir("Cogs") if file.endswith(".py")]

for filename in files:
    bot.load_extension(f"Cogs.{filename}")

bot.run(TOKEN)