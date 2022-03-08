import json
import discord
from discord.ext import commands
import re

class Sumcoin(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self._last_member = None
    
    @commands.command()
    async def test(self,ctx,message_id):
        await ctx.channel.send("読み込み中")
        l = []
        async for message in ctx.channel.history():
            l.append(message)
            if message.id == int(message_id):
                break
        
        with open("databox/user_data.json","r") as f:
            d = json.load(f)
        
        for i in l:

            if str(i.author.id) in d:
                d[str(i.author.id)] += 1
            else:
                d[str(i.author.id)] = 0
        with open("databox/user_data.json","w") as f:
            json.dump(d,f)
        await ctx.channel.send(str(len([m.content for m in l])))
        
        #msg = discord.utils.get([message async for message in ctx.channel.history()],)
        
        #if msg == None:
        #   await ctx.channel.send("何もありませんでした")
        #else:
        #    await ctx.channel.send(msg)
        #l = [message.content async for message in ctx.channel.history(limit=50)]
        #l = len("".join(l))
        #await ctx.channel.send(str(l))
    
def setup(bot):
    return bot.add_cog(Sumcoin(bot))