from nextcord.ext import commands
import sqlite3
from dotenv import load_dotenv
import os

class Socials(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def youtube(self, ctx):
        conn = sqlite3.connect(os.getenv("DATABASE_PATH"))
        c = conn.cursor()
        c.execute(f"SELECT youtube FROM servers WHERE serverID = '{ctx.guild.id}'")

        results = c.fetchone()

        await ctx.send(f"https://www.youtube.com/channel/{results[0]}")

    @commands.command()
    async def twitch(self, ctx):
        conn = sqlite3.connect(os.getenv("DATABASE_PATH"))
        c = conn.cursor()
        c.execute(f"SELECT twitch FROM servers WHERE serverID = '{ctx.guild.id}'")

        results = c.fetchone()

        await ctx.send(f"https://www.twitch.tv/{results[0]}")

    @commands.command()
    async def facebook(self, ctx):
        conn = sqlite3.connect(os.getenv("DATABASE_PATH"))
        c = conn.cursor()
        c.execute(f"SELECT facebook FROM servers WHERE serverID = '{ctx.guild.id}'")

        results = c.fetchone()

        await ctx.send(f"https://www.facebook.com/{results[0]}")

    @commands.command()
    async def twitter(self, ctx):
        conn = sqlite3.connect(os.getenv("DATABASE_PATH"))
        c = conn.cursor()
        c.execute(f"SELECT twitter FROM servers WHERE serverID = '{ctx.guild.id}'")

        results = c.fetchone()

        await ctx.send(f"https://twitter.com/{results[0]}")

    @commands.command()
    async def website(self, ctx):
        conn = sqlite3.connect(os.getenv("DATABASE_PATH"))
        c = conn.cursor()
        c.execute(f"SELECT website FROM servers WHERE serverID = '{ctx.guild.id}'")

        results = c.fetchone()

        await ctx.send(results[0])    

def setup(bot):
    bot.add_cog(Socials(bot))
    load_dotenv()