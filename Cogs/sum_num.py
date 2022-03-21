import json
import discord
from discord.ext import commands
import re
import aiosqlite

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
            
        for i in l:
                            
            if "k!" in i.content or i.author.bot:
                continue
            num = re.search(r"[0-9]+",i.content)
            if num == None:
                continue
            async with aiosqlite.connect(r"databox/main.db") as db:
                cursor = await db.execute(f"select num from coin where user_id = {int(i.author.id)}")
                coin = await cursor.fetchone()
                print(coin)
                if coin == None:
                    await db.execute(f"insert into coin(user_id,num) values({int(i.author.id)},{int(num.group())})")
                else:
                    coin = coin[0] + int(num.group())
                    await db.execute(f"update coin set num = {coin} where user_id = {int(i.author.id)}")
                await db.commit()

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
        await ctx.channel.send("読み込み中")
        with open("databox/user_data.json","r") as f:
            d = json.load(f)
        l = []
        for i in d.keys():
            user = await self.bot.fetch_user(int(i))
            l.append(user.name)
        await ctx.channel.send("```"+"\n".join(["{} : {}".format(uid,num) for uid,num in zip(l,d.values())])+"```")

def setup(bot):
    return bot.add_cog(Sumcoin(bot))