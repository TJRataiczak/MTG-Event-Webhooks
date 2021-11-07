from nextcord.ext import commands
import requests


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases = ["doggo", "pupper"])
    async def dog(self, ctx):
        url = "https://random.dog/woof.json"
        info = requests.get(url=url)
        data = info.json()
        await ctx.send(data['url'])


def setup(bot):
    bot.add_cog(Fun(bot))
