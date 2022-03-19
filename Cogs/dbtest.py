import discord
from discord.ext import commands

import aiosqlite

class testSqlite3(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self._last_member = None
    
    @commands.command()
    async def testsql(self,ctx,sql):
        try:
            async with aiosqlite.connect("databox/coin.db") as db:
                await db.execute(sql)
                await db.commit()
                await ctx.channel.send("データベースに反映しました")
        except:
            await ctx.channel.send("何らかのエラーが発生したため実行できませんでした")

    @commands.command()
    async def printsql(self,ctx,sql):
        try:
            async with aiosqlite.connect("databox/coin.db") as db:
                async with db.execute(sql) as cursor:
                    for i in await cursor.fetchall():
                        print(i)
                        await ctx.channel.send(str(list(i)))

        except:
            await ctx.channel.send("何らかのエラーが発生したため実行できませんでした")



def setup(bot):
    return bot.add_cog(testSqlite3(bot))