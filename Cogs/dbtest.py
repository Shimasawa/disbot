import discord
from discord.ext import commands

import sqlite3

class testSqlite3(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self._last_member = None
    
    @commands.command()
    async def memo(self,ctx,mode,num1,num2):
        con = sqlite3.connect("databox/coin.db")
        c = con.cursor()
        if mode == "add":
            #c.execute("CREATE TABLE test(userid NUMERIC,num NUMERIC)")
            c.execute(f"insert into test values ({int(num1)},{int(num2)})")
            con.commit()
        if mode == "view":
            c.execute(f"select * FROM test WHERE userid = {int(num1)}")
            print([i[1] for i in c.fetchall()])
            await ctx.channel.send("\n".join([str(i[1]) for i in c.fetchall()]))
        con.close()



def setup(bot):
    return bot.add_cog(testSqlite3(bot))