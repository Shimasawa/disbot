import discord
from discord.ext import commands

import os
from dotenv import load_dotenv

class Originalhelp(commands.DefaultHelpCommand):
    def __init__(self):
        super().__init__()
        self.commands_heading = "コマンド名 : "
        self.no_category = "その他"
        self.command_attrs["help"] = "ヘルプコマンド"

    def get_ending_note(self):
        return (f"コマンドの説明 : {prefix}help コマンド名\n"
                f"カテゴリの説明 : {prefix}help カテゴリ名")


load_dotenv(override=True)
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
prefix = "k!"

bot = commands.Bot(command_prefix=prefix,intents=intents,help_command=Originalhelp())

files = [file[:-3] for file in os.listdir("Cogs") if file.endswith(".py")]

for filename in files:
    bot.load_extension(f"Cogs.{filename}")

bot.run(TOKEN)