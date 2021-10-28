from nextcord.ext import commands
import sqlite3
from dotenv import load_dotenv
import os

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def events(self, ctx):
        await ctx.send(eventbuilder(ctx))
    
    @commands.command()
    async def pioneer(self, ctx):
        await ctx.send(eventbuilder(ctx))

    @commands.command()
    async def modern(self, ctx):
        await ctx.send(eventbuilder(ctx))

    @commands.command()
    async def standard(self, ctx):
        await ctx.send(eventbuilder(ctx))

    @commands.command()
    async def legacy(self, ctx):
        await ctx.send(eventbuilder(ctx))
    
    @commands.command()
    async def sealed(self, ctx):
        await ctx.send(eventbuilder(ctx))

    @commands.command()
    async def draft(self, ctx):
        await ctx.send(eventbuilder(ctx))

    @commands.command()
    async def prerelease(self, ctx):
        await ctx.send(eventbuilder(ctx))

def setup(bot):
    bot.add_cog(Events(bot))
    load_dotenv()

def eventbuilder(ctx):
    conn = sqlite3.connect(os.getenv("DATABASE_PATH"))
    c = conn.cursor()

    if ctx.message.content == "!events":
        c.execute(f"SELECT * FROM events WHERE serverID = '{ctx.guild.id}'")
        results = c.fetchall()
    elif ctx.message.content == "!pioneer":
        c.execute(f"SELECT * FROM events WHERE serverID = '{ctx.guild.id}' AND eventformat = 'Pioneer'")
        results = c.fetchall()
    elif ctx.message.content == "!modern":
        c.execute(f"SELECT * FROM events WHERE serverID = '{ctx.guild.id}' AND eventformat = 'Modern'")
        results = c.fetchall()
    elif ctx.message.content == "!standard":
        c.execute(f"SELECT * FROM events WHERE serverID = '{ctx.guild.id}' AND eventformat = 'Standard'")
        results = c.fetchall()
    elif ctx.message.content == "!legacy":
        c.execute(f"SELECT * FROM events WHERE serverID = '{ctx.guild.id}' AND eventformat = 'Legacy'")
        results = c.fetchall()
    elif ctx.message.content == "!sealed":
        c.execute(f"SELECT * FROM events WHERE serverID = '{ctx.guild.id}' AND eventformat = 'Sealed'")
        results = c.fetchall()
    elif ctx.message.content == "!draft":
        c.execute(f"SELECT * FROM events WHERE serverID = '{ctx.guild.id}' AND eventformat = 'Draft'")
        results = c.fetchall()
    elif ctx.message.content == "!prerelease":
        c.execute(f"SELECT * FROM events WHERE serverID = '{ctx.guild.id}' AND eventformat = 'Prerelease'")
        results = c.fetchall()
    
    conn.close()
    reply = ""

    if results != []:
        for result in results:
            reply += f"{result[2]}: {result[1]}\n"
        return reply
    else:
        return "There are no upcoming events for that format."