import discord
from discord.ext import commands


class Bot_info(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def info(self,ctx):
        """詳細なヘルプコマンドを表示する"""
        embed = discord.Embed(
            title="黒影-info-",
            description="「黒影」は、メンバーごとに数値を設定することができるbotです。\n__β版につき、全てのコマンドは管理者のみ実行可能__",
        )
        embed.add_field(
            name="prefix",
            value="`k!`",
            inline=False  
        )
        embed.add_field(
            name="cal_ch_num",
            value="引数（トリガーとするメッセージid,探索するメッセージ数）\nトリガーに指定したメッセージまで指定された数だけ探索を行い、ユーザー毎にメッセージに含まれる半角数字を合計、保存します。値は次へ引き継がれます",
            inline=False
        )
        embed.add_field(
            name="set_num",
            value="引数（ユーザーid,数字）\n指定されたユーザーの数字を指定された数字に設定します",
            inline=False
        )
        embed.add_field(
            name="look_num",
            value="引数（ユーザーid(デフォルト=None)）\n指定されたユーザーの所持金を表示します。引数を指定しなかった場合、保存中の辞書データをそのまま出力します",
            inline=False
        )
        embed.add_field(
            name="name_list",
            value="サーバー全員の現在の所持金を表示します",
            inline=False
        )
        await ctx.channel.send(embed=embed)

def setup(bot):
    return bot.add_cog(Bot_info(bot))