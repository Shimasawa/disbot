import json
import discord
from discord.ext import commands
import re

class Sumcoin(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self._last_member = None
    
    @commands.command()
    async def cal_ch_num(self,ctx,message_id,limit_num):
        
        if int(ctx.author.id) != 535752156947677195:
            await ctx.channel.send("管理者以外の実行")
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
            num = re.search(r"[0-9]+",i.content)
            if num == None:
                continue

            elif str(i.author.id) in d:
                d[str(i.author.id)] += int(num.group())
            
            else:
                d[str(i.author.id)] = int(num.group())

        with open("databox/user_data.json","w") as f:
            json.dump(d,f,indent=2)
        await ctx.channel.send("処理を終了しました")
        try:
            await ctx.channel.send("__取得したメッセージリスト__\n```{}```".format("\n".join([m.content for m in l])))
        except:
            await ctx.channel.send("取得した中で最も古いメッセージ\n{}".format(l[-1].content))
    @commands.command()    
    async def set_num(self,ctx,user_id,num):
        if int(ctx.author.id) != 535752156947677195:
            await ctx.channel.send("管理者以外の実行")
            return
        with open("databox/user_data.json","r") as f:
            d = json.load(f)
        d[str(user_id)] = int(num)
        with open("databox/user_data.json","w") as f:
            json.dump(d,f,indent=2)
        await ctx.channel.send("設定しました")
    
    @commands.command()
    async def look_num(self,ctx,user_id=None):
        if int(ctx.author.id) != 535752156947677195:
            await ctx.channel.send("管理者以外の実行")
            return
        with open("databox/user_data.json","r") as f:
            d = json.load(f)
        
        if user_id == None:
            await ctx.channel.send("```json\n{}```".format(str(d)))
        else:
            await ctx.channel.send(str(d[str(user_id)]))
    
    @commands.command()
    async def name_list(self,ctx):
        if int(ctx.author.id) != 535752156947677195:
            await ctx.channel.send("管理者以外の実行")
            return
        with open("databox/user_data.json","r") as f:
            d = json.load(f)
        for i in d.keys():
            user = discord.get_user(int(i))
            await ctx.channel.send("{}:{}".format(user.name,d[str(i)]))

def setup(bot):
    return bot.add_cog(Sumcoin(bot))