import discord
from discord.ext import commands

class Sumcoin(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self._last_member = None
    
    @commands.command()
    async def test(self,ctx):
        await ctx.channel.send("成功")
    
def setup(bot):
    return bot.add_cog(Sumcoin(bot))