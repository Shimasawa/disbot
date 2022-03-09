import json
import discord
from discord.ext import commands
import re

class Sumcoin(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self._last_member = None
    
    @commands.command()
    async def test(self,ctx,message_id,limit_num):
        
        if int(ctx.author.id) != 535752156947677195:
            print("管理者以外の実行")
            return

        await ctx.channel.send("読み込み中")
        
        l = []
        
        async for message in ctx.channel.history(limit=int(limit_num)+2):

            l.append(message)
            
            if message.id == int(message_id):
                break
        
        if len(l) == int(limit_num):
            await ctx.channel.send("メッセージを取得できませんでした。\n__取得したメッセージのリスト__")
            await ctx.channel.send("\n".join([m.content for m in l]))
            return

        await ctx.channel.send("{}件のメッセージを取得しました".format(len(l)))

        with open("databox/user_data.json","r") as f:
            d = json.load(f)
        
        for i in l:
                        
            if "k!" in i.content or i.author.bot:
                continue
            print(i.content)
            num = re.search(r"[0-9]+",i.content)
            if num == None:
                continue

            elif str(i.author.id) in d:
                d[str(i.author.id)] += int(num.group())
            
            else:
                d[str(i.author.id)] = int(num.group())

        with open("databox/user_data.json","w") as f:
            json.dump(d,f,indent=2)

        await ctx.channel.send("\n".join([m.content for m in l]))
        
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